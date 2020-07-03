'''
Programmer: Mahrokh Ebrahimi
Discroption:
 Write a program that asks for the names of three runners and the time it took each of them to ﬁnish a race. The program should display who came in ﬁrst, second, and third place. Think about how many test cases are needed to verify that your problem works correctly.
Date: 6/30/2020

'''

runner1 = input('runner 1?')
time1 = int(input('time?'))

runner2 = input('runner 2?')
time2 = int(input('time?'))

runner3 = input('runner 3?')
time3 = int(input('time?'))

if (time1 < time2):
    if (time1 < time3):
        print( 'runner-1 = '+runner1 + ' cames first ')
        if (time2 < time3):
            print( 'runner-2 = '+ runner2 + ' comes second')
            print('runner-3 = '+ runner3 + ' comes at the end')
        elif (time3 < time2):
            print( 'runner-3 = '+ runner3 + ' comes second')
            print('runner-2 = '+ runner2 + ' comes at the end')


elif (time2 < time1):
    if (time2 < time3):
        print( 'runner-2 = '+runner2 + ' cames first ')
        if (time1 < time3):
            print(runner1 +' comes second')
            print(runner3 +' comes third')
        elif (time3 < time1):
            print(runner3 +' comes second')
            print(runner1 +' comes third')
        
            
