#!usr/bin/env python3

# Python problem set 5

#Q1 script to read a file

petty = open("Python_05.txt" , "r")
for lyr in petty:
   lyr = lyr.upper()
   print (lyr)

#Q2 modify script to write to new file

petty_read = open("Python_05.txt" , "r")
petty_write = open("Python_05_uc.txt")
for lyr in petty:
  lyr = lyr.upper()
  print (lyr)
print ("Wrote 'Python_05_uc.txt' ")



#Q3 open/print revcomp fasta seq

sequences = open("Python_05.fasta", "r")
for gene in sequences:
   print (gene)


rc_genes = {}

for gene in sequences:
   gene = gene.rstrip()
   id, seq = gene.split()

   rc_genes[id] = seq
sequences.close()
print(rc_genes)
  
fasta = open("Python_05.fasta" , "r")
sequences = {}
order = []
for seq in fasta:
    if seq.startswith('>'):
       name = seq[1:].rstrip('\n')
       order.append(name)
       sequences[name] = ''
    else:
       sequences[name] += seq.rstrip('\n').rstrip('*')
print (sequences)


