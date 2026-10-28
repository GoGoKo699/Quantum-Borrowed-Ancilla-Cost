"""Finite algebra and matrix checks for the borrowed-CCZ precision law.

The universal bounds are analytical; this program checks their finite identities
and explicit construction. Run from any directory. Python 3.11+ and NumPy.
"""

from __future__ import annotations

import argparse
from fractions import Fraction as F
from itertools import product
import json
from math import asin, ceil, comb, pi, sin
from pathlib import Path

import numpy as np


def choose(n: int, k: int) -> int:
    return comb(n, k) if 0 <= k <= n else 0


def wrap(x: F) -> F:
    """Principal phase in units of pi, with interval [-1, 1)."""
    return x - 2 * ((x + 1) // 2)


def phases(n: int) -> list[F]:
    a = F(1, 4 * (n - 1))
    values = []
    for k in range(n + 1):
        p = a - F(n + 3, 2 * n * (n - 1)) * k + F(3, 2 * n * (n - 1)) * k * k
        d = comb(n, k)
        values.append(wrap(d * p - choose(n - 3, k - 3)) / d)
    return values


def exact_checks() -> dict:
    small = {
        3: ['1/8', '-1/8', '1/8', '-1/8'],
        4: ['1/12', '-1/12', '0', '1/12', '-1/12'],
        5: ['1/16', '-1/16', '-3/80', '3/80', '1/16', '-1/16'],
        6: ['1/20', '-1/20', '-1/20', '0', '1/20', '1/20', '-1/20'],
        7: ['1/24', '-1/24', '1/24', '-19/840', '19/840', '-1/24', '1/24', '-1/24'],
    }
    sector_checks = 0
    for n in range(3, 101):
        a = F(1, 4 * (n - 1))
        values = phases(n)
        weights = {0: -(n - 2), 1: 1, n - 1: -1, n: n - 2}
        assert [values[k] for k in (0, 1, n - 1, n)] == [a, -a, a, -a]
        assert max(map(abs, values)) == a
        if n in small:
            assert values == list(map(F, small[n]))
        for k, theta in enumerate(values):
            p = a - F(n + 3, 2 * n * (n - 1)) * k + F(3, 2 * n * (n - 1)) * k * k
            assert (comb(n, k) * (p - theta) - choose(n - 3, k - 3)) % 2 == 0
            sector_checks += 1
        for j in range(3):
            assert sum(c * choose(n - 2, k - j) for k, c in weights.items()) == 0
        assert sum(c * comb(n, k) for k, c in weights.items()) == 0
        assert sum(c * choose(n - 3, k - 3) for k, c in weights.items()) == 1
        # At the four edge sectors the weighted common probe has equal mass
        # on the +a and -a residual eigenphases.
        mass = {a: 0, -a: 0}
        for k, c in weights.items():
            mass[values[k]] += abs(c) * comb(n, k)
        assert mass[a] == mass[-a] == 2 * (n - 1)

    # Independent basis enumeration of the target's negative eigenvalues.
    for n in range(3, 11):
        counts = [0] * (n + 1)
        for bits in product((0, 1), repeat=n):
            counts[sum(bits)] += int(all(bits[:3]))
        assert counts == [choose(n - 3, k - 3) for k in range(n + 1)]

    # Direct six-gate diagonal circuit, independent of the sector construction.
    for bits in product((0, 1), repeat=3):
        k = sum(bits)
        pair_sum = sum(bits[i] * bits[j] for i in range(3) for j in range(i + 1, 3))
        circuit_phase = F(1, 8) - F(k, 4) + F(pair_sum, 2)
        target_phase = int(all(bits))
        assert wrap(circuit_phase - target_phase) == F((-1) ** k, 8)

    return {
        'N_range': [3, 100],
        'sector_phase_identities': sector_checks,
        'small_N_phase_rows_in_pi_units': {str(n): row for n, row in small.items()},
        'target_basis_enumeration_N': [3, 10],
        'zero_borrowed_diagonal_circuit_basis_states': 8,
    }


def apply_pair_left(w: np.ndarray, gate: np.ndarray, first: int, second: int) -> np.ndarray:
    """Apply a pair gate by explicit bit-index updates, with data in low 3 bits."""
    dim = w.shape[0]
    output = np.zeros_like(w)
    mask = (1 << first) | (1 << second)
    for source in range(dim):
        local = ((source >> first) & 1) + 2 * ((source >> second) & 1)
        for target_local in range(4):
            target = (source & ~mask) | ((target_local & 1) << first) | (((target_local >> 1) & 1) << second)
            output[target] += gate[target_local, local] * w[source]
    return output


def conserving_pair(rng: np.random.Generator) -> np.ndarray:
    z = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
    q, _ = np.linalg.qr(z)
    gate = np.zeros((4, 4), dtype=complex)
    gate[0, 0], gate[3, 3] = np.exp(1j * rng.uniform(-pi, pi, size=2))
    gate[np.ix_([1, 2], [1, 2])] = q
    return gate


def circuit_checks(rng: np.random.Generator) -> dict:
    largest_character_residual = 0.0
    largest_unitarity_residual = 0.0
    count = 0
    for n in (3, 4, 5, 6):
        dim = 1 << n
        charges = np.array([x.bit_count() for x in range(dim)])
        sectors = [np.flatnonzero(charges == k) for k in range(n + 1)]
        sign = np.array([-1 if x & 7 == 7 else 1 for x in range(dim)])
        tau = np.zeros(dim)
        for k, c in {0: n - 2, 1: 1, n - 1: 1, n: n - 2}.items():
            tau[sectors[k]] = c / (4 * (n - 1))
        for _ in range(6):
            w = np.eye(dim, dtype=complex)
            for _ in range(24):
                first, second = rng.choice(n, size=2, replace=False)
                w = apply_pair_left(w, conserving_pair(rng), int(first), int(second))
            unitary_residual = float(np.max(np.abs(w.conj().T @ w - np.eye(dim))))
            assert unitary_residual < 1e-11
            largest_unitarity_residual = max(largest_unitarity_residual, unitary_residual)
            determinants = [np.linalg.det(w[np.ix_(s, s)]) for s in sectors]
            chi = determinants[1] / determinants[-2] * (determinants[-1] / determinants[0]) ** (n - 2)
            residual = float(abs(chi - 1))
            assert residual < 1e-10
            largest_character_residual = max(largest_character_residual, residual)
            e = sign[:, None] * w
            overlap = abs(np.dot(tau, np.diag(e)))
            assert overlap <= np.cos(pi / (4 * (n - 1))) + 1e-11
            count += 1
    return {
        'N_values': [3, 4, 5, 6],
        'random_circuits': count,
        'pair_gates_per_circuit': 24,
        'max_character_residual': largest_character_residual,
        'max_unitarity_residual': largest_unitarity_residual,
    }


def randomized_channel_checks(rng: np.random.Generator) -> dict:
    count = 0
    worst_excess = 0.0
    rows = []
    for n in (3, 4, 5, 6, 7, 8, 12, 20):
        theta = pi * np.array([float(v) for v in phases(n)])
        a = pi / (4 * (n - 1))
        kernel = 1 - np.cos(theta[:, None] - theta[None, :])
        probs = list(rng.dirichlet(np.ones(n + 1), size=40))
        endpoint = np.zeros(n + 1)
        endpoint[0] = endpoint[1] = 0.5
        probs.append(endpoint)
        for p in probs:
            matrix = np.sqrt(p[:, None] * p[None, :]) * kernel
            eig = np.linalg.eigvalsh(matrix)
            assert abs(float(eig.sum())) < 1e-12
            assert np.count_nonzero(eig > 1e-12) <= 1
            half_trace_norm = float(np.abs(eig).sum() / 2)
            excess = half_trace_norm - sin(a) ** 2
            assert excess < 1e-12
            worst_excess = max(worst_excess, excess)
            count += 1
        endpoint_error = float(np.abs(np.linalg.eigvalsh(
            np.sqrt(endpoint[:, None] * endpoint[None, :]) * kernel
        )).sum() / 2)
        assert abs(endpoint_error - sin(a) ** 2) < 1e-12
        rows.append({'m': n - 3, 'deterministic_error': sin(a), 'randomized_error': sin(a) ** 2})
    return {'input_distributions': count, 'max_upper_bound_excess': worst_excess, 'example_errors': rows}


def resource_counts() -> list[dict]:
    rows = []
    for epsilon in (0.1, 0.01, 0.001, 0.0001):
        row = {'epsilon': epsilon}
        for label, power in (('deterministic', 1), ('randomized', 2)):
            m = max(0, ceil(pi / (4 * asin(epsilon ** (1 / power))) - 2))
            error = sin(pi / (4 * (m + 2))) ** power
            assert error <= epsilon
            if m:
                assert sin(pi / (4 * (m + 1))) ** power > epsilon
            row[label + '_qubits'] = m
        rows.append(row)
    return rows


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write-results', type=Path, help='Write the actual finite-check report to this path.')
    args = parser.parse_args()
    rng = np.random.default_rng(20261028)
    result = {
        'status': 'passed',
        'scope': 'Finite construction and algebra checks; universal optimality and reachability are established by the written proofs and cited theorem.',
        'numpy_version': np.__version__,
        'seed': 20261028,
        'exact': exact_checks(),
        'circuits': circuit_checks(rng),
        'randomized_channel': randomized_channel_checks(rng),
        'resource_counts': resource_counts(),
    }
    if args.write_results:
        args.write_results.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
