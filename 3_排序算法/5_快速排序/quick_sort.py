#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def quick_sort(L):
    quick_sort_interval(L, 0, len(L))

def quick_sort_interval(L, start, end):
    if start >= end -1:
        return
    print('list:', L[start:end])
    pivot = partition_v1_1(L, start, end)
    quick_sort_interval(L, start, pivot)
    quick_sort_interval(L, pivot + 1, end)

# 最后一个元素作为分区点，从左向右遍历数组
def partition_v1(L, start, end):
    base = L[end-1]
    i = start
    # 先找出第一个大于分区点元素的位置
    while L[i] < base and i < end - 1:
        i += 1
    # 从第一个大于分区点的位置开始遍历
    for j in range(i+1, end-1):
        if L[j] <= base:
            L[i], L[j] = L[j], L[i]
            i += 1
    # 将分区点与第一个大于分区点的元素交换位置
    if not end - 1 == i:
        L[end-1], L[i] = L[i], base
    print('left:', L[start:i], ' ,pivot:', L[i], ' ,right:', L[i+1:end])
    print('pivot', i)
    return i

# 也是最后一个元素作为分区点，从左向右便利，不同于上面的版本，只是用了一个 while 循环
def partition_v1_1(L, start, end):
    base = L[end - 1]
    i = start
    j = start
    while j < end - 1:
        if L[i] < base:
            i += 1
            j += 1
            continue
        if L[j] > base:
            j += 1
        else:
            L[i], L[j] = L[j], L[i]
            i += 1
            j += 1
    if not end - 1 == i:
        L[end-1], L[i] = L[i], base
    print('left:', L[start:i], ' ,pivot:', L[i], ' ,right:', L[i+1:end])
    print('pivot', i)
    return i

# 第一个元素为分区点
# 左右两个指针
# 左指针指向从左开始第一个大于分区点的元素的位置
# 右指针指向从右开始最后一个大于分区点的元素
def partition_v2(L, start, end):
    base = L[start]
    left = start + 1
    right = end - 1
    while left < right:
        # 左指针，从左向右开始遍历，如果指向的元素小于分区点，则向左，指向下一个元素
        if L[left] <= base:
            left += 1
            continue
        # 右指针，从右向左便利，如果指向的元素大于分区点，则向右，指向前一个元素
        if L[right] > base:
            right -= 1
            continue
        # 当左指针指向一个大于分区点的元素，而右指针指向了一个小于等于分区点的元素
        # 则交换两个指针所指向的元素
        L[left], L[right] = L[right], L[left]
        # 左右指针分别前进 1
        left += 1
        right -= 1
    # 判断左指针最后指向的元素与分区点的大小，
    pivot = left
    if L[pivot] > base:
        pivot -= 1
    # 交换分区点与左指针的元素
    L[start], L[pivot] = L[pivot], base
    print('left:', L[start:pivot], ' ,pivot:', L[pivot], ' ,right:', L[pivot+1:end])
    print('pivot', pivot)
    return pivot

# 根据动画实现
def partition_anim(L, start, end):
    base = L[start]
    left = start + 1
    right = left
    while right < end:
        if L[left] <= base:
            left += 1
            right += 1
            continue
        if L[right] > base:
            right += 1
            continue
        L[left] = L[right]
        left += 1
        right += 1
    pivot = left
    if pivot >= end:
        pivot = end - 1
    if L[pivot] > base:
        pivot = left - 1
    L[start], L[pivot] = L[pivot], base
    print('left:', L[start:pivot], ' ,pivot:', L[pivot], ' ,right:', L[pivot+1:end])
    print('pivot', pivot)
    return pivot

test_list_1 = [6, 5, 3, 1, 8, 7, 2, 4, 9]
test_list_2 = [5, 1, 8, 6, 7]
test_list_3 = [8, 7, 6, 5, 4, 3, 2, 1]
test_list_4 = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
test_list_5 = [6, 11, 3, 9, 8]

test_list = test_list_5
quick_sort(test_list)

# print(test_list)
# partition_v1(test_list, 0, len(test_list))

print(test_list)
