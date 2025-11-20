# Complete Decision Tree for Matrix Column Processing Algorithm

## Overview
This document describes the complete decision-making process for transforming any n×n matrix to achieve columns with unique trailing zero counts through strategic column operations.

## Main Processing Pipeline Decision Tree

```
START: process()
│
├─ STEP 1: SORT BY TRAILING ZEROS
│  │
│  ├─ Count trailing zeros for each column
│  │  │
│  │  └─ For each column j (0 to n-1):
│  │     │
│  │     ├─ Initialize count = 0, first_nonzero_row = None
│  │     │
│  │     ├─ For each row i (n-1 down to 0):
│  │     │  │
│  │     │  ├─ Is matrix[i][j] == 0?
│  │     │  │  │
│  │     │  │  ├─ YES → count++, continue
│  │     │  │  │
│  │     │  │  └─ NO → first_nonzero_row = i, BREAK
│  │     │  │
│  │     │  └─ End row loop
│  │     │
│  │     └─ Return (count, first_nonzero_row)
│  │
│  ├─ Create column ordering by trailing zeros
│  │  │
│  │  ├─ Create pairs: (column_index, trailing_zero_count)
│  │  │
│  │  ├─ Sort by: -trailing_zeros (descending)
│  │  │
│  │  └─ Extract new_order = [sorted_column_indices]
│  │
│  ├─ Reorder matrix columns
│  │  │
│  │  └─ For each row: reordered_row = [row[i] for i in new_order]
│  │
│  └─ Result: Columns sorted by trailing zeros (most to least)
│
├─ STEP 2: MAKE COLUMNS HAVE UNIQUE TRAILING ZEROS
│  │
│  ├─ Initialize max_attempts = 5
│  │
│  ├─ Main differentiation loop
│  │  │
│  │  └─ For attempt (0 to max_attempts-1):
│  │     │
│  │     ├─ Get current trailing zero info
│  │     │  │
│  │     │  ├─ info = [(tz_count, first_nonzero_row) for each column]
│  │     │  │
│  │     │  └─ counts = [tz_count for tz_count, _ in info]
│  │     │
│  │     ├─ Check if all unique
│  │     │  │
│  │     │  ├─ Is len(set(counts)) == len(counts)?
│  │     │  │  │
│  │     │  │  ├─ YES → SUCCESS, return True
│  │     │  │  │
│  │     │  │  └─ NO → Continue differentiation
│  │     │  │
│  │     │  └─ Group columns by trailing zero count
│  │     │     │
│  │     │     └─ groups[tz_count] = [(col_index, first_nonzero_row), ...]
│  │     │
│  │     ├─ Try strategic differentiation
│  │     │  │
│  │     │  └─ For each group with ≥2 columns:
│  │     │     │
│  │     │     ├─ Skip if all-zero columns (tz_count == n)
│  │     │     │
│  │     │     └─ Call _differentiate_columns_strategically(cols)
│  │     │        │
│  │     │        ├─ SUCCESS? → changed = True, BREAK
│  │     │        │
│  │     │        └─ FAILED? → Continue to next group
│  │     │
│  │     ├─ Check progress
│  │     │  │
│  │     │  ├─ Is changed == False?
│  │     │  │  │
│  │     │  │  ├─ YES → BREAK attempt loop
│  │     │  │  │
│  │     │  │  └─ NO → Continue to next attempt
│  │     │  │
│  │     │  └─ Continue attempt loop
│  │     │
│  │     └─ End attempt loop
│  │
│  └─ Strategic Column Differentiation (_differentiate_columns_strategically)
│     │
│     ├─ For each pair (col_i, col_j) in group:
│     │  │
│     │  ├─ Get column info
│     │  │  │
│     │  │  ├─ col1, row1 = cols[i]
│     │  │  ├─ col2, row2 = cols[j]
│     │  │  │
│     │  │  └─ Skip if either row is None (all-zero column)
│     │  │
│     │  ├─ Get first non-zero values
│     │  │  │
│     │  │  ├─ val1 = matrix[row1][col1]
│     │  │  │
│     │  │  └─ val2 = matrix[row2][col2]
│     │  │
│     │  ├─ STRATEGY 1: Direct elimination at first non-zero row
│     │  │  │
│     │  │  ├─ Is val1 % val2 == 0?
│     │  │  │  │
│     │  │  │  ├─ YES → multiplier = -(val1 // val2)
│     │  │  │  │  │
│     │  │  │  │  ├─ add_columns(col1, col2, multiplier)
│     │  │  │  │  │
│     │  │  │  │  ├─ Print operation details
│     │  │  │  │  │
│     │  │  │  │  └─ Return True (success)
│     │  │  │  │
│     │  │  │  └─ NO → Try Strategy 2
│     │  │  │
│     │  │  └─ STRATEGY 2: Reverse elimination
│     │  │     │
│     │  │     ├─ Is val2 % val1 == 0?
│     │  │     │  │
│     │  │     │  ├─ YES → multiplier = -(val2 // val1)
│     │  │     │  │  │
│     │  │     │  │  ├─ add_columns(col2, col1, multiplier)
│     │  │     │  │  │
│     │  │     │  │  ├─ Print operation details
│     │  │     │  │  │
│     │  │     │  │  └─ Return True (success)
│     │  │     │  │
│     │  │     │  └─ NO → Try Strategy 3
│     │  │     │
│     │  │     └─ STRATEGY 3: Different row targeting
│     │  │        │
│     │  │        ├─ Is row1 ≠ row2?
│     │  │        │  │
│     │  │        │  ├─ YES → target_row = min(row1, row2)
│     │  │        │  │  │
│     │  │        │  │  ├─ val1_target = matrix[target_row][col1]
│     │  │        │  │  ├─ val2_target = matrix[target_row][col2]
│     │  │        │  │  │
│     │  │        │  │  ├─ Are both values non-zero?
│     │  │        │  │  │  │
│     │  │        │  │  │  ├─ YES → Try divisibility operations
│     │  │        │  │  │  │  │
│     │  │        │  │  │  │  ├─ val1_target % val2_target == 0?
│     │  │        │  │  │  │  │  │
│     │  │        │  │  │  │  │  ├─ YES → Create zero in col1
│     │  │        │  │  │  │  │  │  │
│     │  │        │  │  │  │  │  │  ├─ multiplier = -(val1_target // val2_target)
│     │  │        │  │  │  │  │  │  │
│     │  │        │  │  │  │  │  │  ├─ add_columns(col1, col2, multiplier)
│     │  │        │  │  │  │  │  │  │
│     │  │        │  │  │  │  │  │  └─ Return True
│     │  │        │  │  │  │  │  │
│     │  │        │  │  │  │  │  └─ val2_target % val1_target == 0?
│     │  │        │  │  │  │  │     │
│     │  │        │  │  │  │  │     ├─ YES → Create zero in col2
│     │  │        │  │  │  │  │     │  │
│     │  │        │  │  │  │  │     │  ├─ multiplier = -(val2_target // val1_target)
│     │  │        │  │  │  │  │     │  │
│     │  │        │  │  │  │  │     │  ├─ add_columns(col2, col1, multiplier)
│     │  │        │  │  │  │  │     │  │
│     │  │        │  │  │  │  │     │  └─ Return True
│     │  │        │  │  │  │  │     │
│     │  │        │  │  │  │  │     └─ NO → Continue to next pair
│     │  │        │  │  │  │  │
│     │  │        │  │  │  │  └─ End divisibility check
│     │  │        │  │  │  │
│     │  │        │  │  │  └─ NO → Continue to next pair
│     │  │        │  │  │
│     │  │        │  │  └─ End target row processing
│     │  │        │  │
│     │  │        │  └─ NO → Continue to next pair
│     │  │        │
│     │  │        └─ End Strategy 3
│     │  │
│     │  └─ Continue to next column pair
│     │
│     └─ Return False (no successful differentiation found)
│
├─ STEP 3: FINAL SORT BY TRAILING ZEROS
│  │
│  ├─ Count trailing zeros for all columns (after differentiation)
│  │
│  ├─ Create column-trailing_zero pairs
│  │
│  ├─ Sort by -trailing_zeros (descending)
│  │
│  ├─ Reorder matrix columns according to final sort
│  │
│  └─ Return processed matrix
│
└─ END: Return final matrix
```

## Key Decision Points Summary

### 1. Trailing Zero Counting Decision
```
For each column from bottom to top:
├─ Element == 0? → count++, continue
└─ Element ≠ 0? → record row position, stop counting
```

### 2. Column Sorting Decision
```
Current trailing zero counts: [a, b, c, d, ...]
└─ Sort columns by descending trailing zero count
```

### 3. Strategic Differentiation Decision
```
Two columns with same trailing zeros:
├─ Get first non-zero elements: val1, val2
├─ Strategy 1: val1 % val2 == 0?
│  ├─ YES → Eliminate val1 using col2
│  └─ NO → Try Strategy 2
├─ Strategy 2: val2 % val1 == 0?
│  ├─ YES → Eliminate val2 using col1
│  └─ NO → Try Strategy 3
└─ Strategy 3: Different first non-zero rows?
   ├─ YES → Try elimination at earlier row
   └─ NO → Move to next column pair
```

### 4. Success Evaluation Decision
```
After each operation:
├─ Did any trailing zero count change?
│  ├─ YES → Continue with next attempt
│  └─ NO → Stop attempts
└─ All columns have unique counts? → Complete success
```

## Column Operations Used

### Column Swap
```
swap_columns(col1, col2):
└─ For each row: swap matrix[row][col1] ↔ matrix[row][col2]
```

### Column Addition
```
add_columns(target_col, source_col, multiplier):
└─ For each row: matrix[row][target_col] += multiplier * matrix[row][source_col]
```

## Algorithm Characteristics

- **Approach**: Strategic elimination based on divisibility
- **Target**: Create unique trailing zero counts per column
- **Operations**: Column addition with calculated multipliers
- **Termination**: Maximum 5 attempts or success
- **Complexity**: O(n³) worst case for n×n matrix
- **Space**: O(n²) for matrix + O(n) for tracking

## Example Decision Flow

```
Input Matrix:
[2, 4, 6, 1]
[1, 2, 3, 2]  
[0, 0, 0, 3]
[0, 0, 0, 0]

Step 1: Count trailing zeros → [2, 2, 2, 1]
Step 2: Group by count → {2: [col0, col1, col2], 1: [col3]}
Step 3: Differentiate group with count=2:
   - col0 vs col1: val1=1, val2=2 → 2%1==0 → eliminate val2
   - col0 vs col2: val1=1, val3=3 → 3%1==0 → eliminate val3
Step 4: Result → [4, 4, 2, 1] trailing zeros
```