#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def selection_sort(L):
    for i in range(0, len(L)):
        min_pos = i
        print('1', L)
        for j in range(i+1, len(L)):
            if L[j] < L[min_pos]:
                min_pos = j
        tmp = L[min_pos]
        L[min_pos] = L[i]
        L[i] = tmp
    return L

test_list_1 = [6, 5, 3, 1, 8, 7, 2, 4]
print(selection_sort(test_list_1))
