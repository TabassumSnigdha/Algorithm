#!/usr/bin/env python
# coding: utf-8

# In[2]:


import heapq
import math


def Dijkstra(Graph, source):
    dist = []
    for i in range(len(Graph)+1):
        dist.append(math.inf)
    dist[source]=0
    
    visited=[0]*(len(Graph)+1)
    prev=[0]*(len(Graph)+1)
    queue=[]       
    
    for vertex in Graph:
        heapq.heappush(queue,(dist[vertex], vertex))   

    while len(queue)!=0:
        u,l=heapq.heappop(queue)
        if visited[l]:
            continue            
        visited[l]=True
        
        for v in graph[l]:
            alt=u+v[1]            
            if alt<dist[v[0]]:
                dist[v[0]]=alt
                prev[v[0]]=l
                heapq.heappush(queue,(dist[v[0]],v[0]))
                 
    return dist





f_r=open('input2.txt')
f_w=open('output2.txt','w')
graph={}
test=int(f_r.readline())
   
for i in range(test):
    line=f_r.readline()
    line=line.strip()
    line=line.split(" ")
    vartex=int(line[0])
    edeg=int(line[1])
        
    if vartex==1:
        graph[vartex]=[]
        f_w.write("0\n")
            
    else:
        for x in range(edeg):
            l=f_r.readline()
            l=l.strip()
            l=l.split(" ")
            
            vartex1=int(l[0])
            desti=int(l[1])
            titan=int(l[2])
            
                
            if vartex1 not in graph:
                graph[vartex1]=[]
                
            if desti not in graph:
                graph[desti]=[]
                
            graph[vartex1].append((desti,titan))

        retrn=Dijkstra(graph,1)
        graph = {}
        f_w.write(str(retrn[-1])+"\n")
        
f_r.close()
f_w.close()


# In[ ]:




