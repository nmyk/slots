import sys
import os
import machine

def CLI(slotMachine):
	playerInput = raw_input('Command: ')
	parsedCommands = playerInput.split()
	if len(parsedCommands) > 0:
		if parsedCommands[0] == 'bet':
			if len(parsedCommands) ==2:
				slotMachine.changeBet(int(parsedCommands[1]))
			else:
				print 'The current bet is $' + str(slotMachine.bet) + '.'
		elif parsedCommands[0] == 'balance':
			slotMachine.printBalance()
		elif parsedCommands[0] == 'add':
			slotMachine.addMoney(int(parsedCommands[1]))
		elif parsedCommands[0] == 'quit':
			sys.exit(0)
		elif parsedCommands[0] == 'help':
			os.system('clear')
			printHelp()
		else:
			os.system('clear')
			print 'Invalid command. Type "help" for options.'
	else:
		slotMachine.gamble()

def printHelp():
	print 'Commands:\n bet (#)\n balance\n help\n quit\n Press enter without issuing a command to pull the crank!'
	print """
	Combination                        Payout multiplier 
	----------------------------------------------------
	PINEAPPLE PINEAPPLE PINEAPPLE            500
	WATERMELON WATERMELON WATERMELON         250
	ORANGE ORANGE ORANGE                      80
	WATERMELON WATERMELON *any*               35
	ORANGE WATERMELON *any*                   15
	CHERRY CHERRY CHERRY                      10
	LEMON LEMON LEMON                          8 
	CHERRY CHERRY *any*                        5
	LEMON LEMON *any*                          2     

"""

def gameIntro():
	print """
    	
	
                  SLOTS! v1.0
            developed by Nick Mykins	

"""
