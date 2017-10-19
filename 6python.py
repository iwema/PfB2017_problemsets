# Python problem set 6

#Q1 find occurrences of Nobody in the poem

#!usr/bin/env python3

import re

shel = open ('Python_06_nobody.txt' , 'r')

poem = shel.read()

print (poem)

for item in re.finditer (r"Nobody" , poem):
    print("Nobody location:" , item.start(), "-" , item.end())


#Q2 replace Nobody with name, and output


shel = open ('Python_06_nobody.txt' , 'r')
poem = shel.read()
rob = re.sub(r"Nobody" , "Rob" , poem)
print (rob)
shel_write = open("Rob.txt" , "w")
shel_write.write(re.sub(r"Nobody" , "Rob" , poem))
print("wrote 'Rob.txt'")

#Q3 fasta pattern matching

histones = open ('Python_06.fasta.1' , 'r')
hisseq = histones.read()
for header in re.finditer(r">.+$, hisseq, re.M):
   print(header)




