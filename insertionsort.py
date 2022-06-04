def insertion_sort(list_a):
    indexing_length = range(1, len(list_a))
    for i in indexing_length:
        x = list_a[i]

        while list_a[i-1]> x and i>0:
            list_a[i], list_a[i-1] = list_a[i-1], list_a[i]
            i = i -1


    return list_a


print(insertion_sort([7,8,9,5,6,4,3,1,2]))

