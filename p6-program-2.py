'''
Programmer: Mahrokh Ebrahimi
 
Description:
 Modify the West LA College program so that the user enters the rate of tuition increase instead of having it fixed at 4 percent. The rate then increases by 0.5 percent each subsequent year.

Date: 7/10/2020
'''
print('West La College')
print()

tution = 15000
rate = int(input('Enter rate of tuition'))

for i in range(1, 11):
    tution = (tution * rate) + tution
    print('for', i , 'year, tution =', tution)