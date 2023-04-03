#!/usr/bin/env python
# coding: utf-8

# In[1]:


def Bubble_Sort(s):
    for i in range(len(s)):
        for j in range(0, len(s)-i-1):
            if s[j] > s[j+1]:
                s[j], s[j+1] = s[j+1], s[j]


def enque(name,patient):
    name,seriel=name.split(" ")
    patient.append([name,seriel])
    
def seeDoctor(patient):
    s=[]
    for i in patient:
        s.append(int(i[1]))
        
    Bubble_Sort(s)
    out=str(s[0])
    
    for i in range(len(patient)):
        if out in patient[i]:
            p=patient.pop(i)
            return p
            
def printQueue(patient):
    return(patient)
    
            
###############################################

input4=open("input4.txt")
lst=input4.readlines()
patient=[]
#print(lst)
for name in lst:
    name=name.strip()
    if name!="see doctor":
        enque(name,patient)
        #print(patient)
    else:
        
        print("Patients list: ",printQueue(patient))
        p=seeDoctor(patient)
        print("doctor watch: ",p,"\nRemainin patient: ",printQueue(patient))
        print()
        
    
input4.close()


# In[ ]:




