from collections import Counter

from synth_rearc.core import *


NOISE_SHAPES_AEE291AF = (
    frozenset({(ZERO, ZERO)}),
    frozenset({(ZERO, ZERO), (ZERO, ONE)}),
    frozenset({(ZERO, ZERO), (ONE, ZERO)}),
    frozenset({(ZERO, ZERO), (ZERO, ONE), (ONE, ZERO)}),
    frozenset({(ZERO, ZERO), (ZERO, ONE), (ONE, ONE)}),
    frozenset({(ZERO, ZERO), (ONE, ZERO), (ONE, ONE)}),
    frozenset({(ZERO, ONE), (ONE, ZERO), (ONE, ONE)}),
    frozenset({(ZERO, ZERO), (ZERO, ONE), (ZERO, TWO)}),
    frozenset({(ZERO, ZERO), (ONE, ZERO), (TWO, ZERO)}),
)


def _candidate_windows_aee291af(I: Grid) -> Tuple:
    x0 = height(I)
    x1 = width(I)
    x2 = []
    x3 = frozenset({EIGHT})
    x4 = frozenset({TWO, EIGHT})
    for x5 in range(THREE, min(x0, x1) + ONE):
        for x6 in range(subtract(x0, x5) + ONE):
            for x7 in range(subtract(x1, x5) + ONE):
                x8 = crop(I, (x6, x7), (x5, x5))
                x9 = asindices(x8)
                x10 = box(x9)
                x11 = toobject(x10, x8)
                x12 = palette(x11)
                if x12 != x3:
                    continue
                x13 = difference(x9, x10)
                x14 = toobject(x13, x8)
                x15 = palette(x14)
                x16 = difference(x15, x4)
                x17 = equality(x16, frozenset())
                x18 = contained(TWO, x15)
                x19 = both(x17, x18)
                if x19:
                    x2.append(x8)
    return tuple(x2)


def _pattern_aee291af(
    side: Integer,
    red_cells: Indices,
) -> Grid:
    x0 = canvas(EIGHT, (side, side))
    x1 = fill(x0, TWO, red_cells)
    return x1


def _interior_indices_aee291af(
    side: Integer,
) -> Tuple:
    return tuple((i, j) for i in range(ONE, subtract(side, ONE)) for j in range(ONE, subtract(side, ONE)))


def _mutate_pattern_aee291af(
    red_cells: Indices,
    interior: Tuple,
) -> Indices:
    x0 = tuple(red_cells)
    x1 = tuple(idx for idx in interior if idx not in red_cells)
    while True:
        x2 = randint(ONE, min(TWO, len(x0)))
        x3 = frozenset(sample(x0, x2))
        x4 = randint(ZERO, min(TWO, len(x1)))
        x5 = frozenset() if x4 == ZERO else frozenset(sample(x1, x4))
        x6 = difference(red_cells, x3)
        x7 = combine(x6, x5)
        x8 = equality(len(interior), FOUR)
        x9 = branch(x8, TWO, FIVE)
        x10 = branch(x8, THREE, FIVE)
        x11 = both(greater(len(x7), decrement(x9)), greater(increment(x10), len(x7)))
        if both(x11, x7 != red_cells):
            return x7


def _square_patch_aee291af(
    side: Integer,
    loc: IntegerTuple,
) -> Indices:
    x0 = asindices(canvas(EIGHT, (side, side)))
    x1 = shift(x0, loc)
    return x1


def _paint_pattern_aee291af(
    grid: Grid,
    pattern: Grid,
    loc: IntegerTuple,
) -> Grid:
    x0 = asobject(pattern)
    x1 = shift(x0, loc)
    x2 = paint(grid, x1)
    return x2


def _fill_fragment_aee291af(
    grid: Grid,
    patch: Indices,
) -> Grid:
    return fill(grid, EIGHT, patch)


def generate_aee291af(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice((FOUR, FIVE))
        x1 = choice((THREE, FOUR, FOUR, FIVE))
        x2 = _interior_indices_aee291af(x0)
        x3 = branch(equality(x0, FOUR), (THREE, FOUR), (FOUR, FIVE))
        x4 = choice(x3)
        x5 = frozenset(sample(x2, x4))
        x6 = _mutate_pattern_aee291af(x5, x2)
        x7 = _pattern_aee291af(x0, x5)
        x8 = _pattern_aee291af(x0, x6)
        x9 = add(multiply(x0, TWO), EIGHT)
        x10 = x9
        x11 = x9
        x12 = x10
        x13 = canvas(ONE, (x11, x12))
        x14 = tuple([x7] * subtract(x1, ONE) + [x8])
        x15 = list(x14)
        shuffle(x15)
        x16 = []
        x17 = frozenset()
        x18 = ZERO
        while x18 < len(x15):
            x19 = F
            x20 = ZERO
            while x20 < 400:
                x21 = randint(ZERO, subtract(x11, x0))
                x22 = randint(ZERO, subtract(x12, x0))
                x23 = _square_patch_aee291af(x0, (x21, x22))
                x24 = intersection(x17, x23)
                if len(x24) != ZERO:
                    x20 = increment(x20)
                    continue
                x16.append((x15[x18], (x21, x22), x23))
                x17 = combine(x17, x23)
                x19 = T
                break
            if not x19:
                break
            x18 = increment(x18)
        if x18 != len(x15):
            continue
        x25 = x13
        for x26, x27, _ in x16:
            x25 = _paint_pattern_aee291af(x25, x26, x27)
        for _, _, x28 in x16:
            x29 = tuple(idx for idx in intersection(outbox(x28), asindices(x25)) if index(x25, idx) == ONE)
            if len(x29) == ZERO:
                continue
            x30 = randint(ZERO, min(FOUR, len(x29)))
            if x30 == ZERO:
                continue
            x31 = frozenset(sample(x29, x30))
            x25 = _fill_fragment_aee291af(x25, x31)
        x32 = difference(asindices(x25), x17)
        x33 = len(x32)
        x34 = divide(multiply(x33, THREE), 25)
        x35 = divide(multiply(x33, FIVE), 25)
        x36 = unifint(diff_lb, diff_ub, (x34, x35))
        x37 = len(intersection(ofcolor(x25, EIGHT), x32))
        x38 = ZERO
        while both(greater(x36, x37), greater(600, x38)):
            x39 = choice(NOISE_SHAPES_AEE291AF)
            x40 = height(x39)
            x41 = width(x39)
            x42 = randint(ZERO, subtract(x11, x40))
            x43 = randint(ZERO, subtract(x12, x41))
            x44 = shift(x39, (x42, x43))
            x45 = all(index(x25, idx) == ONE for idx in x44)
            if x45:
                x25 = _fill_fragment_aee291af(x25, x44)
                x37 = add(x37, len(x44))
            x38 = increment(x38)
        x46 = _candidate_windows_aee291af(x25)
        x47 = apply(height, x46)
        x48 = maximum(x47)
        x49 = matcher(height, x0)
        x50 = sfilter(x46, x49)
        x51 = Counter(x50)
        x52 = both(equality(x48, x0), both(equality(len(x50), x1), equality(len(x51), TWO)))
        if not x52:
            continue
        x53 = x51[x7]
        x54 = x51[x8]
        x55 = equality(x53, subtract(x1, ONE))
        x56 = equality(x54, ONE)
        x57 = both(x55, x56)
        if not x57:
            continue
        return {"input": x25, "output": x8}
