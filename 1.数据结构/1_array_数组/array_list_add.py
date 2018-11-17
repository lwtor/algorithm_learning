list = [1, 2, 3, 4, 5]
k = 'a'
print("origin: %s , k=%s" %(list, k))
temp = list[3]
list[3] = k
list.append(temp)
print("result: %s" %(list))
