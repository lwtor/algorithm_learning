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
    if right < len(L) and L[right] ==num:
        return right
    return -1

list1 = [1, 3, 4, 5, 6, 8, 8, 8, 11, 18]
list2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
test_list = list1
print(find_last(list1, 1))
print(find_last(list2, 1))
