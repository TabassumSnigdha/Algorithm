#!/usr/bin/env python
# coding: utf-8

# In[2]:


#1(b)
finput=open('input1b.txt','r')
foutput=open('output1b.txt','w')
graph={}
l1=finput.readline().split()
n=int(l1[0])
e=int(l1[1])
for i in range(n+1):
    graph[i]=[]
for j in range(e):
    l2=finput.readline()
    x,y,z=l2.split()
    x=int(x)
    y=int(y)
    z=int(z)
    if x in graph.keys():
        graph[x].append((y,z))
for key,val in graph.items():
    foutput.write((f'{key}:{str(val)}\n'))


# In[ ]:





# In[ ]:




