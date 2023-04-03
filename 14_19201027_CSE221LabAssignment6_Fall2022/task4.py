#!/usr/bin/env python
# coding: utf-8

# In[1]:


file_read=open("input4.txt")
file_write=open("output4.txt","w")
l=file_read.readlines()
#print(l)
for i in l:
    c=0
    i=i.strip()
    a,b=i.split(" ")
    if a=="0" and b=="0":
        break
    for j in range(int(a),int(b)):
        if j*j<=int(b):
            c+=1
        else:
            break
    file_write.write(str(c)+"\n")
file_read.close()
file_write.close()


# In[ ]:




