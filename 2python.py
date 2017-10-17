#!/usr/bin/env python3
import sys

dna = 'CTAAAATACCCTAGGGGAGATGCCGCTATAGGTCGGTATAGGG'
if 'AAA' in dna :
	print ('AAA present')
else :
	print ('AAA NOT present')
if 'TTT' in dna :
	print ('TTT present')
else :
        print ('TTT NOT present')
if 'CCC' in dna :
	print ('CCC present')
else :
        print ('CCC NOT present')
if 'GGG' in dna :
	print ('GGG present')
else :
        print ('GGG NOT present')
if 'ATC' in dna :
	print ('ATC present')
else :
        print ('ATC NOT present')
if 'TCG' in dna :
	print ('TCG present')
else :
        print ('TCG NOT present')
if 'CGA' in dna :
	print ('CGA present')
else :
        print ('CGA NOT present')
if 'GAT' in dna :
	print ('GAT present')
else :
        print ('GAT NOT present')


#dna = sys.argv[1]
#codon = sys.argv[2]

#if codon in dna :
#	message = "is in your DNA seqence."
#	print (codon, message)
#if codon not in dna :
#	message = 'is NOT in your DNA sequence.'
#	print (codon, message)



number = float (sys.argv[1])

if number >= 0 :
	message = 'is positive'
	print (number, message)
	
	if number > 50 :
		message = 'is bigger than 50'
		print (number, message)

		if number % 3 == 0 :
			message = "is divisible by 3"
			print (number, message)
	elif number < 50 :
		message = 'is smaller than 50'
		print (number, message)

		if number % 2 == 0 :
			message = "is an even number"
			print (number, message)
	elif number == 50 :
		message = 'is equal to 50'
		print (number, message)

else :
	message = 'is negative'
	print (number, message)
