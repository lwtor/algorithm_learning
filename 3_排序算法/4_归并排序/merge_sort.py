#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def merge_sort(L):
    return merge_scot_c(L, 0, len(L))

def merge_scot_c(L, start, end):
    if end - start <= 1:
        return
    center = int((start + end) / 2)
    print('left :', L[start:center])
    print('right:', L[center:end])
    print('-------------------------')
    merge_scot_c(L, start, center)
    merge_scot_c(L, center, end)
    merge_v2(L, start, center, end)

# 最开始写的合并函数
def merge(L, start, center, end):
    left_list = L[start:center]
    right_list = L[center:end]
    print('merge -- ', 'left:', left_list, ', right:',right_list)
    left_index = 0
    right_index = 0
    list_index = start
    while(left_index < len(left_list) or right_index < len(right_list)):
        if left_index == len(left_list):
            # print('left_list end')
            L[list_index] = right_list[right_index]
            list_index += 1
            right_index += 1
            continue

        if right_index == len(right_list):
            # print('right_list end')
            L[list_index] = left_list[left_index]
            list_index += 1
            left_index += 1
            continue

        if left_list[left_index] <= right_list[right_index]:
            # print('add left list')
            L[list_index] = left_list[left_index]
            list_index += 1
            left_index += 1
        else:
            # print('add right list')
            L[list_index] = right_list[right_index]
            list_index += 1
            right_index += 1
    print('after merge:', L[start:end])
    print('---------------------------')

# 改进后的合并函数，将左右区间遍历完之后的情况给移到循环外
def merge_v2(L, start, center, end):
    print('merge -- ', 'left:', L[start:center], ', right:',L[center:end])
    merge_list = []
    left_index = start
    right_index = center
    while left_index < center and right_index < end:
        if L[left_index] <= L[right_index]:
            merge_list.append(L[left_index])
            left_index +=1
        else:
            merge_list.append(L[right_index])
            right_index += 1
    if left_index == center:
        merge_list.extend(L[right_index:end])
    if right_index == end:
        merge_list.extend(L[left_index:center])
    print('after merge:', merge_list)
    L[start:end] = merge_list
    print('---------------------------')

test_list_1 = [6, 5, 3, 1, 8, 7, 2, 4, 9]
test_list_4 = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
test_list_5 = [11, 8, 3, 9, 7, 1, 2, 5]
test_list_6 = [3, 2, 1]
test_list = test_list_6
merge_sort(test_list)
print(test_list)

test_list_2 = [1, 3, 5, 7, 2, 4, 6, 8]
test_list_3 = [5, 6]
# merge_v2(test_list_3, 0, 1, 2)
# merge(test_list_3, 0, 1, 2)
# print(test_list_3)
