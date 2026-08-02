from synth_rearc.core import *


TEMPLATE_TRANSFORMS_79369CC6 = (
    identity,
    rot90,
    rot180,
    rot270,
    hmirror,
    vmirror,
    dmirror,
    cmirror,
)


def verify_79369cc6(I: Grid) -> Grid:
    x0 = height(I)
    x1 = width(I)
    x2 = astuple(THREE, THREE)
    x3 = interval(ZERO, subtract(x0, TWO), ONE)
    x4 = interval(ZERO, subtract(x1, TWO), ONE)
    x5 = None
    x6 = frozenset({FOUR, SIX})
    for x7 in x3:
        for x8 in x4:
            x9 = crop(I, astuple(x7, x8), x2)
            x10 = palette(x9)
            x11 = difference(x10, x6)
            x12 = equality(size(x11), ZERO)
            x13 = both(contained(FOUR, x10), contained(SIX, x10))
            x14 = both(x12, x13)
            if x14:
                x5 = x9
                break
        if x5 is not None:
            break
    if x5 is None:
        return I
    x15 = []
    x16 = set()
    for x17 in TEMPLATE_TRANSFORMS_79369CC6:
        x18 = x17(x5)
        x19 = ofcolor(x18, SIX)
        x20 = tuple(sorted(x19))
        if x20 in x16:
            continue
        x16.add(x20)
        x21 = ofcolor(x18, FOUR)
        x15.append((x19, x21))
    x22 = asindices(I)
    x23 = ofcolor(I, SIX)
    x24 = asindices(x5)
    x25 = interval(NEG_TWO, x0, ONE)
    x26 = interval(NEG_TWO, x1, ONE)
    x27 = I
    for x28 in x25:
        for x29 in x26:
            x30 = astuple(x28, x29)
            x31 = shift(x24, x30)
            x32 = intersection(x31, x22)
            for x33, x34 in x15:
                x35 = shift(x33, x30)
                x36 = difference(x35, x22)
                x37 = equality(size(x36), ZERO)
                if flip(x37):
                    continue
                x38 = intersection(x23, x32)
                x39 = equality(x38, x35)
                if flip(x39):
                    continue
                x40 = shift(x34, x30)
                x27 = fill(x27, FOUR, x40)
                break
    return x27
