a = set([1, 2, 3])
b = set([2, 3, 4])

print(a ^ b)

print({x for x in 'abcs' if x not in 'ac'})

map = {'f': 1, 'b': 4, 'c': 3}
# print(map['a'])

# del map['a']

tmp_map = sorted(map, reverse=False)

list_key = list(map.keys())
print(list_key)
print(tmp_map)
