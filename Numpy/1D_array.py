import numpy as np
print("\nThe NUMPY version: ",np.__version__)

list1 = [1,2,3,4]
a1=np.array(list1)
a2=np.eye(3)
a3=np.arange(2,10,2)
a4=np.arange(1,10,2)
a5= np.arange(10,21)
a6=np.full((4,3),5)
a7=np.linspace(0,1,5)           # creates evenly spaced numbers btw a given range.
a8=np.ones((4,5))

print("\n1D array: ",a1)
print("\nIdentity Matrix: ",a2) 
print("\nEven Numbers: ",a3)
print("\nOdd Numbers: ",a4)
print("\nPrint a range of numbers: ",a5)
print("\nPrint same element: ",a6)
print("\nOutput of linspace: ",a7)
print("\nOutput: ",a8)


list1=[10,20,30,40]
array=np.array(list1,dtype=float)
array1=np.array(list1,dtype='U32')
print(array)
print(array1)


list1=[10,2.0,30,40,"hello"]
print(np.array(list1))
array=np.array(list1,dtype=object)
print(array)