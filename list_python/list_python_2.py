def selectionSort(a):
    # 0 -> len(a) - 1
    for i in range(len(a)): 
        # min_index = i
        min_index = i

        for j in range(i + 1, len(a)):
            if a[min_index] >= a[j]:
                min_index = j
        
        tamp = a[min_index]
        a[min_index] = a[i]
        a[i] = tamp
    return a

print(selectionSort([12, 3, 5, 6, 19]))




