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
