# -*- coding:utf-8 -*-

array_list = [4, 2, 3, 5, 9, 6]
array_empty = []

# 普通的在数组中查询key值的
def find_on_array(array, key) :
    if len(array) == 0 :
        return -1
    else :
        i = 0
        while i < len(array_list):
            if array_list[i] == key :
                return i
            i = i + 1
    return -1

# 使用哨兵结点
def find_on_array_use_sentinel(array, key):
    length = len(array)
    if length == 0:
        return -1
    temp = array[length - 1]
    if array[length - 1] == key :
        return length - 1
    array[length - 1] = key
    i = 0
    while array[i] != key:
        i = i + 1
    if i == length - 1 :
        return -1
    else :
        return i

def explain_result(position) :
    if position == -1 :
        print("could not find the key")
    else :
        print("the key's position is ", position + 1)
    return

print("array list : ", array_list)

key = input("input the number you want to find : ")
#position = find_on_array(array_list, key)
position = find_on_array_use_sentinel(array_list, key)
explain_result(position)
