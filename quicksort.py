def quick_sort(s):
    length = len(s)
    if length<=1:
        return s
    else:
        pivot = s.pop()

    items_greater = []
    items_lower = []

    for item in s:
        if item > pivot:
            items_greater.append(item)

        else:
            items_lower.append(item)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

print(quick_sort([8,4,2,5,9,3,1,0,6,7,10]))

