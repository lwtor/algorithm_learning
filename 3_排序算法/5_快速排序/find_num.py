#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 寻找第k大的元素
def find_num(L, rank):
    func = partition_right
    pivot = func(L, 0, len(L))
    while True:
        if pivot == rank - 1:
            return L[pivot]
        if pivot < rank - 1:
            pivot = func(L, pivot+1, len(L))
        else:
            pivot = func(L, 0, pivot)

def partition(L, start, end):
    base = L[end - 1]
    left = start
    right = start
    while right < end - 1:
        if L[left] <= base:
            left += 1
            right += 1
            continue
        if L[right] > base:
            right += 1
            continue
        L[left], L[right] = L[right], L[left]
        left += 1
        right += 1
    if not end - 1 == left:
        L[end-1], L[left] = L[left], base
    print('1 -- left:', L[start:left], " ,pivot:", L[left], ' ,right:', L[left+1:end])
    return left

def partition_left(L, start, end):
    base = L[start]
    # i 指向从左向右最后一个小于分区点的元素
    i = start
    for j in range(start+1, end):
        if L[j] < base:
            i += 1
            if not i == j:
                L[i], L[j] = L[j], L[i]
    L[start], L[i] = L[i], L[start]
    print('2 -- left:', L[start:i], ' ,pivot:', L[i], ' ,right:', L[i+1:end])
    return i

def partition_right(L, start, end):
    base = L[end - 1]
    high = end - 1
    for low in range(high, start - 1, -1):
        if L[low] > base:
            high -= 1
            if not low == high:
                L[low], L[high] = L[high], L[low]
    L[end-1], L[high] =L[high], L[end-1]
    print('3 -- left:', L[start:high], ' ,pivot:', L[high], ' ,right:', L[high+1:end])
    return high-1

test_list = [8, 7, 6, 5, 4, 3, 2, 11]
print(test_list)
print(find_num(test_list, 5))
# partition_right([1, 2, 3, 4], 0, 4)
