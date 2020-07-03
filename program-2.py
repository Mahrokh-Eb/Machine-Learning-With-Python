'''
Programmer: Mahrokh Ebrahimi
Discroption: Write a program to ask the user to enter the amount spent on electricity and Gas bill for 3 consecutive months. Count and display the number of  months where the user went over budget if the electricity bill is over $45 dollars and Gas bill is over $30 dollars. 
Date:6/29/2020

'''
electricity1 = int(input('enter the amount spent on electricity-1'))
electricity2 = int(input('enter the amount spent on electricity-2'))
electricity3 = int(input('enter the amount spent on electricity-3'))

gas1 = int(input('enter the amount spent on gas-1'))
gas2 = int(input('enter the amount spent on gas-2'))
gas3 = int(input('enter the amount spent on gas-3'))

count = 0
if electricity1 > 45:
    count += 1
    
if electricity2 > 45:
    count += 1
    
if electricity3 > 45:
    count += 1
    
if gas1 > 30:
    count += 1
    
if gas2 > 30:
    count += 1

if gas2 > 30:
    count += 1
    
print('count= ', count)
    
    # TODO: write code...