'''
Programmer: Mahrokh Ebrahimi
 
Description:
1-  Design a program for West LA College. Assume the current tuition is $15,000 per year, and tuition is expected to increase by 4 percent each year. Display the tuition each year for the next 10 years.

Date: 7/8/2020
'''
print('West La College')
print()
tution = 15000

for i in range(1, 11):
    tution = (tution *.04) + tution
    print('for', i , 'year, tution =', tution)
    