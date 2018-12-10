from typing import List

def merge_sort(a: List[int]):
    _merge_sort_between(a, 0, len(a)-1)

def _merge_sort_between(a: List[int], low: int, high: int):
    # The indices are inclusive for both low and high.
    if low >= high: return
    mid = low + (high - low)//2
    print('left :', a[low:mid])
    print('right:', a[mid:high])
    print('-------------------------')
    _merge_sort_between(a, low, mid)
    _merge_sort_between(a, mid+1, high)

    _merge(a, low, mid, high)

def _merge(a: List[int], low: int, mid: int, high: int):
    # a[low:mid], a[mid+1, high] are sorted.
    i, j = low, mid+1
    tmp = []
    print('merge index -- ', 'low:', low, 'high:', high)
    print('merge -- ', 'left:', a[low:mid+1], ', right:',a[mid+1:high+1])
    while i <= mid and j <= high:
        if a[i] <= a[j]:
            tmp.append(a[i])
            i += 1
        else:
            tmp.append(a[j])
            j += 1
    start = i if i <= mid else j
    end = mid if i <= mid else high
    tmp.extend(a[start:end+1])
    a[low:high+1] = tmp
    print('after merge:', a[low:high+1])
    print('----------------------------')

test_list_1 = [6, 5, 3, 1, 8, 7, 2, 4, 9]
test_list_2 = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
merge_sort(test_list_2)
print(test_list_2)
