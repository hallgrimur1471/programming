#!/usr/bin/env python3

a = [3,5,8]
b = [4,6]

if len(b) < len(a):
    b.append([])
elif len(a) < len(b):
    a.append([])

d = []
for i in range(len(a)):
    d.append(a[i])
    d.append(b[i])
d = list(filter(lambda x: x!=[], d))
print(d)
