//construct a program to create the following array using numpy.arr=([1,2,3],[4,5,6]) perform the following operations on the array using numpy features//
 
 import numpy as numpy
 a=np.array(lst)
 print(a.ndim)
 print(a.shape)
 print(a.size)
 print(a.dtype)

 //An election is conted by five candidates the numbered 1 to 5
 and the voting is done by marking the conditon number on the ballot paper//

 count=[0,0,0,0,0]
 spoit=0
 n=int(input("Enter no of ballets: "))
 for i in range(n):
 vote=int(input("Enter vote{i+1}: "))
 if 1<=vote<=5:
 count[vote-1]+=1
 else:
 spoilt+=1
 print("\n Election Result: ")
 for i in range(5):
 print("conditate {i+1}: {count[i]}votes")
 print("spoilt Ballots :", spoilt)

 //develop an appliction with the following details://
 
n=int(input("Enter number of elements: "))
arr=[]
for i in range(n):
arr.append(int(input("Enter element{i+1}:" )))
max=abs(arr[0]-arr[1])
min=abs(arr[0]-arr[1])
for i in range(n):
for J in range(i+1,n):
diff=abs(arr[i]-arr[j])
if diff>max:
max=diff
elif diff<min:
min=diff
print("Maximum difference:", max)
print("Minimum difference:", min)

//write a numpy program to find the set difference between two arrays The set difference will return sorted distint values in array that are not in arrays

import numpy as np
array1=np.array([0,10,20,40,60,80]
array2=np.array([10,20,40,50,70,90])
result=np.array(sorted(set(array1)-set(array2)))
print("Array 1:",array1)
print("Array 2:",array2)
print("Set difference between two arrays:",result)

//Develop a program which takes 10 integer input user and state them in an array now copy all the elements in another array but in reverse order

arr1=[]
arr2=[]
print("Enter 10 integers: ")
for i in range(10):
    num=int(Input())
    arr1.append(num)
for i in range(9,-1,-1):
    arr2.append(arr1[i])
    print(arr1)
    print(arr2)