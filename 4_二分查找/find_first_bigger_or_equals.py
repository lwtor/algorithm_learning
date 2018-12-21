#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def find_first(L, num):
    left = 0
    right = len(L) - 1
    while left <= right:
        print(left, right)
        mid = (left + right) // 2
        if L[mid] >= num:
            right = mid - 1
        else:
            left = mid + 1
    print(right)
    right += 1
    if right < len(L) and L[right] >= num:
        return right
    return -1

def test(L, num):
    pos = find_first(L, num)
    print(L, ' -- [', pos, '] =', L[pos])

list1 = [1, 3, 4, 5, 6, 8, 8, 8, 11, 18]
list2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
list3 = [3, 4, 6, 7, 10]
test_list = list1
test(list1, 8)
test(list2, 2)
test(list3, 5)
