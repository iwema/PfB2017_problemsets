#Chapter 2 : Printing and manipulating text

# Calculating AT content

dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
A = dna.count("A")
T = dna.count("T")
length = len(dna)
AT_content  = (A + T) / length
print("The AT content is " + str(AT_content))
print("The DNA length is " + str( length))
print("A count is" , A)
print("T count is" , T)

#print("The sequence is this length:" + length) doesn't work b/c string and integer can't concatenate
#print("The sequence is this length" , length) works b/c not trying to concatenate a string and integer, they are separate entities here
#print("The sequence is this length" + str(length)) works b/c changed an integer to a string, which can concatenate w/ another string
#don't need to make strings if just giving a number and not doing anything else with it, e.g. last 2 print statements 

#-----

# Complementing DNA

dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
At = dna.replace ("A" , "t")
Ta = At.replace ("T" , "a")
Cg = Ta.replace ("C" , "g")
Gc = Cg.replace ("G" , "c")
print (dna)
print (At)
print (Ta)
print (Cg)
print (Gc)
print (Gc.upper())

#-----

# Restriction fragment lengths

dna = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
ecori_f = dna.find ("GAATTC") + 1  #cut site is bet G and A, so add 1 to count
ecori_e = len(dna) - ecori_f
print ("Length of the fragment before the EcoRI cut is" , ecori_f)
print ("Length of the fragment after the EcoRI cut is" , ecori_e)

#-----

# Splicing out introns, part one

dna = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
exon1 = dna[:64]  #1-63; needs to be one higher b/c str exclusive at end
intron = dna[64:91]  #start at 64 b/c str inclusive at start
exon2 = dna[91:]
print ("The first exon is here:" , exon1, ", the intron is here:" , intron, ", and the second exon is here:" , exon2)
print (len(dna))
print (len(exon1), len(intron), len(exon2))

#-----

# Splicing out introns, part two

len_ex1 = len(exon1)
len_ex2 = len(exon2)
coding = ((len_ex1 + len_ex2) / len(dna)) * 100
print (coding)

#-----

# Splicing out introns, part three

print (exon1, intron.lower(), exon2)  #this puts a space between each of the elements
print (exon1 + intron.lower() + exon2) #no spaces between elements

#-----

#Chapter 3 : Reading and writing files

#file_name = "/Users/admin/PfB2017_problemsets/Py4Bio_ex/reading_files/examples/dna.txt" #string, stores name of file
#file = open (file_name)  #file object, represents the file itself
#file_contents = file.read()  #string, stores text of file  # read ONLY works on file objects!
#print (file_contents)
#ACTGTACGTGCACTGATC #this is the output

dna_practice = open("/Users/admin/PfB2017_problemsets/Py4Bio_ex/reading_files/examples/dna.txt") #needed full file name to get to exact location
dna_read = dna_practice.read()  #have to do this to actually be able to read the contents of the file that was just opened; opening doesn't equal reading! 
print (dna_read)


#>>> repr(file_contents)   #this function shows a representation of the variable. including the new line
#"'ACTGTACGTGCACTGATC\\n'"
 
#-----

# Splitting genomic DNA

genomic_read = open("/Users/admin/PfB2017_problemsets/Py4Bio_ex/reading_files/exercises/genomic_dna.txt" , "r")
genomic = genomic_read.read()
exon1 = genomic[:64]  #1-63; needs to be one higher b/c str exclusive at end                                
intron = genomic[64:91]  #start at 64 b/c str inclusive at start
exon2 = genomic[91:]
genomic_coding = open("genomic_coding.txt" , "w")
genomic_noncoding = open("genomic_noncoding.txt" , "w")
gen_code = genomic_coding.write(exon1 + exon2)
gen_noncode = genomic_noncoding.write(intron)
genomic_read.close()
genomic_coding.close()
genomic_noncoding.close()

#-----

# Writing a FASTA file

header1 = "ABC123"
header2 = "DEF456"
header3 = "HIJ789"
seq1 = "ATCGTACGATCGATCGATCGCTAGACGTATCG"
seq2 = "actgatcgacgatcgatcgatcacgact"
seq3 = "ACTGAC-ACTGT--ACTGTA----CATGTG"
print (">" + header1, "\n" , seq1)
print (">" + header2, "\n" , seq2.upper())
print (">" + header3, "\n" , seq3.replace("-" , ""))

output = open ("seq.fasta" , "w")
output1 = output.write (">" + header1 + "\n" + seq1 + "\n")
output2 = output.write (">" + header2 + "\n" + seq2.upper() + "\n")
output3 = output.write (">" + header3 + "\n" + seq3.replace("-" , "") + "\n")

test_read = open("seq.fasta" , "r")
test = test_read.read()
print (test)

#-----

# Writing multiple FASTA files

out1 = open(header1 + ".fasta" , "w")
out2 = open(header2 + ".fasta" , "w")
out3 = open(header3 + ".fasta" , "w")

out1.write (">" + header1 + "\n" + seq1 + "\n")
out2.write (">" + header2 + "\n" + seq2.upper() + "\n")
out3.write (">" + header3 + "\n" + seq3.replace("-" , "") + "\n")

#-----

#Chapter 4 : Lists and loops

#file = open("some_input.txt")
#for line in file:
## do something with the line

#compare the above with the below--if you read the file rather than just open it, the for loop will go character by character, rather than line by line!

#file = open("some_input.txt")
#contents = file.read()
#for line in contents:
# warning: line contains just a single character!

#-----

# Processing DNA in a file

chapter4 = open("/Users/admin/PfB2017_problemsets/Py4Bio_ex/lists_and_loops/exercises/input.txt" , "r")
output = open("trimmed.txt" , "w")
for dna in chapter4:
   trimmed = dna[14:]
   output.write(trimmed)
   print ("Trimmed DNA with length " + str(len(trimmed)))
chapter4.close()
output.close()

#-----

# Multiple exons from genomic DNA

genomic_dna = open("/Users/admin/PfB2017_problemsets/Py4Bio_ex/lists_and_loops/exercises/genomic_dna.txt" , "r").read()
exons = open("/Users/admin/PfB2017_problemsets/Py4Bio_ex/lists_and_loops/exercises/exons.txt" , "r")

codingseq = "" 

for line in exons:
   positions = line.split(",")
   start = int(positions[0])
   stop = int(positions[1])
   exon = genomic_dna[start:stop]
   codingseq = codingseq + exon
print("The combined coding sequence is:" , codingseq)

output = open("genomic_exons.txt" , "w")
output.write(codingseq)
output.close()

#-----

#Chapter 5 : Writing our own functions

def get_at_content(dna, sig_figs):
   length = len(dna)
   a_count = dna.upper().count('A')
   t_count = dna.upper().count('T')
   at_content = (a_count + t_count) / length
   return round(at_content, sig_figs)

test_dna = "ATGCATGCAACTGTAGC"
print (get_at_content(test_dna, 1))
print (get_at_content(test_dna, 2))
print (get_at_content(test_dna, 3))

#write functions to do one job at a time; e.g. calculate something, then print something NOT calculate and print something!

#assertions are used to test whether our created function is behaving as expected.  A group of assertions is called a "test suite"  If the assertion isn't working, there will be an error, as it will not be true

#-----

# Percentage of amino acid residues, part one

def get_aa_percentage (protein, aa):

   #convert input to upper case, should input be submitted in lower

   protein = protein.upper()
   aa = aa.upper()

   aa_count = protein.count(aa)
   protein_length = len(protein)
   percentage = aa_count * 100 / protein_length
   return percentage

#test the function with assertions

assert get_aa_percentage("MSRSLLLRFLLFLLLLPPLP", "M") == 5
assert get_aa_percentage("MSRSLLLRFLLFLLLLPPLP", "r") == 10
assert get_aa_percentage("msrslllrfllfllllpplp", "L") == 50
assert get_aa_percentage("MSRSLLLRFLLFLLLLPPLP", "Y") == 0

#-----

# Percentage of amino acid residues, part two

protein = "MSRSLLLRFLLFLLLLPPLP"
aa_list = ['M', 'L', 'F']

# the "total" list  will contain counts for each of the matching aa's
total = 0

for aa in aa_list:
   print ("counting number of " + aa)
   aa = aa.upper()
   aa_count = protein.count(aa)

   #add number for this aa to the total count
   total = total + aa_count
   print("running total is " + str(total))

percentage = total * 100 / len(protein)
print ("final percentage is " + str(percentage))

#-----

def get_aa_percentage (protein, aa_list = ['A','I','L','M','F','W','Y','V']):
   protein = protein.upper()
   protein_length = len(protein)
   total = 0
   for aa in aa_list:
      aa = aa.upper()
      aa_count = protein.count(aa)
      total = total + aa_count
   percentage = total * 100 / protein_length
   return percentage

# test the function with assertions
assert get_aa_percentage("MSRSLLLRFLLFLLLLPPLP", "M") == 5
assert get_aa_percentage("MSRSLLLRFLLFLLLLPPLP", ["M" , "L"]) == 55
assert get_aa_percentage("msrslllrfllfllllpplp", ["F" , "L" , "S"]) == 70
assert get_aa_percentage("MSRSLLLRFLLFLLLLPPLP") == 65

#-----

#Chapter 6 : Conditional tests



