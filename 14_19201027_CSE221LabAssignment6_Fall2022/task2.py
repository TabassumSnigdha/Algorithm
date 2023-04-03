#!/usr/bin/env python
# coding: utf-8

# In[2]:


def assignment_selection(arr,n,m):
    arr.sort()
    lst1[0] = arr[0][0]
    total[0] += 1
    f = arr[0][0]

    for i in range(1, n):
        for j in range(m):
            if arr[i][1] >= lst1[j] or lst1[j] == -1:
                lst1[j] = arr[i][0]
                f = arr[i][0]
                total[j] += 1

    sum = 0
    for i in total:
        sum += i
    w.write(str(sum))


arr = []
ans = []
r = open("input2.txt")
w = open("output2.txt", 'w')
lst = r.read().split("\n")

n, m = lst[0].split(' ')
n = int(n)
m = int(m)

for i in range(1, n+1):
    x, y = lst[i].split(' ')
    x = int(x)
    y = int(y)
    arr.append((y,x))

lst1 = [-1] * m
total = [0] * m

assignment_selection(arr,n,m)


# In[ ]:




