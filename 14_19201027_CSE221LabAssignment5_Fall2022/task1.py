#!/usr/bin/env python
# coding: utf-8

# In[10]:


import heapq
import math

def Dijkstra(Graph, source):
    dist = [math.inf]*(len(Graph)+1)
    dist[source]=0
    Q=[]
    visited=[0]*(len(Graph)+1)
    prev=[0]*(len(Graph)+1)   
    
    for v in Graph:
        heapq.heappush(Q,(dist[v], v))   

    while len(Q)!=0:
        u,l=heapq.heappop(Q)
        if visited[l]:
            continue
            
        visited[l]=True
        
        for v in graph[l]:
            alt=u+v[1]
            
            if alt<dist[v[0]]:
                dist[v[0]]=alt
                prev[v[0]]=l
                heapq.heappush(Q,(dist[v[0]],v[0]))
    #print(prev) 
    return prev


################################################






file_read=open('input1.txt')
file_write=open('output1.txt','w')
d={"Motijheel":1,"A":2,"B":3,"C":4,"D":5,"E":6,"F":7,"G":8,"H":9,"I":10,"J":11,"K":12,"L":13,"MOGHBAZAR":14}
ds={1:"Motijheel",2:"A",3:"B",4:"C",5:"D",6:"E",7:"F",8:"G",9:"H",10:"I",11:"J",12:"K",13:"L",14:"MOGHBAZAR"}
graph={}
for i in range(1,15):
    graph[i]=[]
lst=file_read.readlines()
for line in lst:
    s,e,c=line.strip().split(" ")
    s=d[s]
    e=d[e]
    c=int(c)
    if s not in graph:
        graph[s]=[(e,c)]
        graph[e]=[(s,c)]
    else:
        graph[s]=graph[s]+[(e,c)]
        graph[e]=graph[e]+[(s,c)]
#print(graph)
ans=Dijkstra(graph,1)  
#print(ans)
path="MOGHBAZAR"
n=ans[14]
#print([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14])
while n!=0:
    path=ds[n]+"-->"+path
    n=ans[n]
#print(path)
file_write.write(path)
file_write.close()


# In[ ]:





# In[ ]:




