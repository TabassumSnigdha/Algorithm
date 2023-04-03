#!/usr/bin/env python
# coding: utf-8

# In[2]:


def assignment_selection(arr, n):
    arr.sort()
    ans.append(arr[0])
    cnt = 1
    f = arr[0][0]

    for i in range(1, n):
        if arr[i][1] >= f:
            cnt += 1
            f = arr[i][0]
            ans.append(arr[i])

    w.write(str(cnt)+ '\n')
    for p in ans:
        w.write(f"{p[1]} {p[0]}\n")


arr = []
ans = []
r = open("input1.txt")
w = open("output1.txt", 'w')
lst = r.read().split("\n")

n = int(lst[0])

for i in range(1, n+1):
    x, y = lst[i].split(' ')
    x = int(x)
    y = int(y)
    arr.append((y, x))

assignment_selection(arr, n)


# In[ ]:




