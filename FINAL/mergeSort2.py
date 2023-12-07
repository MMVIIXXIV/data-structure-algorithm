def mergeSort(lt):
    if len(lt) <= 1:
        return lt

    middle = len(lt)//2
    left = lt[:middle]
    right = lt[middle:]

    mergeSort(left)
    mergeSort(right)

    mergeTwoSortList(left, right, lt)

def mergeTwoSortList(a, b, lt):
    lenA = len(a)
    lenB = len(b)

    i = j = k = 0

    while i < lenA and j < lenB:
        if a[i] <= b[j]:
            lt[k] = a[i]
            i += 1
        else:
            lt[k] = b[j]
            j += 1
        k += 1

    while i < lenA:
        lt[k] = a[i]
        i += 1
        k += 1

    while j < lenB:
        lt[k] = b[j]
        j += 1
        k += 1

lt = [10, 3, 15, 7, 8, 23, 98, 29]

mergeSort(lt)
print(lt)