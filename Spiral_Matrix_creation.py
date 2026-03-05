# function to generate spiral matrix of size n*n

def spiral_matrix(n, matrix=None):
    if matrix is None:
        matrix = [[0] * n for _ in range(n)]
    num = 1
    top, bottom, left, right = 0, n-1, 0, n-1
    
    while num <= n*n:
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1
        
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1
        
        for i in range(right, left - 1, -1):
            matrix[bottom][i] = num
            num += 1
        bottom -= 1
        
        for i in range(bottom, top - 1, -1):
            matrix[i][left] = num
            num += 1
        left += 1
    
    return matrix

# Test
if __name__ == "__main__":
    n = 4
    result = spiral_matrix(n)
    print("Spiral Matrix:", result)



