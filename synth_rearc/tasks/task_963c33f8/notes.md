The stable rule is column-based:

- The top 3x3 marker block has two full `9` rows.
- Treat its three columns as independent vertical rods.
- A `9,9,1` rod falls straight down in the same column until its `1` tip is immediately above the first `5`; without a `5` below it, the rod reaches the bottom.
- A `9,9,9` rod reaches the bottom in the same column.

The original official data had two isolated annotation errors: train pair 1 deleted two cells from a bottom `5` bar, and train pair 2 shifted its all-`9` rod one column right. The corrected outputs now follow the same rule as train pair 0 and the test pair. The verifier and generator therefore use only the uniform same-column rule.
