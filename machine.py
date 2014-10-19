import sys
import os
import reels 

class Machine:

	def __init__(self,bal,coin):
		self.balance = bal
		self.bet = coin

	def print_balance(self):
		if self.balance > 0:
			print 'You have $' + str(self.balance) + ". Don't spend it all in one place."

	def add_money(self, amt):
		self.balance += amt

	def change_bet(self, bet):
		if bet <= self.balance:
			self.bet = bet
			print 'Bet changed to $' + str(bet) + "."
		else:
			print "You can't bet more money than is in the machine!"

	def gamble(self):
		if self.balance <= 0:
			self.is_broke()
		else:
			win = reels.spin()
			self.balance += self.bet * (win - 1)
			if win > 0:
				print "Woo! Woo! You won $" + str(win*self.bet) + "!\n"
				self.print_balance()
			else:
				print "Meh. Try again!\n"
				self.print_balance()
		if self.bet > self.balance > 0:
			print "Your wager now exceeds your balance. "
			self.change_bet(self.balance)
			
	def is_broke(self):
		print 'You have no more money! Get outta here!'
		sys.exit(0)
		

		

