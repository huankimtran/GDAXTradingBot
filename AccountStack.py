import Stack
from Account import *
class AccountStack(Stack.Stack):
	"""
	this class represents an account stack that hold all the accounts of
	a market, or a user
	"""
	def __init__(self,exchange):
		Stack.Stack.__init__(self)
		self.Exchange=exchange
	def newAccount(self,market,balcBuy=0,balcSell=0):
		acc=self.generateNew(Account,False,market,balcBuy,balcSell)
		if acc is not -1:
			print("Account "+str(acc.ID)+" has been created\nSell balace: "+str(balcSell)+"\nBuy balance: "+str(balcBuy)+"\n")
		return acc
