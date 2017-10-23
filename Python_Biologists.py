dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
A = dna.count("A")
T = dna.count("T")
length = len(dna)
AT_content  = (A + T) / length
print("The AT content is", str(AT_content))
print("The DNA length is" ,str( length))
print("A count is" , str(A))
print("T count is" , str(T))

#print("The sequence is this length:" + length) doesn't work b/c string and integer can't concatenate
#print("The sequence is this length" , length) works b/c not trying to concatenate a string and integer, they are separate entities here
#print("The sequence is this length" + str(length)) works b/c changed an integer to a string, which can concatenate w/ another string
-----



