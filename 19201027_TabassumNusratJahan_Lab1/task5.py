#!/usr/bin/env python
# coding: utf-8

# In[2]:


input_file=open('input5.txt')
output_file=open('output5.txt','w')
n=input_file.readline() 
l=[]
name=[]
# normal list creat
for i in range(int(n)):
    s=input_file.readline().strip()
    l.append(s)
    
    s=s.split(" ")
    name.append(s[0])
#print(l)
    
#Sort by name

for i in range(len(name)-1):
    mn=name[i]
    idx=i
    for j in range(i+1,len(name)):
        
        if name[j]<mn:
            mn=name[j]
            idx=j
            
        #for same name     
        if name[j]==mn:
            lst1=l[i].split(" ")
            lst2=l[j].split(" ")
            if (lst1[-1])>(lst2[-1]):
                mn=name[j]
                idx=j
                
    temp=name[i]
    name[i]=name[idx]
    name[idx]=temp
        
    temp=l[i]
    l[i]=l[idx]
    l[idx]=temp

        
# write

for i in l:
    output_file.write(i+"\n")

input_file.close()
output_file.close()


# In[ ]:




