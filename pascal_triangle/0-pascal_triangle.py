#!/usr/bin/python3
def pascal_triangle(n):
    # Check special case
    if n <= 0:
        return []
    
    # Initialize the Pascal's triangle with the first row
    triangle = [[1]]
    
    # Generate the remaining rows
    for i in range(1, n):
        # Create a new row with a leading 1
        row = [1]
        # Add the middle numbers calculated from the previous row
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        # Add a trailing 1 to the new row
        row.append(1)
        # Append the new row to the Pascal's triangle
        triangle.append(row)
    
    return triangle
