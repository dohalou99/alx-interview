def generate_pascals_triangle(n):
    """
    Generate Pascal's triangle up to the nth row.

    Args:
    - n: An integer representing the number of rows in Pascal's triangle.

    Returns:
    - A list of lists representing Pascal's triangle.
    """
    pascals_triangle = []

    if not isinstance(n, int) or n <= 0:
        return pascals_triangle

    for row in range(n):
        current_row = []
        for position in range(row + 1):
            if position == 0 or position == row:
                current_row.append(1)
            else:
                previous_row = pascals_triangle[row - 1]
                current_value = previous_row[position - 1] + previous_row[position]
                current_row.append(current_value)
        pascals_triangle.append(current_row)

    return pascals_triangle

# Example usage:
print(generate_pascals_triangle(5))
