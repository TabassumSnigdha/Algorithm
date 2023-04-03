#!/usr/bin/env python
# coding: utf-8

# In[1]:


#task4(snigdha)
def Cyclic_checker(graph,visited,stack,node):
    visited[node-1] = 1
    stack[node-1] = 1
 
    for neighbour in graph[node]:
        if visited[neighbour-1] == 0:
            if Cyclic_checker(graph,visited,stack,neighbour) == 1:
                return 1
        elif stack[neighbour-1] == 1:
            return 1
 
    stack[node-1] = 0
    return 0

def Cyclic(graph,n,e):
    visited = [0] * (n)
    stack = [0] * (n)
    for node in graph:
        if visited[node-1] == 0:
            if Cyclic_checker(graph,visited,stack,node) == 1:
                return ("found")
    return ("Not found")
   
    
##########################################    
finput=open('input2.txt','r')
foutput=open('output4.txt','w')
graph={}
l1=finput.readline().split()
n=int(l1[0])
e=int(l1[1])
for i in range(n+1):
    graph[i]=[]
for j in range(e):
    l2=finput.readline()
    x,y=l2.split()
    x=int(x)
    y=int(y)
    if x in graph.keys():
        graph[x].append(y)
#print(graph)

cycl=Cyclic(graph,n,e)
if cycl=="found":
    foutput.write("Yes")
else:
    foutput.write("No")
foutput.close()


# In[ ]:




