#!/usr/bin/env python
# coding: utf-8

# In[3]:


input_file=open('input1b.txt')
output_file=open('output1b.txt','w')
n=int(input_file.readline()) # case no
for i in range(n):
    l=input_file.readline()
    l=l.strip().split(" ")
    r=0
    if l[2]=="+":
        r=int(l[1])+int(l[3])
        output_file.write("The result of "+l[1]+" "+l[2]+" "+l[3]+" is "+str(r)+"\n")
    elif l[2]=="-":
        r=int(l[1])-int(l[3])
        output_file.write("The result of "+l[1]+" "+l[2]+" "+l[3]+" is "+str(r)+"\n")
    elif l[2]=="*":
        r=int(l[1])*int(l[3])
        output_file.write("The result of "+l[1]+" "+l[2]+" "+l[3]+" is "+str(r)+"\n")
    elif l[2]=="/":
        r=int(l[1])/int(l[3])
        output_file.write("The result of "+l[1]+" "+l[2]+" "+l[3]+" is "+str(r)+"\n")


input_file.close()
output_file.close()


# In[ ]:




