#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 使用递归的方式
def binary_search(L, num):
    return binary_search_inner(L, 0, len(L), num)

def binary_search_inner(L, start, end, num):
    if start > end:
        return -1
    mid = (start + end) // 2
    print(start, end, mid)
    if L[mid] == num:
        return mid
    elif L[mid] > num:
        return binary_search_inner(L, start, mid-1, num)
    return binary_search_inner(L, mid+1, end, num)

# 使用循环
def binary_search_v2(L, num):
    left = 0
    right = len(L)
    while left < right:
        mid = (left + right) // 2
        print(left, right, mid, L[mid])
        if L[mid] == num:
            return mid
        elif L[mid] > num:
            right = mid - 1
        else:
            left = mid + 1
    return -1

test_list = [i*i for i in range(50)]
#print(test_list)
pos = binary_search_v2(test_list, 49)

print(pos)
