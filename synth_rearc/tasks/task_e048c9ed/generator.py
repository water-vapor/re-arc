from synth_rearc.core import *


BAR_STARTS_E048C9ED = (ZERO, ZERO, ONE, ONE, ONE, TWO)
TRAILING_PAD_E048C9ED = (ZERO, ZERO, ONE, ONE, TWO, TWO, THREE, FOUR, FIVE, SIX, SEVEN)


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


def _row_layout_e048c9ed(
    diff_lb: float,
    diff_ub: float,
) -> tuple[Integer, tuple[Integer, ...]]:
    start_row = choice((ONE, TWO))
    lower = TWO if start_row == ONE else ONE
    nbars = unifint(diff_lb, diff_ub, (lower, FOUR))
    grid_h = multiply(TWO, nbars)
    if start_row == TWO:
        grid_h = add(grid_h, TWO)
    rows = interval(start_row, grid_h, TWO)
    return grid_h, rows


def _pick_lengths_e048c9ed(
    nrows: Integer,
    diff_lb: float,
    diff_ub: float,
) -> tuple[Integer, ...]:
    ndistinct = unifint(diff_lb, diff_ub, (ONE, min(FOUR, nrows)))
    distinct_lengths = list(interval(TWO, add(TWO, ndistinct), ONE))
    if ndistinct == TWO and nrows >= THREE and choice((T, F, F)):
        lengths = [TWO] * (nrows - ONE) + [choice((FOUR, FIVE))]
        shuffle(lengths)
        return tuple(lengths)
    lengths = list(distinct_lengths)
    while len(lengths) < nrows:
        lengths.append(choice((distinct_lengths[ZERO],) * THREE + tuple(distinct_lengths)))
    shuffle(lengths)
    return tuple(lengths)


def _pick_starts_e048c9ed(nrows: Integer) -> tuple[Integer, ...]:
    if choice((T, T, F)):
        base = choice((ZERO, ONE))
        offsets = []
        for _ in range(nrows):
            step = choice((ZERO, ZERO, ZERO, ONE, NEG_ONE))
            start = max(ZERO, min(TWO, base + step))
            offsets.append(start)
        return tuple(offsets)
    return tuple(choice(BAR_STARTS_E048C9ED) for _ in range(nrows))


def generate_e048c9ed(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        grid_h, rows = _row_layout_e048c9ed(diff_lb, diff_ub)
        lengths = _pick_lengths_e048c9ed(size(rows), diff_lb, diff_ub)
        starts = _pick_starts_e048c9ed(size(rows))
        right_edges = tuple(add(add(start, length), NEG_ONE) for start, length in zip(starts, lengths))
        max_right = max(right_edges)
        marker_gap = choice((ONE, ONE, TWO, TWO, THREE, FOUR))
        marker_col = add(max_right, marker_gap)
        grid_w = add(add(marker_col, ONE), choice(TRAILING_PAD_E048C9ED))
        if grid_w > 30:
            continue

        gi = canvas(ZERO, (grid_h, grid_w))
        gi = fill(gi, FIVE, initset((ZERO, marker_col)))

        if choice((T, F)):
            colors = repeat(choice(interval(ONE, 10, ONE)), size(rows))
        else:
            colors = tuple(choice(interval(ONE, 10, ONE)) for _ in rows)

        go = gi
        for row, start, length, color_value in zip(rows, starts, lengths, colors):
            patch = connect((row, start), (row, add(add(start, length), NEG_ONE)))
            gi = fill(gi, color_value, patch)
            go = fill(fill(go, color_value, patch), _bar_digit_e048c9ed(lengths, length), initset((row, marker_col)))

        if gi == go:
            continue
        return {"input": gi, "output": go}
