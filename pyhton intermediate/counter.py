from collections import Counter
# counter is a dictionary subclass for counting hashable objects
a = [1,2,3,4,5,6,7,7,7,4,3,3,3,3]
j = (1,"shubh","lodhi","shubh")
ld = {1:1}
f = Counter(j)
print(list(f.elements()))
# print(tuple(f.subtract(ld)))
print(f)
s = Counter(a) 
print(s)
print(list(s.elements()))
print(tuple(s.elements()))
sub = {7:2,3:1}
print((s.subtract(sub)))
print(list(s.elements()))
print(s)
