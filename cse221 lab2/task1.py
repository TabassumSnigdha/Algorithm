#!/usr/bin/env python
# coding: utf-8

# In[1]:


#array1=[11,45,34,22,12]
#arrayMark=[40,50,20,10,10]

def insertionSort(array1,arrayMark): 
    for j in range(len(arrayMark)):
        for i in range(0,len(arrayMark)-1):
            if(arrayMark[i]<arrayMark[i+1]):
                temp=arrayMark[i]
                arrayMark[i]=arrayMark[i+1]
                arrayMark[i+1]=temp
                #print(arrayMark)
                
                tempID=array1[i]
                array1[i]=array1[i+1]
                array1[i+1]=tempID
                #print(array1)

#insertionSort(array1,arrayMark)

inputTXT = open("input1.txt","r")
lines = inputTXT.read().splitlines()

#Taking array1(studentID) and arrayMark(Student Marks) from inputtxt
array1=[int(i) for i in lines[1].split()]
arrayMarks=[int(j) for j in lines[2].split()]


#calling insertion Sort on array1 and arrayMarks
insertionSort(array1,arrayMarks)
output = open("output1.txt","w")


#writing the sorted array1 on outputtxt
for variable in array1:
    output.write(f"{variable} ")
    
    
inputTXT.close() 
output.close()


# In[ ]:




