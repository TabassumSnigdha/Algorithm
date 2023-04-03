#!/usr/bin/env python
# coding: utf-8

# In[2]:


#2

def BFS(visited, graph, node):
    queue =[]
    visited[node-1]=1 
    queue.append(node)
    
    while len(queue)!=0:
         #deque m
        m=queue.pop(0)
        #print(m,end=" ")
        foutput.write(str(m)+" ")
      
        for neighbour in graph[m]:
            if visited[neighbour-1]==0:
                visited[neighbour-1]=1
                queue.append(neighbour)
                
#####################################################

finput=open('input2.txt','r')
foutput=open('output2.txt','w')
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
BFS(visited, graph, 1)


# In[ ]:




