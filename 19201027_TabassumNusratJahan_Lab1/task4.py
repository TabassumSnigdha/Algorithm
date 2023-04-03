#!/usr/bin/env python
# coding: utf-8

# In[4]:


input_file=open('input4.txt')
output_file=open('output4.txt','w')
n=input_file.readline() # student no 
id=input_file.readline().strip().split(" ")
marks=input_file.readline().strip().split(" ")

for i in range(len(marks)-1):
    mx=int(marks[i])
    idx=i
    for j in range(i+1,len(marks)):
        if int(marks[j])>mx:
            mx=int(marks[j])
            idx=j
        #for id maintain if marks same    
        if int(marks[j])==mx:
            if int(id[j])<int(id[i]):
                mx=int(marks[j])
                idx=j
    
    temp=marks[i]
    marks[i]=str(mx)
    marks[idx]=temp
    
    temp=id[i]
    id[i]=id[idx]
    id[idx]=temp
    
#write
for i in range(len(id)):
    output_file.write("ID: "+id[i]+" Mark: "+marks[i]+"\n")
    

input_file.close()
output_file.close()


# In[ ]:




