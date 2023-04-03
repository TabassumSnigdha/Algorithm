#!/usr/bin/env python
# coding: utf-8

# In[22]:


file = open("input1a.txt","r")
line = file.readlines()
lst = []
for i in line:
    i = i.strip()
    lst.append(int(i))
n = (lst[0])
output = open("output1a.txt","w")
for i in range(1,n+1):
    if lst[i]%2==0:
        output.write(str(lst[i])+"is a even number\n")
    elif lst[i]%2==1:
        output.write(str(lst[i])+"is an odd number\n")
file.close()


# In[ ]:




