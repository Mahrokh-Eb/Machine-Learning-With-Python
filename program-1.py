'''
Programmer: Mahrokh Ebrahimi
Discroption:Write a program to accept the food expenses of 3 Guests (one at a time). Using Accumulation concept, calculate and display the total expenses from all  3 guests combined. 
Date:6/29/2020

'''
guest1 = int(input('food expenses of guest1?'))
guest2 = int(input('food expenses of guest2?'))
guest3 = int(input('food expenses of guest3?'))

sum = guest1 + guest2 + guest3

print('total expenses from all  3 guests combined = ',sum )