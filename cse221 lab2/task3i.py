#!/usr/bin/env python
# coding: utf-8

# In[1]:


#task03(i)

# low  –> Starting index,  high  –> Ending index */
def quickSort(arr, low, high) :
    if (low < high) :
        # pi is partitioning index, arr[pi] is now at right place 
        pi = partition(arr, low, high)
        quickSort(arr, low, pi- 1)  # Before pi
        quickSort(arr, pi + 1, high) # After pi
    

# This function takes last element as pivot, places the pivot element at its correct position in sorted array,
#and places all smaller (smaller than pivot) to left of pivot and all greater elements to right of pivot 
def partition (arr, low, high):
    
    # pivot (Element to be placed at right position)
    pivot = arr[high] 
    i = (low - 1)  # Index of smaller element and indicates the 
    # right position of pivot found so far
    for j in range(low, high):        
        
        # If current element is smaller than the pivot
        if (arr[j] < pivot):
            i=i+1    # increment index of smaller element
            #swap arr[i] and arr[j]
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1],arr[high] = arr[high],arr[i+1]
    
    #swap arr[i + 1] and arr[high])
    return (i+1)

#file read
input3=open("input3i.txt")
output3=open("output3i.txt","w")

l=input3.readlines()

l=l[1].split(" ")
#print(l)
array=[int(p) for p in l]
quickSort(array,0, len(array) - 1)
#print(array)
for i in array:
    output3.write(str(i)+" ")
input3.close()
output3.close()


# In[ ]:




