#!/usr/bin/env python
# coding: utf-8

# In[2]:


def DFS(i, j,visited,graph,daimond,d_lst):
    
    #print(i,j)
    visited[i][j] = 1
    if graph[i][j] == 'D':
        d_lst.append((i,j))
    
    
    #col
    if (j < c)  and (graph[i][j+1] != '#') and (visited[i][j+1]==0):
        #print(i,j)
        DFS(i,j+1,visited,graph,daimond,d_lst)
    if (j > 1)  and (graph[i][j-1] != '#') and (visited[i][j-1]==0):
        #print(i,j)
        DFS(i, j-1,visited,graph,daimond,d_lst)
    ###################
       
    #row
    if (i < r) and (graph[i+1][j] != '#') and (visited[i+1][j]==0):
        #print(i+1,j)
        DFS(i+1, j,visited,graph,daimond,d_lst)
    if (i > 1)  and (graph[i-1][j] != '#') and (visited[i-1][j]==0):
        DFS(i-1, j,visited,graph,daimond,d_lst)
        
    
    
##################################################
finput = open("input6.txt")
foutput= open("output6.txt","w")
l = finput.readline().strip().split(" ")
r=int(l[0])
c=int(l[1])

#print(r,c)
t=[0]*(c+1)
graph=[t]
for i in range(r):
    s = finput.readline().strip()
    tl=[0]
    #print(string[0])
    for j in range(len(s)):
        #print(len(j))
        tl.append(s[j])
    graph.append(tl)
#print(graph)
      
visited=[]
for i in range(r+1):
    visited.append([0]*(c+1))
#print(visited)


##############################
daimond=0
d_lst = []
for i in range(1,r+1):
    for j in range(1,c+1):
        if (graph[i][j]!='#') and  (visited[i][j]==0):
            d_lst = []
            #dfs(i,j)
            DFS(i, j,visited,graph,daimond,d_lst) 
            daimond = max(daimond, len(d_lst))

foutput.write(str(daimond))

foutput.close()


# In[ ]:




