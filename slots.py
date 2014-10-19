import cli
import reels
import machine
import os


def main():
	os.system('clear')
	slot_machine = machine.Machine(50,1)
	cli.game_intro()
	cli.print_help()
	slot_machine.print_balance()
	while True:
		if slot_machine.balance > 0:
			cli.CLI(slot_machine)
		else:
			slot_machine.is_broke()


if __name__ == '__main__':
	main()

