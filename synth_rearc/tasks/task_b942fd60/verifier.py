import heapq

from synth_rearc.core import *


def verify_b942fd60(I: Grid) -> Grid:
    x0 = first(ofcolor(I, TWO))
    x1 = I
    x2 = [(ZERO, ZERO, x0, RIGHT)]
    x3 = ONE
    x4 = set()
    x5 = {x0: x0}
    while len(x2) > ZERO:
        x6, _, x7, x8 = heapq.heappop(x2)
        x9 = (x7, x8)
        if x9 in x4:
            continue
        x4.add(x9)
        x10 = x7
        x11 = ZERO
        while True:
            x12 = add(x10, x8)
            x13 = index(I, x12)
            if equality(x13, ZERO):
                x1 = fill(x1, TWO, initset(x12))
                x10 = x12
                x11 = increment(x11)
                continue
            x14 = x12 in x5 and equality(x5[x12], x10)
            x15 = both(x14, equality(x11, ZERO))
            if x15:
                x10 = x12
                continue
            break
        if x13 is None or contained(x12, x5):
            continue
        x16 = add(x6, x11)
        x5[x12] = x10
        if equality(x8[0], ZERO):
            heapq.heappush(x2, (x16, x3, x10, UP))
            x3 = increment(x3)
            heapq.heappush(x2, (x16, x3, x10, DOWN))
            x3 = increment(x3)
        else:
            heapq.heappush(x2, (x16, x3, x10, LEFT))
            x3 = increment(x3)
            heapq.heappush(x2, (x16, x3, x10, RIGHT))
            x3 = increment(x3)
    return x1
