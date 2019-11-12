
list1 = [2, 4, 5]
list2 = [2, 3, 6]

list3 = []
for i in range(len(list1)):
    product = list1[i] * list2[i]
    list3.append(product)

print(list3)