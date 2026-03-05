# Ascendeum---1st-Round
1st Coding Round

# Spiral Matrix Generator

A simple Python script that generates an `n x n` spiral matrix filled with consecutive numbers starting at 1 and winding inward.

## File

- `Spiral_Matrix_creation.py` – contains the implementation and a basic test harness.

## Functionality

### `spiral_matrix(n, matrix=None)`

- **Parameters**:
  - `n` *(int)*: The size of the square matrix.
  - `matrix` *(list of lists, optional)*: An existing matrix to populate. If not provided, a new zeroed `n x n` matrix is created.
- **Returns**: The resulting spiral matrix as a list of lists.

The function iterates layer by layer (top row, right column, bottom row, left column), filling numbers from 1 through `n*n`.

## Usage

```python
from Spiral_Matrix_creation import spiral_matrix

n = 4
result = spiral_matrix(n)
print("Spiral Matrix:", result)
```

or run the script directly:

```bash
python Spiral_Matrix_creation.py
```

## Example Output

For `n = 4`:

```
Spiral Matrix: [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
```
