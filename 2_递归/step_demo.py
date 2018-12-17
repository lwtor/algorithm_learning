#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def step_calculate(num):
    print('step_calculate', num)
    if num == 1:
        return 1
    if num == 2:
        return 2
    return step_calculate(num - 1) + step_calculate(num - 2)

step_count = input("输入台阶数：")
count = step_calculate(int(step_count))
print('%s 个台阶，总共有 %d 种情况' %(step_count, count))
