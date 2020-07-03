'''
Programmer: Mahrokh Ebrahimi

Description:
Write a Python program that calculates the discounted price of an item using the if-elif-else statement.

Your conditions are as follows:

If the price is 300 or above, it will be discounted by 30%
If the price falls between 200 and 300, it will be discounted by 20%
If the price falls between 100 and 200, it will be discounted by 10%
If the price is less than 100, it will be discounted by 5%
There is no discount for negative prices

Date: 6/22/2020 
'''
price = float(input('Please enter the price'))

if price>0:
    if price >= 300:
        price -= price * 30/100
        print(price)
        
    elif 200< price <300:
        price -= price * 20/100
        print(price)
    
    
    elif 100< price <200:
        price -= price * 10/100
        print(price)
    
    
    elif  price <100:
        price -= price * 5/100
        print(price)
    
    
print('Done!')
    
    
    

