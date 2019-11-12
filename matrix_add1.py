m1 = [
    [1, 3, 5],
    [2, 4, 6]
]

m2 = [
    [5, 2, 7],
    [1, 0, 8]
]

result = [
    # [m1[0][0] + m2[0][0], m1[0][1] + m2[0][1]],
    # [m1[1][0] + m2[1][0], m1[1][1] + m2[1][1]]
    # [0, 0],
    # [0, 0]
]

for row_number in range(len(m1)):
    row = m1[row_number]
    result_row = []
    for column_number in range(len(row)):
        print(f"{row_number} {column_number}")
        print(f"I want to add {m1[row_number][column_number]} to {m2[row_number][column_number]}")
        # result[row_number][column_number] = m1[row_number][column_number] + m2[row_number][column_number]
        result_row.append(m1[row_number][column_number] + m2[row_number][column_number])
    result.append(result_row)
print(result)
