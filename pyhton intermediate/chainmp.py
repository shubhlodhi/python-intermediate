from collections import ChainMap
a = {1:"shubh",2:"lodhi"}
b = {1:"hello", 2: 45}
d = [12,12,12]
f = [23,23,23]
g = ChainMap(d,f)
print(g)
t = ChainMap(a,b)
print(t)