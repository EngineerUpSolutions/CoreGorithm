# Example: Generating an n x n Multiplication Table (Matrix)


def multiplication_table(n):
    table = []
    for i in range(1, n + 1):
        row = []
        for j in range(1, n + 1):
            row.append(i * j)
        table.append(row)
    return table

# Test
n = 4
result = multiplication_table(n)
for row in result:
    print(row)


    # Why is this O(n²) space?

    # You are creating a 2D list (table) with n rows and n columns.

    # Every single cell in that matrix is stored in memory.

    # So total space = n × n = O(n²)
