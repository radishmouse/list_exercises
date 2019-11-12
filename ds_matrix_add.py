matrix1 = [[1, 3, 5], [2, 4, 6]]
matrix2 = [[5, 2, 4], [1, 0, 4]]
matrix1_lst = []
matrix2_lst = []
new_lst = []
for lst in matrix1:
   for num in lst:
       matrix1_lst.append(num)
for lst in matrix2:
   for num in lst:
       matrix2_lst.append(num)
matrix1_len = len(matrix1_lst)
for num in range(matrix1_len):
   product = matrix1_lst[num] + matrix2_lst[num]
   new_lst.append(product)
result_matrix_row1 = new_lst[:len(new_lst)//2]
result_matrix_row2 = new_lst[len(new_lst)//2:]
print(result_matrix_row1)
print(result_matrix_row2)