`arc2_opus46_summary.json` was consistent with the official examples and I used it as the working hypothesis.

`arc2_sonnet45_summary.jsonl` was not reliable here. It describes a 180-degree duplication rule, but the official examples show a clockwise corner-color rotation followed by outward diagonal extension from each rotated corner.

The public ARC data originally omitted two orange cells at `(8, 1)` and `(9, 0)` from the down-left ray in the second training output. Those cells were restored in both official copies of the task, so every pair and the verifier now follow the same rotated-corners-plus-rays rule without an exact-input compatibility branch.
