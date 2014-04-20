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
		if count == 1:
			print roll 
		else:
			print roll, 
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

def single_dice_type(n_dice, n_dice_type):
	total = 0
	for x in range(n_dice):
		roll = randint(1, n_dice_type)
		total += roll
		print roll, 
	print "Total:", total

def dice_rolls(dicemode):
	#this is for rolling any number of dice
	modes = dicemode.split()
	for x in modes:
		print "Results for", x + ":",
		rocknroll = x.split('d')
		single_dice_type(int(rocknroll[0]), int(rocknroll[1]))

pool = 1
dicemode = 1

message = "Enter Mode: "
error = """ Valid inputs:
"S", "s", "shadowrun", "shadowrun dice pool", are all valid for calculating shadowrun dice pools.
Other valid inputs include: "2d6" or "4d6 2d20" or "d20" or something.
Enter '0' if you'd like to exit your mode or this program.
"""
while dicemode != '0':
	
	dicemode = raw_input(message)
	if dicemode == 's' or dicemode == 'S' or dicemode.find('hadow') > 0:
		while pool != 0:	
			pool = int(raw_input("Enter dicepool size: "))
			if pool == 0:
				break
			print "result: ", 
			hits = shadowrun_pool(pool)
			print hits, "hits occured."
		
	elif dicemode.find('d') > 0:
		#for ndm dice roll modes
		dice_rolls(dicemode)
					
	else:
		print "Invalid input. ", error
		
		

