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


#Q4  fastq line count, char num/line, len

fastq = open("Python_05.fastq", "r")

lines = 0
chars = 0

for line in fastq:
   line = line.rstrip("\n")
   lines += 1
   chars += len(line)

fastq.close()

avg_line_len = chars / lines

print ("# of lines =" , lines)
print ("# of characters =" , chars)
print ("average line length =" , avg_line_len)

#Q5  generate gene lists saved in files, add to sets, compare


alpaca_all = open ("/Users/admin/Desktop/alpaca_all_genes.tsv" , "r") 
alpaca_stem = open ("/Users/admin/Desktop/alpaca_stemcellproliferation_genes.tsv" , "r") 
alpaca_pigment = open ("/Users/admin/Desktop/alpaca_stemcellpigmentation_genes.tsv", "r") 

al_all = set()
al_stem = set()
al_pigment = set()

for seq in alpaca_all:
   seq = seq.rstrip("\n")
   if seq.startswith("Gene"):
      continue
   else:
      al_all.add(seq)

for seq in alpaca_stem:
   seq = seq.rstrip("\n")
   if seq.startswith("Gene"):
      continue
   else:
      al_stem.add(seq)

for seq in alpaca_pigment:
   seq = seq.rstrip("\n")
   if seq.startswith("Gene"):
      continue
   else:
      al_pigment.add(seq)

not_stem = al_all - al_stem
both_go = al_stem & al_pigment

for stem_pig in both_go:
   print (stem_pig)

alpaca_all.close()
alpaca_stem.close()
alpaca_pigment.close()


alpaca_stem = open ("/Users/admin/Desktop/alpaca_stemcellproliferation_genes.tsv" , "r")
alpaca_tf = open ("/Users/admin/Desktop/alpaca_transcriptionFactors.tsv" , "r")


al_stem = set()
al_tf = set()

for seq in alpaca_stem:
   seq = seq.rstrip("\n")
   if seq.startswith("Gene"):
      continue
   else:
      al_stem.add(seq)

for seq in alpaca_tf:
   seq = seq.rstrip("\n")
   if seq.startswith("Gene"):
      continue
   else:
      al_tf.add(seq)

stem_tf = al_stem & al_tf

for tf_pro in stem_tf:
   print (tf_pro)

alpaca_stem.close()
alpaca_tf.close()

# didn't finish Q5, the command line part
