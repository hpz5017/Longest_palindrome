#!/usr/bin/env python
import sys
import time
def IsPalindrome(string):   
   n=len(string) 
   for i in range(n//2):
    if string[i] !=  string[n-i-1]:   
      return False
   return True

def maxPalindrome(string):
   n=len(string)
   print(n)
   B = [ [0 for col in range(n) ] for row in range(n) ]
   for i in range(n):
     B[i][0]= string[i]
   for k in range(1,n):
      for i in range(0,n-k):
       if IsPalindrome(string[i:i+k+1])==True:   #When slicing a string, ex:string[x:y],
         B[i][k] =  string[i:i+k+1]              #index x is included, but y is not included, if we need yth char, we should use y+1
       elif  len(B[i][k-1])  >  len(B[i+1][k-1]) :
         B[i][k]= B[i][k-1]
       else:
         B[i][k]=  B[i+1][k-1]
   return( B[0][n-1])

file=open('C:\\Users\\zhong\\Desktop\\python_algorithm\\test.txt','r')
string=file.read()
start = time.clock()
if IsPalindrome(string)==True:
     print("This is a palindrome")
else:
     print("This is not a palindrome \nThe longest palindrome in this string is:",maxPalindrome(string))
     end = time.clock()
     print("running time is ",end-start)

