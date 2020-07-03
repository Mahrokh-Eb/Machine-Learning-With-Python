'''
Programmer: Mahrokh Ebrahimi
Discroption: Write a program that allows the user to enter values for a salesperson’s base salary, total sales, and commission rate. The program computes and outputs the salesperson’s pay by adding the base salary to the product of the total sales and commission rate. 
Date:6/28/2020
'''

baseSalary = int(input('what is your base salery?'))
totalSales = int(input('what is your total sales?'))
comissionRate = int(input('what is your comission rate?'))

#product of the total sales and commission rate
p = totalSales * comissionRate

#adding base salary
result = p + baseSalary

print(result)
