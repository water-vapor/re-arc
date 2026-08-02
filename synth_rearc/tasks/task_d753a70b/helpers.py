from synth_rearc.core import *


def diamond_outline_d753a70b(
    center: IntegerTuple,
    radius: Integer,
    dims: IntegerTuple,
) -> Indices:
    h, w = dims
    ci, cj = center
    cells = set()
    for di in range(-radius, radius + ONE):
        dj = radius - abs(di)
        row = ci + di
        if dj == ZERO:
            col = cj
            if ZERO <= row < h and ZERO <= col < w:
                cells.add((row, col))
            continue
        col_left = cj - dj
        col_right = cj + dj
        if ZERO <= row < h and ZERO <= col_left < w:
            cells.add((row, col_left))
        if ZERO <= row < h and ZERO <= col_right < w:
            cells.add((row, col_right))
    return frozenset(cells)


def diamond_candidates_d753a70b(
    patch: Patch,
    dims: IntegerTuple,
) -> tuple[tuple[Integer, IntegerTuple], ...]:
    cells = tuple(sorted(toindices(patch)))
    if len(cells) == ZERO:
        return tuple()
    rows = tuple(i for i, _ in cells)
    cols = tuple(j for _, j in cells)
    limit = maximum(dims)
    seed = first(cells)
    candidates = []
    for ci in range(minimum(rows) - limit, maximum(rows) + limit + ONE):
        for cj in range(minimum(cols) - limit, maximum(cols) + limit + ONE):
            center = astuple(ci, cj)
            radius = manhattan(initset(seed), initset(center))
            if any(manhattan(initset(cell), initset(center)) != radius for cell in cells):
                continue
            if diamond_outline_d753a70b(center, radius, dims) != frozenset(cells):
                continue
            candidates.append((radius, center))
    candidates.sort(key=lambda item: (item[ZERO], item[ONE][ZERO], item[ONE][ONE]))
    return tuple(candidates)


def transformed_component_d753a70b(
    obj: Object,
    dims: IntegerTuple,
) -> Object:
    x0 = color(obj)
    x1 = toindices(obj)
    if x0 not in (TWO, FIVE):
        return obj
    x2 = diamond_candidates_d753a70b(x1, dims)
    if len(x2) == ZERO:
        return obj
    x3, x4 = first(x2)
    x5 = maximum((ZERO, subtract(x3, ONE))) if equality(x0, TWO) else add(x3, ONE)
    x6 = diamond_outline_d753a70b(x4, x5, dims)
    return recolor(x0, x6)
