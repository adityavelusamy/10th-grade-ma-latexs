# Matrix Processor Usage Guide

This Python script processes any n×n matrix to create columns with different numbers of trailing zeros through strategic column operations.

## Features

- **Universal compatibility**: Works with any square matrix (n×n)
- **Column echelon form**: Arranges columns based on leading entry positions
- **Trailing zero optimization**: Creates unique trailing zero counts for each column
- **Automatic reorganization**: Orders columns by trailing zero count (most to least)

## Quick Start

### Basic Usage

```python
from matrix import process_matrix

# Define your matrix as a list of lists
matrix = [
    [1, 2, 3],
    [0, 4, 5], 
    [0, 0, 6]
]

# Process the matrix
result = process_matrix(matrix)
```

### Class-based Usage (More Control)

```python
from matrix import MatrixProcessor

# Create processor instance
processor = MatrixProcessor(matrix)

# Process step by step
processor.arrange_column_echelon_form()
processor.make_columns_unique_trailing_zeros()
processor.reorganize_columns()

# Get final result
final_matrix = processor.get_matrix()
```

## Interactive Functions

### User Input Demo
```python
from matrix import demo_with_user_matrix

# Interactive matrix input
demo_with_user_matrix()
```

### Random Matrix Testing
```python
from matrix import process_random_matrix

# Generate and process random 4x4 matrix
result = process_random_matrix(4)
```

## Example Outputs

### 3×3 Matrix Example
**Input:**
```
[1, 2, 3]
[0, 4, 5]
[0, 0, 6]
```

**Output:**
```
[1, 2, 3]
[0, 4, 5]
[0, 0, 6]

Trailing zero counts: [2, 1, 0]
✓ Success: All columns have different numbers of trailing zeros
```

### 5×5 Matrix Example
**Input:**
```
[0, 0, 1, 2, 3]
[0, 2, 4, 1, 2]
[0, 0, 0, 0, 7]
[0, 0, 0, 1, 1]
[3, 2, 4, 3, 5]
```

**Output:**
```
[1, 0, 1, 2, 0]
[0, 6, 5, 1, -2]
[0, 0, 7, 0, 0]
[0, 0, 0, 1, 0]
[0, 0, 0, 0, 1]

Trailing zero counts: [4, 3, 2, 1, 0]
✓ Success: All columns have different numbers of trailing zeros
```

## How It Works

### Step 1: Column Echelon Form
- Finds leading entry positions in each row
- Swaps columns to arrange them in ascending order of leading positions

### Step 2: Trailing Zero Differentiation
- Groups columns by number of trailing zeros
- Applies strategic column operations to create different trailing zero counts
- Uses multiple strategies:
  - Creating zeros at earlier rows through linear combinations
  - GCD-based approaches for optimal reductions
  - Alternative methods for stubborn cases

### Step 3: Final Reorganization
- Orders columns by trailing zero count (descending)
- Ensures optimal column arrangement

## Matrix Validation

The processor validates input matrices:
- Must be non-empty
- All rows must have same number of columns
- All elements must be numbers (int or float)

```python
from matrix import validate_matrix

try:
    validate_matrix(your_matrix)
    print("Matrix is valid!")
except ValueError as e:
    print(f"Invalid matrix: {e}")
```

## Advanced Features

### Custom Processing Pipeline
```python
processor = MatrixProcessor(matrix)

# Access individual methods
leading_positions = processor.find_leading_entries()
trailing_info = processor.count_trailing_zeros_all_columns()
groups = processor.group_columns_by_trailing_zeros()

# Custom operations
processor.col_swap(0, 1)
processor.add_columns(0, 1, multiplier=2)
```

### Error Handling
The processor includes robust error handling:
- Invalid matrix dimensions
- Non-numeric elements
- Empty matrices
- Infinite loop prevention in optimization algorithms

## Performance Notes

- **Time Complexity**: O(n³) for n×n matrices in worst case
- **Space Complexity**: O(n²) for matrix storage
- **Optimization**: Automatic loop detection prevents infinite processing
- **Attempts**: Limited to 10-20 iterations for practical processing time

## Limitations

1. **Non-square matrices**: Currently supports only n×n matrices
2. **Very large matrices**: Performance may degrade for matrices larger than 20×20
3. **Stubborn cases**: Some matrices may not achieve completely unique trailing zero counts
4. **Integer overflow**: Very large numbers may cause computational issues

## Tips for Best Results

1. **Matrix size**: Works best with matrices 2×2 to 10×10
2. **Element range**: Keep matrix elements in reasonable range (-100 to 100)
3. **Sparse matrices**: Matrices with many zeros often produce better results
4. **Non-singular**: Non-singular matrices typically process more successfully

## Troubleshooting

### Common Issues

**Issue**: "Some columns have duplicate trailing zero counts"
**Solution**: The algorithm tried multiple strategies but couldn't completely differentiate all columns. The result is still valid but not optimal.

**Issue**: Matrix becomes very large numbers
**Solution**: Use smaller initial values or apply the algorithm iteratively with intermediate simplification.

**Issue**: Processing takes too long
**Solution**: Reduce matrix size or increase the max_attempts parameter limit.

## File Structure

- `matrix.py`: Main implementation file
- `MatrixProcessor`: Core class with all functionality
- Helper functions: `process_matrix()`, `demo_with_user_matrix()`, etc.

Run the file directly to see examples with different matrix sizes:
```bash
python matrix.py
```