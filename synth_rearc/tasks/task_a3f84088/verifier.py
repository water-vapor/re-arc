from synth_rearc.core import *


def verify_a3f84088(I: Grid) -> Grid:
    x0 = objects(I, T, F, F)
    x1 = colorfilter(x0, FIVE)
    x2 = argmax(x1, size)
    x3 = subtract(height(x2), TWO)
    x4 = divide(add(x3, ONE), TWO)
    x5 = I
    x6 = x2
    x7 = (TWO, FIVE, ZERO, FIVE)
    for x8 in range(x4):
        x6 = inbox(x6)
        x9 = x7[x8 % FOUR]
        x5 = fill(x5, x9, x6)
    return x5
