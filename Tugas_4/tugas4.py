nested_list_1 = [
    [1,2,3,4,5],
    [2,1,3,5,4],
    [2,1,3,5,4],
    [3,2,1,4,5],
    [3,2,1,4,5],
]
nested_list_2 = [
    [1,2,3,4,5],
    [2,1,3,5,4],
    [2,1,3,5,4],
    [3,2,1,4,5],
    [3,2,1,4,5],
]
nested_list_3 = []

for r in range(5):
    row = []
    for s in range(5):
        sum_nested = 0
        for t in range(5):
            sum_nested += nested_list_1[r][t] * nested_list_2[t][s]
        row.append(sum_nested)
    nested_list_3.append(row)

print("Hasil Perkalian Matriks 5x5: ")
for row in nested_list_3:
    print(",".join(map(str, row)))