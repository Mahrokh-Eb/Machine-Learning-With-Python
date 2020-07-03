'''
Programmer: Mahrokh Ebrahimi

Description:
Program 3: 
Write a program to:
Ask the student for  3 exam scores.
Calculate the average score.
Using a bunch of IF conditions, the computer should determine the grade and display the grade to the user.
Use the following Criteria:
 If Average is 98-100… Assign the grade “A+”
 If Average is 95-97… Assign the grade “A”
 If Average is 91-94… Assign the grade “A-”
If Average is 88-90… Assign the grade “B+”
 If Average is 84-87… Assign the grade “B”
 If Average is 80-83… Assign the grade “B-”
If Average is 75-79… Assign the grade “C+”
 If Average is 70-74… Assign the grade “C”
 If Average is less than 70 and greater than 60 assign grade “D”
 If Average is less than or equal 60 assign grade "NC"

Display the student name 
Display the Average score and letter grade back to the student.

Date: 6/22/2020 

'''
studentName = input('student name?')
score1 = float(input('score-1?'))
score2 = float(input('score-2?'))
score3 = float(input('score-3?'))

average = (score1 + score2 + score3) / 3
str(average)

if 97< average <=100:
    print(studentName)
    print('Average score= ', average)
    print('A+')
    
elif 95<= average <=97:
    print(studentName)
    print('Average score= ', average)
    print('A')
    
elif 91<= average <=94:
    print(studentName)
    print('Average score= ', average)
    print('A-')
    
elif 88<= average <=90:
    print(studentName)
    print('Average score= ', average)
    print('B+')

elif 84<= average <=87:
    print(studentName)
    print('Average score= ', average)
    print('B')
    
elif 80<= average <=83:
    print(studentName)
    print('Average score= ', average)
    print('B-')
    
elif 75<= average <=79:
    print(studentName)
    print('Average score= ', average)
    print('C+')
    
elif 70<= average <=74:
    print(studentName)
    print('Average score= ', average)
    print('C')
    
elif 60< average <70:
    print(studentName)
    print('Average score= ', average)
    print('D')
    
else:
    print(studentName)
    print('Average score= ', average)
    print('NC')
    