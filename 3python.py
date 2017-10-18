#!usr/bin/env python3

#python problem set 3
#Q1 counting A & T

dna = 'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCTGTCCCTTCCCAGAAAACCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTCCCCTGCCCTCAACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGACAGAAACACTTTTCG'
print ('The DNA sequence is',dna)

A = dna.count ('A')
T = dna.count ('T')
print ('A =', A)
print ('T =', T)

#Q2 percentage GC

total_count = dna.count ('A') + dna.count ('T') + dna.count ('C') + dna.count ('G')

percent_GC_content = '{:.1%}'.format ((dna.count ('G') + dna.count ('C')) / total_count)

print ('The GC percentage is',percent_GC_content)

#Q3 reverse complement; remember to complement first!

compT2a = dna.replace ('T', 'a')
compA2t = compT2a.replace ('A', 't')
compG2c = compA2t.replace ('G', 'c')
compC2g = compG2c.replace ('C', 'g')

rev = compC2g [::-1]
REV = rev.upper()
print ('The reverse complement of the DNA sequence is:\n',REV)

#Q4 add/commit/push

#Q5 write a script to find EcoR1 start site in above seq

EcoR1 = 'GAATTC'
ecor1_loc = (dna.find ('GAATTC') + 1)

print ('The EcoR1 start position in this strand is',ecor1_loc)

#Q6 location of cut site, along with first/last NTs for each fragment

dna_loc = dna.split('GAATTC')

frag1 = dna_loc[0]
frag2 = dna_loc[1]

start_frag1 = frag1[0]
end_frag1 = frag1[-1]
print ('The first NT of DNA fragment 1 is',start_frag1, 'and the last is', end_frag1)

start_frag2 = frag2[0]
end_frag2 = frag2[-1]
print ('The first NT of DNA fragment 2 is',start_frag2, 'and the last is', end_frag2)

#Q7 fragment extraction and position in entire sequence and length

frag1_len = len(frag1)
frag2_len = len(frag2)
bothfrags = 'The first DNA fragment: {} is {} NTs long and the second fragment: {} is {} NTs long.'
finalfrag = bothfrags.format(frag1, frag1_len, frag2, frag2_len)

print (finalfrag)

# for Q7 didn't id the seq position, but moving on to other things

#Q8 create a list and add the fragments to it

frag_list = [frag1 , frag2]
print ('This is the list of both DNA fragments' , frag_list)

#Q9 sorted list

frag_list.sort()
print ('This is a sorted list of the fragments:' , frag_list)

#Q10 sorted by fragment length



