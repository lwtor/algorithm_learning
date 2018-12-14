from typing import List
import random

def quick_sort(a: List[int]):
    _quick_sort_between(a, 0, len(a)-1)

def _quick_sort_between(a: List[int], low: int, high: int):
    if low >= high: return
    print('list:', a[low:high+1])
    m = _partition(a, low, high)   # a[m] is in final position
    _quick_sort_between(a, low, m-1)
    _quick_sort_between(a, m+1, high)

def _partition(a: List[int], low: int, high: int):
    pivot, j = a[low], low
    for i in range(low+1, high+1):
        print(a[low:high], ' ,i :', i, ' ,j :', j)
        if a[i] <= pivot:
            j += 1
            a[j], a[i] = a[i], a[j]  # swap
            # print('change , i ->', i , 'j ->', j, ' -- ', a[low:high])
    a[low], a[j] = a[j], a[low]
    print('left:', a[low:j], ' ,pivot:', a[j], ' ,right:', a[j+1:high+1])
    print('pivot', j)
    return j

if __name__ == "__main__":
    a1 = [3, 5, 6, 7, 8]
    a2 = [2, 2, 2, 2]
    a3 = [4, 3, 2, 1]
    a4 = [5, -1, 9, 3, 7, 8, 3, -2, 9]
    a5 = [6, 5, 3, 1, 8, 7, 2, 4, 9]

    test_list = a5

    quick_sort(test_list)
    print(test_list)

    # quick_sort(a1)
    # print(a1)
    # quick_sort(a2)
    # print(a2)
    # quick_sort(a3)
    # print(a3)
    # quick_sort(a4)
    # print(a4)
