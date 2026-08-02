from synth_rearc.core import *


def verify_963c33f8(I: Grid) -> Grid:
    x0 = height(I)
    x1 = width(I)
    x2 = next(
        j for j in range(x1 - 2)
        if all(I[i][j + k] == NINE for i in (ZERO, ONE) for k in range(3))
        and all(I[TWO][j + k] in (ONE, NINE) for k in range(3))
    )
    x3 = tuple(I[TWO][x2 + k] for k in range(3))
    x4 = fill(I, SEVEN, frozenset((i, j) for i in range(3) for j in range(x2, x2 + 3)))
    x5 = [list(row) for row in x4]
    for x6, x7 in enumerate(range(x2, x2 + 3)):
        x8 = (NINE, NINE, x3[x6])
        if x3[x6] == ONE:
            x9 = next((i for i in range(3, x0) if I[i][x7] == FIVE), None)
            x10 = x0 - 3 if x9 is None else x9 - 3
        else:
            x10 = x0 - 3
        for x11, x12 in enumerate(x8):
            x5[x10 + x11][x7] = x12
    return tuple(tuple(row) for row in x5)
