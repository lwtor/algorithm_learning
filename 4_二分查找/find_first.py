#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def find_first(L, num):
    left = 0
    right = len(L) - 1
    while left <= right:
        mid = (left + right) // 2
        if L[mid] >= num:
            right = mid - 1
        else:
            left = mid + 1

    if left < len(L) and L[left] == num:
        return left
    return -1

# 容易理解的版本
def find_first_easy(L, num):
    low = 0
    high = len(L) - 1
    while low <= high:
        mid = (low + high) // 2
        if L[mid] > num:
            high = mid - 1
        elif L[mid] < num:
            low = mid + 1
        else:
            if mid == 0 or not a[mid - 1] == num:
                return mid
            high = mid - 1
    return -1

list1 = [1, 3, 4, 5, 6, 8, 8, 8, 11, 18]
list2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
test_list = list1
print(find_first(list1, 8))
print(find_first(list2, 2))
