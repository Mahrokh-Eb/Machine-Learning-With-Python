'''
Programmer: Mahrokh Ebrahimi
 
Description:
  Modify the West LA College program so that the user enters the rate of tuition increase for the first year. The rate then increases by 0.5 percent each subsequent year.

Date: 7/10/2020
'''

print('West La College')
print()

tution = 15000
rate = int(input('Enter rate of tuition'))
tution = (tution * rate) + tution
print()
print( 'the tuition of first year, baased on the rate you entered is = ', tution)
print()

for i in range(2, 11):
    tution = (tution * .5) + tution
    print('for', i , 'year, tution =', tution)