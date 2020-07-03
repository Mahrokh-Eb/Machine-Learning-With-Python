'''
Programmer: Mahrokh Ebrahimi

Discroption:
write a program to ask 5 users for their gender and age. Print the total number of users that their age is under or 40 years old and are female or they are male and older than or 25 years old. 
Date: 6/30/2020

'''
gender_count_female = 0
gender_count_male = 0
age_count_under_forty = 0
age_count_older_twnty = 0
f = 20
m = 30

for i in range(3):
    gender = input('what is your gender? f/m')
    if (gender == f):
        gender_count_female += 1
    elif (gender == m):
        gender_count_male += 1
        
    age = int(input('how old are you?'))
    if (age < 41):
        age_count_older_twnty += 1
    if (age_count_older_twnty):
        age_count_older_twnty += 1
        
#  total number of users that their age is under or 40 years old and are female
x = age_count_under_forty + gender_count_female
print(' total number of users that their age is under or 40 years old and are female = ', x)

# they are male and older than or 25
y = age_count_older_twnty + gender_count_male
print('they are male and older than or 25 = ', y)

    