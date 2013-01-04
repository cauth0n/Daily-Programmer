#!/usr/bin/python
from random import randint

chosen =  randint(1, 100)#random 
print "C> Welcome to guess-that-numbers game! I have already picked a number in [1, 100]. Please make a guess. Type \"exit\" to quit."
while True:
	userIn = raw_input('U> ')
	if userIn == "exit":
		print "Thank you for playing!"
		break
	userIn = int(userIn)
	if userIn == chosen:
		print "C> Correct! That is my number. you win! <Program terminates>"
		break
	elif userIn < chosen:
		print "C> Wrong. That number is below my number."
	elif userIn > chosen:
		print "C> Wrong. That number is above my number."

