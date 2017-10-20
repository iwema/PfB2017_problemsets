#!usr/bin/env python3

# this is the problem set from Python 4

#Q1 while loop 1 to 100

count = 1
while count <= 100:
   print('count:' , count)
   count += 1

print ("That's all!")

#Q2 while loop factorial of 1000

num = 1000
fac = 1000

while num > 1:
   num -= 1
   fac *= num
 
print ("The factoral of ", num, "is", fac)

#Q3 iterate list using for loop

numbers = [101,2,15,22,95,33,2,27,72,15,52]
for num in numbers:
   if num % 2 == 0: #this means even
      print(num)


#Q4 sort above list, iterate and print, calculate sum, print both sums

numbers = [101,2,15,22,95,33,2,27,72,15,52]
odds = []
evens = []

for num in numbers:
   if num % 2 == 0:
      evens.append(num)
   else:
      odds.append(num)

all_even = 0
all_odd = 0
for even in evens:
   all_even += even
for odd in odds:
   all_odd += odd

print ("even sum is" , all_even)
print ("odd sum is" , all_odd)

#Q5 use pop and remove with integer list

numbers = [101,2,15,22,95,33,2,27,72,15,52]
print (numbers)  #[101, 2, 15, 22, 95, 33, 2, 27, 72, 15, 52]
numbers.pop() #52
popnum = numbers.pop()
print (numbers, popnum)  #[101, 2, 15, 22, 95, 33, 2, 27, 72] 15
print (numbers, numbers.pop())  #[101, 2, 15, 22, 95, 33, 2, 27] 72

remnum = numbers.remove(95)
print (numbers, remnum)  #[101, 2, 15, 22, 33, 2, 27] None #doesn't show removed number like pop

#Q6  write script using range in for loop to print numbers 0-99

for number in range(100):
   print (number)

#Q7  write loop using range to print 1-100

for number in range(1,101):
   print (number)

#Q8  rewrite script to take start end values from command line

import sys

start = int(sys.argv[1])
end = int (sys.argv[2])

for number in range(start, end + 1):
   print (number, end=' ')

#Q9 modify script to print only odd

import sys

start = int(sys.argv[1])
end = int (sys.argv[2])

for number in range(start, end + 1):
   if number % 2 == 0: #this means even
      continue
   else:
      print (number, end = ' ')

#Q10  make list, use for loop to iterate and print element, length, sequence

sequences = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']
for seq in sequences:
   print (len(seq), "\t", seq)

#Q11  rewrite 10 using list comprehension to generate list of tuples of seq and len, print both

sequences = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']

lens = [(len(seq), seq) for seq in sequences]

for tuples in lens:
   print (tuples[0], "\t", tuples[1])

#Q12  modify 10 to also print number of each sequence

sequences = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']
count = 1
for seq in sequences:
   print (count, "\t", len(seq), "\t", seq) 
   count+= 1

#Q13  create shuffled sequence   #this is very confusing, not sure I would know how to do this

import random

sequence = "ATTGC"
length = len(sequence)
shuffle = length
seq_list = list(sequence)

while shuffle > 0:
   ran1 = random.randrange (0, length -1, 1)
   ran2 = random.randrange (0, length -1, 1)

   nt1 = seq_list[ran1]
   nt2 = seq_list[ran2]

   seq_list[ran2] = nt1
   seq_list[ran1] = nt2

   shuffle -= 1

print("".join(seq_list))


#Q14  2 DNA seq, align, output fasta, store separate, remove newlines, use for loop with range, report %



