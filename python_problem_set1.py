#!/usr/bin/env python3
import sys

print ('Hello New York')
name = 'Carrie Iwema'
print (name)

color = 'black'
activity = 'rowing'
animal = 'octopus'
[ name, color, activity, animal ]
favorites = [ name, color, activity, animal ]
print (favorites)

{ 'name' : 'Carrie Iwema' , 'color' : 'black' , 'activity' : 'rowing' , 'animal' : 'octopus' }


fave = { 'name' : 'Carrie Iwema' , 'color' : 'black' , 'activity' : 'rowing' , 'animal' : 'octopus' }
print (fave)

name = sys.argv[1]
color = sys.argv[2]
activity = sys.argv[3]
animal = sys.argv[4]

print ('My name is', name)
print ('My favorite color is', color)
print ('My favorite new activity is', activity)
print ('My favorite animal is an', animal)
 
