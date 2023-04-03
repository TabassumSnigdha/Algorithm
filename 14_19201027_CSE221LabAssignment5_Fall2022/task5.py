#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Task-05

import heapq
import math

def Network(Graph, source):
    dist=[-math.inf]*(len(Graph)+1)
    dist[source]=0
    Q=[]
    visited=[0]*(len(Graph)+1)
    prev=[0]*(len(Graph)+1)   
    prev[source]=1
    
    for v in Graph:
        heapq.heappush(Q,(dist[v],v)) 
    #print(Q)    
    heapq._heapify_max(Q)
    #print(Q)    
    while len(Q)!=0:
        u,l=heapq._heappop_max(Q)        
        if visited[l]==1:
            continue        
        visited[l]=1
        
        for v in Graph[l]:
            alt = 0            
            if u==0:
                alt=v[1]
            elif v[1]==0:
                alt=u
            elif u<v[1]:
                alt=u
            else:
                alt=v[1]
                
            if alt>dist[v[0]]:
                dist[v[0]]=alt
                prev[v[0]]=l
                
                heapq.heappush(Q, (dist[v[0]],v[0]))
                heapq._heapify_max(Q)
                
    return dist
##################################################################################

file_read=open('input5.txt')
file_write=open('output5.txt','w')
lst=file_read.readlines()
lst=[(i).strip() for i in lst]
#print(lst)

graph={}    
test=int(lst[0])

for i in range(1,len(lst)):
    l=lst[i].split(" ")
    #print(lst[i],"pk")
    source=None
    if len(l)==2:
        n=int(l[0])
        e=int(l[1])
        
        if e==0:
            graph[n]=[]
            i=i+1
            source=int(lst[i])
            
        else:
            for j in range(e):
                i=i+1
                l=lst[i].split(" ")
                var1=int(l[0])
                var2=int(l[1])
                cost=int(l[2])
                
                if var1 not in graph:
                    graph[var1]=[]                
                if var2 not in graph:
                    graph[var2]=[]                
                graph[var1].append((var2, cost))
            
            i=i+1
            source=int(lst[i])
        ans=Network(graph,source)
        #print(graph) 
        #print(ans)
        graph={}
        ans=ans[1:]
        
        for i in ans:
            if i < -1:
                file_write.write("-1"+" ")
            else:
                file_write.write(str(i)+" ")

        file_write.write("\n")          
                
file_read.close()
file_write.close()


# In[ ]:




