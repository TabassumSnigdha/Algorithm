#!/usr/bin/env python
# coding: utf-8

# In[2]:


def bubbleSort(arr):
    for i in range(len(arr)-1):
        swapped = False 
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped=True
        if swapped is False:
            return arr       
    return arr
        
#if the array is sorted then the time complexity will be T(n)=O(n) because only the outer loop will be executed once and the inner loop n times"
#arr=[6,7,1,3]
#bubbleSort(arr)
#print(arr)
input1=open("input3.txt",'r')
arr=input1.readlines()  #['3', '2', '1','4','5']
#print(arr)
output1=open("output3.txt","w")
for i in range(0,len(arr),2):
    number=arr[i].strip()
    #print(arr[i])
    #i+=1
    #print(arr[i])
    small_arr=arr[i+1].split(" ")
    small_arr=[y.strip() for y in small_arr]
    small_arr=[int(y) for y in small_arr]
    smal=bubbleSort(small_arr)
    #print(smal)
    for y in smal:
        output1.write(str(y)+" ")
    output1.write("\n")
    #i+=1
input1.close()
output1.close()


# In[ ]:




