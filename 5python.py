#!usr/bin/env python3

# Python problem set 5

#Q1 script to read a file

petty = open("Python_05.txt" , "r")
for lyr in petty:
   lyr = lyr.rstrip("\n")
   print (lyr.upper())

#Q2 modify script to write to new file

petty_read = open("Python_05.txt" , "r")
petty_write = open("Python_05_uc.txt", "w")
for lyr in petty:
  lyr = lyr.rstrip("\n")
  print (lyr.upper() + "\n")
petty_write.close()
print ("Wrote 'Python_05_uc.txt' ")



#Q3 open/print revcomp fasta seq

seq_in = open("Python_05.fasta", "r")
seq_out = open("Python_05_rc.txt", "w")
fasta ={}
def_gene = ""

for gene in seq_in:
   gene = gene.rstrip("\n")
   if gene.startswith(">"):
      def_gene = gene

   else:
      if def_gene in fasta:
         fasta[def_gene] += gene
      else:
         fasta[def_gene] = gene

for id in fasta:    #complement sequence
   comp = fasta[id].replace("A" , "t")
   comp = comp.replace("T" , "a")
   comp = comp.replace("G" , "c")
   comp = comp.replace("C" , "g")   #upper next
   comp = comp.upper()    #reverse
   rev_comp = comp[::-1]
   seq_out.write(id + "rev_comp\n" + rev_comp + "\n")

seq_out.close()
seq_in.close()
