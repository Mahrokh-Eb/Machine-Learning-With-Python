'''
Programmer: Mahrokh Ebrahimi

Description: Write a program to collect the following data from the user.
1)    User last name
2)    User First Name
3)    Number of Hours worked.
4)    Hourly-wage
 
Calculate the gross wage based on the formula:
Gross wage is number of hours worked multiplied by hourly-wage.
Hint: You use the symbol * for multiplication.

Output: Display the user name and gross wage.

Date: 6/22/2020 
'''
lastName = input('User last name ?')
firstName = input('User First name ?')
numberHours = float(input('Number of Hours worked ?'))
hourlyWage = round(float(input('Hourly-wage ?')))

gross = 0
gross += numberHours * hourlyWage
print(' first name =', firstName,' ,last name =', lastName, ' ,gross income =', gross)

