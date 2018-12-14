#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 快排，不考虑内存使用情况
def quick_sort(L):
    quick_sort_c(L, 0, len(L))

def quick_sort_c(L, start, end):
    if start >= end -1 :
        return
    pivot = partition(L, start, end)
    quick_sort_c(L, start, pivot)
    quick_sort_c(L, pivot+1, end)

# 划分左右区间的时候，通过直接开辟新的数组进行保存，这种方法极度损耗内存
def partition(L, start, end):
    left_list = []
    right_list = []
    base = L[start]
    for item in L[start+1 : end]:
        if item > base:
            right_list.append(item)
        else:
            left_list.append(item)
    temp_list = []
    temp_list.extend(left_list)
    temp_list.append(base)
    temp_list.extend(right_list)
    L[start:end] = temp_list
    return start + len(left_list)

test_list = [11, 4, 1, 56, 5, 8, 93, 12, 22, 3]
quick_sort(test_list)
print(test_list)
