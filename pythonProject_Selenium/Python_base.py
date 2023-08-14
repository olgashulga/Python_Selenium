#issue  1
a = int('123')
print("Value", a)

#issue 2
spam = 7
if spam > 5:
    print("five")
    if spam > 8:
        print("eight")
#FOR
for i in range(3):
    print('Hello!')

#for i in range(4):
        #number = eval(input('Enter a number:'))
        #print('The square of your number is:', number*

for i in range(1,5):
    print(i,'Good day!')
#Цикл while
#i = 0
#while i < 5:
        #i = i + 1
        #print(i, 'Value')
#break
#for i in range(1,10):
    #num = eval(input('Enter your number:'))
    #if num < 0:
        #break
#Function
n = int(input('Enter your number:'))
sum = 0
for num in range(1, n+1, 1):
    sum = sum + num
    print('Total', n, 'Value:', sum)
#List
nums = [1,2,3,4,5]
nums.insert(3,2)
print(nums[:4])
print(nums[3])