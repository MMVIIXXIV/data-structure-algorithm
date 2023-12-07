import re


def mergeTwoSortedArray(a, b):
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

a = [3,6,18,20]
b = [2,5,8,13,34]

print(mergeTwoSortedArray(a, b))