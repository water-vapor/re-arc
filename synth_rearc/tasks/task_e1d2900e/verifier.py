from synth_rearc.core import *


def _candidate_target_e1d2900e(
    loc: IntegerTuple,
    block: Object,
) -> IntegerTuple | None:
    i, j = loc
    bi, bj = ulcorner(block)
    ci, cj = lrcorner(block)
    if i in (bi, ci):
        if j < bj:
            return (i, bj - ONE)
        if j > cj:
            return (i, cj + ONE)
        return None
    if j in (bj, cj):
        if i < bi:
            return (bi - ONE, j)
        if i > ci:
            return (ci + ONE, j)
    return None


def _landing_e1d2900e(
    loc: IntegerTuple,
    blocks: Objects,
) -> IntegerTuple:
    x0 = frozenset({loc})
    x1 = []
    for x2 in blocks:
        x3 = _candidate_target_e1d2900e(loc, x2)
        if x3 is None:
            continue
        x4 = manhattan(x0, x2)
        x1.append((x4, x3))
    if len(x1) == ZERO:
        return loc
    x5 = min(x2 for x2, _ in x1)
    x6 = [x3 for x2, x3 in x1 if x2 == x5]
    if len(x6) != ONE:
        return loc
    return x6[ZERO]


def verify_e1d2900e(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = colorfilter(x0, TWO)
    x2 = sizefilter(x1, FOUR)
    x3 = ofcolor(I, ONE)
    x4 = ofcolor(I, TWO)
    x5 = rbind(_landing_e1d2900e, x2)
    x6 = apply(x5, x3)
    x7 = canvas(ZERO, shape(I))
    x8 = fill(x7, TWO, x4)
    x9 = fill(x8, ONE, x6)
    return x9
