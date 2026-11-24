"""Cellular-automata demonstrator: elementary 1D rules and 2D consensus rules.

Includes a local-only load-consensus use case: sensor nodes each hold a noisy
binary state and repeatedly adopt the majority of themselves plus their four
von-Neumann neighbours.  Compared with a centralised global-mean threshold that
needs every reading up front.
"""
from __future__ import annotations
import random

_NEIGHBOURS_4 = ((1, 0), (-1, 0), (0, 1), (0, -1))
_NEIGHBOURS_8 = tuple((dx, dy) for dx in (-1, 0, 1) for dy in (-1, 0, 1)
                      if (dx, dy) != (0, 0))


def _wrap(index, size):
    return index % size


def _clamp(index, size):
    return 0 if index < 0 else size - 1 if index >= size else index


def ca1d_step(cells, rule, boundary='wrap'):
    """One step of a Wolfram elementary cellular automaton (rule 0..255)."""
    if not 0 <= rule <= 255:
        raise ValueError('rule must be in 0..255')
    if boundary not in ('wrap', 'zero'):
        raise ValueError("boundary must be 'wrap' or 'zero'")
    n = len(cells)
    out = []
    for i in range(n):
        if boundary == 'wrap':
            left, right = cells[_wrap(i - 1, n)], cells[_wrap(i + 1, n)]
        else:
            left = cells[i - 1] if i > 0 else 0
            right = cells[i + 1] if i + 1 < n else 0
        index = (left << 2) | (cells[i] << 1) | right
        out.append((rule >> index) & 1)
    return out


def ca1d_run(cells, rule, steps, boundary='wrap'):
    """Return the sequence of states including the initial one."""
    if steps < 0:
        raise ValueError('steps must be >= 0')
    states = [list(cells)]
    for _ in range(steps):
        states.append(ca1d_step(states[-1], rule, boundary))
    return states


def _pick(grid, r, c, boundary):
    rows, cols = len(grid), len(grid[0])
    if boundary == 'wrap':
        return grid[r % rows][c % cols]
    if boundary == 'zero':
        if 0 <= r < rows and 0 <= c < cols:
            return grid[r][c]
        return 0
    raise ValueError("boundary must be 'wrap' or 'zero'")


def ca2d_step(grid, rule='majority', boundary='wrap'):
    """One step of a 2D rule: 'majority' (von Neumann) or 'life' (B3/S23)."""
    if not grid or not grid[0]:
        raise ValueError('grid must be non-empty')
    rows, cols = len(grid), len(grid[0])
    if any(len(row) != cols for row in grid):
        raise ValueError('grid must be rectangular')
    out = [[0] * cols for _ in range(rows)]
    if rule == 'majority':
        for r in range(rows):
            for c in range(cols):
                total = grid[r][c]
                for dr, dc in _NEIGHBOURS_4:
                    total += _pick(grid, r + dr, c + dc, boundary)
                out[r][c] = 1 if total >= 3 else 0
        return out
    if rule == 'life':
        if boundary not in ('wrap', 'zero'):
            raise ValueError("boundary must be 'wrap' or 'zero'")
        for r in range(rows):
            for c in range(cols):
                live = sum(_pick(grid, r + dr, c + dc, boundary) for dr, dc in _NEIGHBOURS_8)
                out[r][c] = 1 if (live == 3 or (grid[r][c] == 1 and live == 2)) else 0
        return out
    raise ValueError("rule must be 'majority' or 'life'")


def ca2d_run(grid, steps, rule='majority', boundary='wrap'):
    if steps < 0:
        raise ValueError('steps must be >= 0')
    states = [[list(row) for row in grid]]
    for _ in range(steps):
        states.append(ca2d_step(states[-1], rule, boundary))
    return states


def _agreement(grid, value):
    cells = [cell for row in grid for cell in row]
    return sum(cell == value for cell in cells) / len(cells)


def load_consensus(size=12, steps=30, noise=0.15, seed=11, majority_fraction=0.65):
    """Local majority voting over noisy binary sensor states.

    The underlying truth is a uniform load level (1 if majority_fraction >= 0.5
    else 0); individual nodes are unreliable.  The CA only uses local
    neighbourhood information.  The centralised baseline thresholds the global
    mean, which requires every reading to be collected first.
    """
    if size < 2:
        raise ValueError('size must be >= 2')
    if steps < 1:
        raise ValueError('steps must be >= 1')
    if not 0.0 <= noise <= 1.0:
        raise ValueError('noise must be in 0..1')
    if not 0.0 <= majority_fraction <= 1.0:
        raise ValueError('majority_fraction must be in 0..1')
    rng = random.Random(seed)
    truth = 1 if majority_fraction >= 0.5 else 0
    flips = 0
    grid = []
    for _ in range(size):
        row = []
        for _ in range(size):
            value = truth if rng.random() < majority_fraction else 1 - truth
            if rng.random() < noise:
                value = 1 - value
                flips += 1
            row.append(value)
        grid.append(row)

    initial = [row[:] for row in grid]
    consensus_step = None
    for step in range(1, steps + 1):
        grid = ca2d_step(grid, 'majority', boundary='wrap')
        first = grid[0][0]
        if consensus_step is None and all(cell == first for row in grid for cell in row):
            consensus_step = step

    final_value = grid[0][0]
    final_agreement = _agreement(grid, final_value)

    cells = [cell for row in initial for cell in row]
    global_mean = sum(cells) / len(cells)
    threshold_value = 1 if global_mean >= 0.5 else 0
    baseline_agreement = _agreement(initial, threshold_value)

    return {
        'engine': 'cellular_automata_cpu',
        'grid_size': size,
        'steps': steps,
        'noise_probability': noise,
        'noise_flips': flips,
        'underlying_truth': truth,
        'initial_agreement': _agreement(initial, truth),
        'initial_disagreement': 1.0 - _agreement(initial, truth),
        'final_value': final_value,
        'final_agreement': final_agreement,
        'consensus_reached': consensus_step is not None,
        'consensus_step': consensus_step,
        'local_majority_correct': final_value == truth,
        'centralized_global_mean_threshold_value': threshold_value,
        'centralized_global_mean_threshold_agreement': baseline_agreement,
        'note': ('Local majority CA reaches agreement using only neighbourhood reads; '
                 'the baseline needs all readings for a global mean. Illustrative only.'),
    }
