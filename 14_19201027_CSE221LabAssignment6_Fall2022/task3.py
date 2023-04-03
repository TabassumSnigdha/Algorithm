#!/usr/bin/env python
# coding: utf-8

# In[3]:


r = open("input3.txt")
w = open("output3.txt", 'w')
lst = r.read().split("\n")

n = int(lst[0])
arr = lst[1].split(' ')
st = lst[2]

arr.sort()

ans = ""
jack = 0
jill = 0

tmp = []
for i in st:
    if i == 'J':
        tmp.append(arr[0])
        ans += (arr[0])
        jack += int(arr[0])
        arr.pop(0)
    elif i == 'j':
        ans += (tmp[len(tmp) - 1])
        jill += int(tmp[len(tmp) - 1])
        tmp.pop()

w.write(ans)
w.write(f"\nJack will work for {jack} hours")
w.write(f"\nJill will work for {jill} hours")


# In[ ]:




