#!/usr/bin/env python
# coding: utf-8

# In[3]:


def merge(A,p,q,r):
    n1=q-p+1
    n2=r-q
    L=[]
    R=[]
    for i in range(0,n1):
        L.append(A[p+i])
    for j in range(0,n2):
        R.append(A[q+j+1])
    i=j=0
    k = p    
    while(i < n1 and j< n2):
        if L[i] <= R[j]:
            A[k] = L[i]
            i+=1
        else:
            A[k]=R[j]
            j+=1
        k+=1  
    while(i<n1):
        A[k] = L[i]
        i=i+1
        k=k+1      
    while(j<n2):
        A[k]=R[j]
        j=j+1
        k=k+1
def mergeSort(A,p,r):      
        if(p<r):
            q=int((p+r)/2)
            mergeSort(A,p,q)
            mergeSort(A,q+1,r)     
            merge(A,p,q,r)
inputX=open("input2.txt","r")
lines=inputX.read().splitlines()
finalArray=[int(x) for x in lines[1].split()]
mergeSort(finalArray,0,int(lines[0])-1)
output = open("output2.txt","w")




#inseret value on output 
for variable in finalArray:
    output.write(f" {variable } ")
    
inputX.close()  
output.close()


# In[ ]:




