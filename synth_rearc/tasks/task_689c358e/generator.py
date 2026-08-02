from synth_rearc.core import *


COLORS = (TWO, FIVE, EIGHT, NINE)
SHAPES = (
    ("h", frozenset({(0, 1), (1, 0), (1, 1), (1, 2), (1, 3), (2, 1)}), ONE, ONE, THREE, FOUR, RIGHT),
    ("h", frozenset({(0, 2), (1, 0), (1, 1), (1, 2), (1, 3), (2, 2)}), ONE, TWO, THREE, FOUR, LEFT),
    ("v", frozenset({(0, 1), (1, 0), (1, 1), (1, 2), (2, 1), (3, 1)}), ONE, ONE, FOUR, THREE, DOWN),
    ("v", frozenset({(0, 1), (1, 1), (2, 0), (2, 1), (2, 2), (3, 1)}), TWO, ONE, FOUR, THREE, UP),
)


def _blank_grid() -> Grid:
    x0 = canvas(SEVEN, (11, 11))
    x1 = asindices(x0)
    x2 = box(x1)
    x3 = fill(x0, SIX, x2)
    return x3


def _placement_candidates(
    shape: tuple[str, Indices, int, int, int, int, IntegerTuple],
    occupied: Indices,
    used_rows: set[int],
    used_cols: set[int],
) -> list[tuple[Indices, int, int]]:
    kind, patch, row_offset, col_offset, height, width, long_direction = shape
    cands = []
    for i in range(1, 11 - height):
        for j in range(1, 11 - width):
            main_row = i + row_offset
            main_col = j + col_offset
            if kind == "h":
                if main_row in used_rows or main_col == FIVE:
                    continue
                if main_col < FIVE and long_direction != RIGHT:
                    continue
                if main_col > FIVE and long_direction != LEFT:
                    continue
            else:
                if main_col in used_cols or main_row == FIVE:
                    continue
                if main_row < FIVE and long_direction != DOWN:
                    continue
                if main_row > FIVE and long_direction != UP:
                    continue
            placed = shift(patch, (i, j))
            if len(intersection(placed, occupied)) != ZERO:
                continue
            cands.append((placed, main_row, main_col))
    return cands


def generate_689c358e(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        gi = _blank_grid()
        occupied = frozenset({})
        used_rows: set[int] = set()
        used_cols: set[int] = set()
        placements = []
        failed = False
        for color in sample(COLORS, FOUR):
            shape = choice(SHAPES)
            cands = _placement_candidates(shape, occupied, used_rows, used_cols)
            if len(cands) == ZERO:
                failed = True
                break
            placed, main_row, main_col = choice(cands)
            kind = shape[0]
            long_direction = shape[6]
            gi = fill(gi, color, placed)
            occupied = combine(occupied, placed)
            placements.append((color, kind, main_row, main_col, long_direction))
            if kind == "h":
                used_rows.add(main_row)
            else:
                used_cols.add(main_col)
        if failed:
            continue
        kinds = {kind for _, kind, _, _, _ in placements}
        if len(kinds) != TWO:
            continue
        go = gi
        for color, kind, main_row, main_col, long_direction in placements:
            if kind == "h":
                marked = (main_row, ZERO) if long_direction == RIGHT else (main_row, TEN)
                erased = (main_row, TEN) if long_direction == RIGHT else (main_row, ZERO)
            else:
                marked = (ZERO, main_col) if long_direction == DOWN else (TEN, main_col)
                erased = (TEN, main_col) if long_direction == DOWN else (ZERO, main_col)
            go = fill(go, color, initset(marked))
            go = fill(go, ZERO, initset(erased))
        return {"input": gi, "output": go}
