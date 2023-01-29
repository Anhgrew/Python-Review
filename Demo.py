map = { 'anhgrew' : [ 'devops', 'Backend' ], 'grew' : [ 'Mobile', 'AWS' ] }

print(list(map.values())[0][0].lower())

import random

l = [ 1, 2, 3, 4, 5 ]

print(dir(l))

random.shuffle(l)


print(random.choice(l))

string = [ "xxxxoaaa", "b", "c" ]

print(string[0].find("a")) 

print("+".join(string))

print(string[0].split('o'))

string.extend(["d", "l"])

print(string)

string.insert(2, "Anhbren")

print(string)

print(string.pop(3))

def tt(targ):
    for i in targ:
        print(i)


def pp(a, *r):
    print("YYY", a)
    for i in r:
        print(i)


tt([1, 2, 3])
pp(1,2,3,4)

