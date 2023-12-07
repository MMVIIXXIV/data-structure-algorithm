def mergeSort(lt):
    if len(lt) <= 1:
        return lt

    middle = len(lt)//2
    left = lt[:middle]
    right = lt[middle:]

    left = mergeSort(left)
    right = mergeSort(right)

    return mergeTwoSortList(left, right)

def mergeTwoSortList(a, b):
    sorted_list = []

    lenA = len(a)
    lenB = len(b)

    i = j = 0

    while i < lenA and j < lenB:
        if a[i] <= b[j]:
            sorted_list.append(a[i])
            i += 1
        else:
            sorted_list.append(b[j])
            j += 1

    while i < lenA:
        sorted_list.append(a[i])
        i += 1

    while j < lenB:
        sorted_list.append(b[j])
        j += 1

    return sorted_list

lt = [10, 3, 15, 7, 8, 23, 98, 29]

print(mergeSort(lt))