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

with open ("Python_06.fasta", "r") as Histones:
   sequences = Histones.read()
   sequences = re.split("^>", sequences, re.M)
   del sequences[0]
   Histones.close()
print("Converting FASTA file from multiline to single line and writing to file.")
with open ("Histones_saved", "w") as newFasta:
   for fasta in sequences:
      header, sequence = fasta.split("\n", 1)
      header = ">" + header + "\n"
      sequence = sequence.replace("\n","")
      newFasta.write(header + sequence)
   newFasta.close()
print(">>Done!")



