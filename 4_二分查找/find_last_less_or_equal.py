#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def find_last(L, num):
    left = 0
    right = len(L) - 1
    while left <= right:
        mid = (left + right) // 2
        if L[mid] <= num:
            left = mid + 1
        else:
            right = mid - 1
    pos = left - 1
    if pos > 0 and L[pos] <= num:
        return pos
    return -1
def test(L, num):
    pos = find_last(L, num)
    print(L, ' -- [', pos, '] =', L[pos])

list1 = [1, 3, 4, 5, 6, 8, 8, 8, 11, 18]
list2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
list3 = [3, 4, 6, 7, 10]
test_list = list1
test(list1, 8)
test(list2, 2)
test(list3, 5)
