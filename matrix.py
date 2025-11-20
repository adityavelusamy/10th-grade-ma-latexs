import copy
from collections import defaultdict

class MatrixProcessor:
    def __init__(self, matrix):
        if not matrix or not matrix[0]:
            raise ValueError("Matrix cannot be empty")

        self.matrix = copy.deepcopy(matrix)
        self.rows = len(matrix)
        self.cols = len(matrix[0])

        for row in matrix:
            if len(row) != self.cols:
                raise ValueError("All rows must have the same number of columns")

    def swap_columns(self, col1, col2):
        for row in self.matrix:
            row[col1], row[col2] = row[col2], row[col1]

    def add_columns(self, target_col, source_col, multiplier=1):
        for i in range(self.rows):
            self.matrix[i][target_col] += multiplier * self.matrix[i][source_col]

    def count_trailing_zeros(self, col_index):
        count = 0
        first_nonzero_row = None
        for i in range(self.rows - 1, -1, -1):
            if self.matrix[i][col_index] == 0:
                count += 1
            else:
                first_nonzero_row = i
                break
        return count, first_nonzero_row

    def get_trailing_zero_info(self):
        return [self.count_trailing_zeros(col) for col in range(self.cols)]

    def sort_by_trailing_zeros(self):
        info = self.get_trailing_zero_info()
        col_pairs = [(col, info[col][0]) for col in range(self.cols)]
        col_pairs.sort(key=lambda x: -x[1])  # Sort by trailing zeros descending

        new_order = [col for col, _ in col_pairs]
        for row in self.matrix:
            reordered = [row[i] for i in new_order]
            row[:] = reordered

    def make_unique_trailing_zeros(self, max_attempts=5):
        for attempt in range(max_attempts):
            info = self.get_trailing_zero_info()
            counts = [tz_count for tz_count, _ in info]

            if len(set(counts)) == len(counts):
                return True

            # Group columns by trailing zero count
            groups = defaultdict(list)
            for col, (tz_count, first_nonzero_row) in enumerate(info):
                groups[tz_count].append((col, first_nonzero_row))

            # Try to differentiate columns with same count
            changed = False
            for tz_count, cols in groups.items():
                if len(cols) < 2 or tz_count == self.rows:
                    continue

                # Compare first non-zero elements and try to create more trailing zeros
                if self._differentiate_columns_strategically(cols):
                    changed = True
                    break

            if not changed:
                break

        final_info = self.get_trailing_zero_info()
        final_counts = [tz_count for tz_count, _ in final_info]
        return len(set(final_counts)) == len(final_counts)

    def _differentiate_columns_strategically(self, cols):
        """
        Strategically differentiate columns with same trailing zeros by looking at
        the first non-zero element from the bottom and trying to increase trailing zeros
        """
        for i in range(len(cols)):
            for j in range(i + 1, len(cols)):
                col1, row1 = cols[i]
                col2, row2 = cols[j]

                # Skip if either column is all zeros
                if row1 is None or row2 is None:
                    continue

                val1 = self.matrix[row1][col1]
                val2 = self.matrix[row2][col2]

                # Try to eliminate the first non-zero element in one column
                # to increase its trailing zeros
                if val1 != 0 and val2 != 0:
                    # Strategy 1: Try to make val1 zero by using col2
                    if val2 != 0 and val1 % val2 == 0:
                        multiplier = -(val1 // val2)
                        print(f"Attempting to increase trailing zeros in col {col1} by adding {multiplier} * col {col2}")
                        self.add_columns(col1, col2, multiplier)
                        return True

                    # Strategy 2: Try to make val2 zero by using col1
                    elif val1 != 0 and val2 % val1 == 0:
                        multiplier = -(val2 // val1)
                        print(f"Attempting to increase trailing zeros in col {col2} by adding {multiplier} * col {col1}")
                        self.add_columns(col2, col1, multiplier)
                        return True

                    # Strategy 3: Try with different row if first non-zero rows are different
                    elif row1 != row2:
                        # Look for a row where we can create a zero
                        target_row = min(row1, row2)
                        val1_target = self.matrix[target_row][col1]
                        val2_target = self.matrix[target_row][col2]

                        if val1_target != 0 and val2_target != 0:
                            if val2_target != 0 and val1_target % val2_target == 0:
                                multiplier = -(val1_target // val2_target)
                                print(f"Creating zero at row {target_row} in col {col1} by adding {multiplier} * col {col2}")
                                self.add_columns(col1, col2, multiplier)
                                return True
                            elif val1_target != 0 and val2_target % val1_target == 0:
                                multiplier = -(val2_target // val1_target)
                                print(f"Creating zero at row {target_row} in col {col2} by adding {multiplier} * col {col1}")
                                self.add_columns(col2, col1, multiplier)
                                return True

        return False

    def process(self):
        self.sort_by_trailing_zeros()
        self.make_unique_trailing_zeros()
        self.sort_by_trailing_zeros()  # Final sort
        return self.matrix

    def print_matrix(self):
        for row in self.matrix:
            print(row)

    def get_matrix(self):
        return copy.deepcopy(self.matrix)

def process_matrix(matrix):
    processor = MatrixProcessor(matrix)
    return processor.process()

def demo():
    matrix = [
        [8, 3, 6, 9],
        [1, 4, 3, 2],
        [0, 0, 0, 3],
        [3, -3, 3, 3],
        [2, 1, 0.5, 0],
    ]

    print("Original matrix:")
    processor = MatrixProcessor(matrix)
    processor.print_matrix()

    info = processor.get_trailing_zero_info()
    counts = [tz_count for tz_count, _ in info]
    print(f"Trailing zeros: {counts}")

    result = processor.process()

    print("\nProcessed matrix:")
    processor.print_matrix()
    final_info = processor.get_trailing_zero_info()
    final_counts = [tz_count for tz_count, _ in final_info]
    print(f"Final trailing zeros: {final_counts}")

    return result

if __name__ == "__main__":
    demo()
