from collections import deque
a = ["12","shubh",34,"lodhi"]
s = ("shubh","lodhi")
f = deque(s)

print(f)
f.append("shubh")
print(f)
f.pop()
print(f)
d = deque(a)
print(d)
d.append("singh")
print(d)
d.appendleft("kilos")
print(d)
d.pop()
print(d)
(d.popleft())
print(d)