from synth_rearc.core import *


def _bar_digit_e048c9ed(
    lengths: tuple[Integer, ...],
    length: Integer,
) -> Integer:
    ordered_lengths = dedupe(order(lengths, identity))
    repeated_lengths = tuple(
        candidate for candidate in ordered_lengths if lengths.count(candidate) > ONE
    )
    singleton_lengths = tuple(
        candidate for candidate in ordered_lengths if lengths.count(candidate) == ONE
    )
    digit_base = add(ordered_lengths.index(length), ONE)
    if size(repeated_lengths) == ONE and size(singleton_lengths) == ONE:
        outlier_length = first(singleton_lengths)
        length_gap = abs(subtract(outlier_length, first(repeated_lengths)))
        if length == outlier_length and greater(length_gap, ONE):
            digit_base = length_gap
    return multiply(digit_base, digit_base) % TEN


def verify_e048c9ed(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = matcher(size, ONE)
    x2 = matcher(uppermost, ZERO)
    x3 = fork(both, x1, x2)
    x4 = extract(x0, x3)
    x5 = leftmost(x4)
    x6 = remove(x4, x0)
    x7 = order(x6, uppermost)
    x8 = apply(size, x7)
    x9 = frozenset(
        (_bar_digit_e048c9ed(x8, size(obj)), (uppermost(obj), x5))
        for obj in x7
    )
    x10 = paint(I, x9)
    return x10
