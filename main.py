# Python program to create an array of value provided by you
from array import *
arr=array('i',[] )
n=int(input("enter the array"))
for i in range(n):
    x=int(input("enter the value"))
    arr.append(x)
    print(arr )