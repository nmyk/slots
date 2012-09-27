import time

# By changing the "pictures" on the reel, you can make the slot machine whatever theme you want. For example, reel = ['CHAT','CHIEN','ARBRE','MAISON','VILLE','MERDE'] has a French theme.

reel = ['LEMON','CHERRY','ORANGE','WATERMELON','PINEAPPLE','GARBAGE']

def spin(A,B,C):
	reelPics = ['','','']
	reelList = [A,B,C]
	payout = 0

# The probabilities of getting the six pictures are 30%, 25%, 15%, 10%, 5%, and 15%, respectively.
	for i in range(0,3):
		if reelList[i] < 5:
			reelPics[i] = reel[4]
		elif 5 <= reelList[i] < 15:
			reelPics[i] = reel[3]
		elif 15 <= reelList[i] < 30:
			reelPics[i] = reel[2]
		elif 30 <= reelList[i] < 55:
			reelPics[i] = reel[1]
		elif 55 <= reelList[i] < 85:
			reelPics[i] = reel[0]
		elif reelList[i] > 85:
			reelPics[i] = reel[5]
    # Pause in between pictures for suspense!
	print 20*' ' + reelPics[0]
	time.sleep(.4)
	print 20*' ' + reelPics[1]
	time.sleep(.4)
	print 20*' ' + reelPics[2] + '\n'
	time.sleep(.2)
	
	# Various payout schemes. Edit these to your heart's content.
	if reelPics == [reel[4],reel[4],reel[4]]:
		payout = 500
	elif reelPics == [reel[3],reel[3],reel[3]]:
		payout = 250
	elif reelPics == [reel[2],reel[2],reel[2]]:
		payout = 80
	elif reelPics[0] == reelPics[1] == reel[3] and reelPics[2] != reel[3]:
		payout = 35
	elif reelPics[0] == reel[2] and reelPics[1] == reel[3]:
		payout = 15
	elif reelPics == [reel[1],reel[1],reel[1]]:
		payout = 10
	elif reelPics == [reel[0],reel[0],reel[0]]:
		payout = 8
#	elif reelPics[0] == reel[4] and reelPics[2] != reel[4]:
#		payout = 20
	elif reelPics[0] == reelPics[1] == reel[1] and reelPics[2] != reel[1]:
		payout = 5
#	elif reelPics[0] == reel[3] and reelPics[2] != reel[3]:
#		payout = 10
#	elif reelPics[0] == reel[2] and reelPics[2] != reel[2]:
#		payout = 5
#	elif reelPics[0] == reel[1] and reelPics[1] != reel[1] and reelPics[2] != reel[1]:
#		payout = 1
	elif reelPics[0] == reelPics[1] == reel[0] and reelPics[2] != reel[0]:
		payout = 2
	return payout
