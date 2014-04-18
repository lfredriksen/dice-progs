from random import randint

def shadowrun_pool(dicepool):
	#solely for counting hits above a threshold for shadowrun
	#dicepool is the amount of dice you use on this roll
	count = dicepool
	hits = 0
	ones = 0
	while count > 0:
		roll = randint(1, 6)
		#shadowrun rules use d6s, and a hit is a 5. 1s should be counted as well
		if roll >= 5:
			hits += 1
		elif roll == 1:
			ones += 1
		count -= 1
		
	if ones >= float(dicepool)/2:
		if hits == 0:
			print "CRITICAL GLITCH!", ones, "ones occured.",
			#this occurs when half or more of your dicepool results in 1s and
			#you have no hits
		else: 
			print "Glitch occurred.", ones, "ones occured.",
			#this occurs when half or more of your dicepool results in 1s but 
			#you have hits.
	return hits

def dice_rolls(dicepool):
	#this is for rolling any number of dice

pool = 1
dicemode = 1

message = "Enter Mode: "
error = """ Valid inputs:
"S", "s", "shadowrun", "shadowrun dice pool", are all valid for calculating shadowrun dice pools.
Other valid inputs include: "2d6" or "4d6 2d20" or "d20"
"""
while dicemode != '0':
	
	dicemode = raw_input(message)
	if dicemode == 's' or 'S':
		while pool != 0:	
			pool = int(raw_input("Enter dicepool size: "))
			print "result: ", shadowrun_pool(pool), " hits occured."
	elif dicemode == '6':
		
	else:
		print "Enter valid input!", error
		

