#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def insertion_sort(L):
    swap_count = 0
    count = 0
    for i in range(1, len(L)):
        for j in range(0, i):
            count += 1
            if L[i] < L[j]:
                swap_count += 1
                tmp = L[j]
                L[j] = L[i]
                L[i] = tmp
    print('swap count: ', swap_count, 'count: ', count)
    return L

def insertion_sort_anim(L):
    swap_count = 0
    count = 0
    for i in range(1, len(L)):
        p = i
        for j in range(i - 1, -1, -1):
            count += 1
            if L[j] > L[p]:
                swap_count += 1
                tmp = L[j]
                L[j] = L[p]
                L[p] = tmp
                p = j
            else:
                break
    print('swap count: ', swap_count, 'count: ', count)
    return L

test_list_1 = [6, 5, 3, 1, 8, 7, 2, 4]
test_list_2 = [1, 2, 3, 4, 5, 6, 7, 8]
func = insertion_sort
print(func([3,2,1]))
print(func(test_list_1))
print(func(test_list_2))

# insertion_sort_anim([1, 2, 3])
