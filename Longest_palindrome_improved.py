import sys
import time

def maxPalindrome(string):
   n=len(string)
   print(n)
   B = [ [0 for col in range(n) ] for row in range(n) ]
   F = [ [0 for col in range(n) ] for row in range(n) ]  #table to record true or false
   for i in range(n):
     B[i][0]= string[i]
     F[i][0]=1
   for k in range(1,n):
      for i in range(0,n-k):
       if k==1:
        if string[i]==string[i+1]:
         F[i][k]=1
         B[i][k]=string[i:i+k+1] 
        else:
         F[i][k]=0
         B[i][k]=  B[i+1][k-1]
       elif F[i][k-1]==1 and F[i+1][k-1]==1:
         B[i][k] =  string[i:i+k+1]             
         F[i][k]=1
       elif F[i][k-1]!=1 or F[i+1][k-1]!=1:
         if string[i]==string[i+k]:
          B[i][k]= string[i:i+k+1]
          F[i][k]=1
         else:
          F[i][k]=0
          B[i][k]=  B[i+1][k-1]
       elif  len(B[i][k-1])  >  len(B[i+1][k-1]) :
         B[i][k]= B[i][k-1]
       else:
         B[i][k]=  B[i+1][k-1]
   return( B[0][n-1])


string=input("Enter string here: ")
start = time.clock()
print("The longest palindrome in this string is:",maxPalindrome(string))
end = time.clock()
print("running time is ",end-start)
