#!/usr/bin/env python
# coding: utf-8

# In[2]:


def BFS(graph,visited, node, goal,parent):
    queue = []  
    visited[node-1]=1 
    queue.append(node)
    if node == goal:
        foutput.write("Time: 0")
        foutput.write("\nShortest path: "+str(node))
     
    while len(queue)!=0:
        m=queue.pop(0) 
        
        for neighbour in graph[m]: #[2]
            if visited[neighbour-1]==0:
                visited[neighbour-1]=1
                queue.append(neighbour)
                parent[neighbour]=m
                 
                
                if neighbour == goal:
                    #print("parent",parent)
                    p=""
                    c=-1
                    des=destination
                    while des!=None:
                        p=" " +str(des)+p
                        des=parent[des]
                        c+=1
                    foutput.write("Time: "+str(c))
                    foutput.write("\nShortest path: "+p)
                    return
####################################################

finput=open('input5.txt','r')
foutput=open('output5.txt','w')
graph={}
l1=finput.readline().split()
n=int(l1[0])
e=int(l1[1])
destination=int(l1[2])
for i in range(1,n+1):
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
visited=[0]*n
parent=[None]*(n+1)
   
#graph = {1: [2, 3, 4], 2: [1, 5], 3: [1, 9], 4: [1, 6, 7], 5: [2], 6: [4, 8], 7: [4], 8: [6], 9: [3]}
BFS(graph,visited, 1,destination,parent)


# In[ ]:





# In[ ]:




