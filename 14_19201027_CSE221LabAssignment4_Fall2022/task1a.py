#!/usr/bin/env python
# coding: utf-8

# In[3]:


#1(a)
file= open("input1a.txt")
file_out= open("output1a.txt","w")
line = file .readlines()
lst= []
for i in line:
    i = i.strip()
    i = i.split()
    lst.append(i)
nodes= int(lst[0][0])
edges = int(lst[0][1])
a= [[0 for _ in range(nodes+1)] for _ in range(nodes+1)]

r=[]
c=[]
value=[]
for i in range(1,len(lst)):
    r.append(lst[i][0])
    c.append(lst[i][1])
    value.append(lst[i][2])
#print(a,r,c,value)
for i in range(0,len(a)):
    for j in range (0,len(r)):
        f= int(r[j])
        h= int(c[j])
        a[f][h]= int(value[j])
for i in range (0,len(a)):
    for j in range (0,len(a[i])):
        file_out.write(str(a[i][j])+" ")
    file_out.write("\n")


# In[ ]:





# In[ ]:




