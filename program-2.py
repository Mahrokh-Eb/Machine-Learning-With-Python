'''
Programmer: Mahrokh Ebrahimi
Discroption:Write a program using for loop to find the total sum of numbers 1-20. Use accumulation concept.
Date: 30/6/2020
'''
count = 0
for i in range(1, 21, 1):
    print(i, end =' ')
    count += i
    print('sum = ', count)

print() 
print('---------------------------------------------------')    
print('while loop:')

count = 0   
sum = 0
while (count <= 20):
    print(count, end =' ')
    sum = sum + count
    print('sum = ', sum)
    count +=1
    
    
    