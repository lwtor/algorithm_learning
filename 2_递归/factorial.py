#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 普通的递归函数，从打印中可以看出函数栈里保存了5个函数
def factorial(n):
    print('factorial', n)
    if  n == 1:
        return 1
    else:
        return factorial(n-1) * n

# 使用了尾递归的函数，由于python自身不支持尾递归，所以和上面的函数得到的是一样的结果
def factorial_v2(n, res):
    print('factorial_v2', n, res)
    if n == 1:
        return res
    else:
        return factorial_v2(n-1, n*res)

print(factorial(5))
print(factorial_v2(5, 1))
