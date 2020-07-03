'''
Programmer: Mahrokh Ebrahimi
Discroption: Write a program using for loop to find the square of numbers from 1-10.

Hint: The operator for square is **

Sample Output:

 number          square
========================
   1             1
   2             4
   3             9
   4             16
   5             25
   6             36
   7             49
   8             64
   9             81
   10          100
Date:6/30/2020

'''
square = 1
for i in range(1, 11):
   print(i,'= ', end = '')
   square = i ** i 
   print(square)
   