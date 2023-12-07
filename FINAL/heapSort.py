def heapify(lt, heapLen, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < heapLen and lt[largest] < lt[left]:
        largest = left

    if right < heapLen and lt[largest] < lt[right]:
        largest = right

    if largest != i:
        lt[i], lt[largest] = lt[largest], lt[i]

        heapify(lt, heapLen, largest)

def heapSort(lt):
    length = len(lt)

    for i in range(length // 2 - 1, -1, -1):
        #print(length // 2 - 1, i)
        heapify(lt, length, i)

    for i in range(length-1, 0, -1):
        lt[i], lt[0] = lt[0], lt[i]
        heapify(lt, i, 0)

lt = [5,4,3,2,1,8,9]
heapSort(lt)
print(lt)