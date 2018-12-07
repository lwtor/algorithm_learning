#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def bubble_sort(L):
    step_count = 0
    for i in range(1, len(L)):
        for j in range(0, len(L) - i):
            step_count += 1
            if L[j+1] < L[j]:
                tmp = L[j+1]
                L[j+1] = L[j]
                L[j] = tmp
            print('step', (i-1) * 10 + j , '-->', L)
    print('step count %d' %step_count)
    return L

def bubble_sort_plus(L):
    step_count = 0
    bubble_count = 0
    for i in range(1, len(L)):
        has_change = False
        bubble_count += 1
        for j in range(0, len(L) - i):
            step_count += 1
            if L[j+1] < L[j]:
                has_change = True
                tmp = L[j+1]
                L[j+1] = L[j]
                L[j] = tmp
            # print('step', (i-1) * 10 + j , '-->', L)
        if not has_change:
            break
        # print('step', i, '-->', L)
    print('step count %d, bubble count %d' %(step_count, bubble_count))
    return L

L = [1, 3, 5, 7, 2, 4, 6, 8, 9]
test_list = [3, 54, 63, 4, 2, 5, 14, 21, 46]
test_list1 = [3, 2, 1]
test_list2 = [1, 2, 3]

# print(bubble_sort(L))
# print(bubble_sort(test_list))
# print(bubble_sort(test_list1))
# print(bubble_sort(test_list2))
print('-------------------------------')
# print('origin -->', L)
# print(bubble_sort_plus(L))
# print(bubble_sort_plus(test_list))
# print(bubble_sort_plus(test_list1))
# print(bubble_sort_plus(test_list2))
print(bubble_sort_plus([3, 5, 4, 1, 2, 6]))
