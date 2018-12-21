#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def counting_sort(L, max):
    # C = [0 for i in range(max+1)]
    C = [0] * (max+1)
    for i in L:
        C[i] = C[i] + 1
    count = 0
    for i in range(len(C)):
        count += C[i]
        C[i] = count
    new_list = [0] * len(L)
    for i in L:
        index = C[i]
        new_list[index-1] = i
        C[i] = index - 1

counting_sort([2,5,3,0,2,3,0,3], 5)
