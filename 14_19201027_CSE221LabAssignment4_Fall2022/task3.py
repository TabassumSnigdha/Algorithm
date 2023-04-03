#!/usr/bin/env python
# coding: utf-8

# In[3]:


def DFS_VISIT (graph,visited, node):
    #print(node,end=" ")
    foutput.write(str(node)+" ")
    visited[int(node)-1]=node

    for neighbour in graph[node]:
        if neighbour not in visited:
            DFS_VISIT(graph,visited,neighbour)
    
            
#This part is needed if the graph is disconnected. 
def DFS (graph,visited, node ):
    for node in graph:
        if node not in visited:
            DFS_VISIT(graph,visited, node)

    
            

   
    
##########################################    
finput=open('input3.txt','r')
foutput=open('output3.txt','w')
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
        graph[y].append(x)
#print(graph)

visited =[0]*n
DFS( graph,visited, 1)


# In[ ]:





# In[ ]:





# In[ ]:




