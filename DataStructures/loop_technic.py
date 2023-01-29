from math import isnan

from numpy import maximum
dic = {'a': 1, 'b': 2, 'c': 3, 1: 3}
# set = {1, 22, 3}
# for k, v in dic.items():
#     print(k, v)
# print(end='\n')

# arr = (113, 2, 3)

# for i, v in enumerate(dic):
#     print(i, v)


# for i, v in enumerate(set):
#     print(i, v)


# print( i for i in dic.items())

print(dic.fromkeys(dic.keys(), 1))
print(dic.pop('a'))
print(dic)

a = [1, 2, 3]
b = [4, 5, 6]
for k, v in zip(a, b):
    print(k, v)
    
    
import sys
print(sys.maxsize)