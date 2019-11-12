m1 = [[1, 3], [2, 4], [7, 8]]
m2 = [[5, 2], [1, 0], [9, 2]]

m3 = []

for i in range(len(m1)):
    l1 = m1[i]
    l2 = m2[i]
    result = []
    for j in range(len(l1)):
        result.append(l1[j] + l2[j])
    m3.append(result)

print(m3)