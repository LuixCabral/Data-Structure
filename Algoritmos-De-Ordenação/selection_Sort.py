arr = [64, 34, 25, 5, 22, 11, 90, 12]

n = len(arr)

for i in range(n):
    index_Minimo= 1
    for j in range(i+1,n):
        if arr[j] < arr[index_Minimo]:
            index_Minimo = j
    arr[i], arr[index_Minimo] = arr[index_Minimo], arr[i]

print("array organizada", arr)

        
