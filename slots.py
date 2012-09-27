import cli
import reels
import machine
import os

def main():
	os.system('clear')
	slotMachine = machine.Machine(50,1)
	cli.gameIntro()
	cli.printHelp()
	slotMachine.printBalance()
	while True:
		if slotMachine.balance > 0:
			cli.CLI(slotMachine)
		else:
			slotMachine.isBroke()

if __name__ == '__main__':
	main()

