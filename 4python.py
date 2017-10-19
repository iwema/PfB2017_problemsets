#!usr/bin/env python3

# this is the problem set from Python 4

#Q1 while loop 1 to 100

count = 0
while count < 100:
   count+=1
   print('count:' , count)

print ("That's all!")

#Q2 while loop factorial of 1000

num = 1000
fac = 1
i = 1

while i <= num:
   fac = fac * i
   i = i + 1
print ("The factoral of ", num, "is", fac)

#Q3 iterate list using for loop

numbers = [101,2,15,22,95,33,2,27,72,15,52]
for num in numbers:
    print(num)

numbers_iterator = iter (numbers)
next(numbers_iterator)

for num in numbers:
   if num % 2 == 0:
     print (num)

#Q4 sort above list, iterate and print, calculate, print
