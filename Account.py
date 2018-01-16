from decimal import *
import time

class Account:
	def __init__(self,market,buyAcc=0,sellAcc=0):
		"""Ex:in BTC-USD if you have $2 and 1 BTC your buyAS=2 and your sellAS=1
		self.Balance: this account sell asset balance and buy asset balance
		Ex: for 'ETH-USD' sell balace is in ETH, buy balance is in USD
		self.Market: the market this account belongs to
		self.AccountID: the ID of this account in the AccountStack
		self.AccountORder: holds all the id of orders in the OrderStack 
		posted by this account"""
		self.Balance={'sell':Decimal(sellAcc),'buy':Decimal(buyAcc)}
		self.Market=market
		self.ID=hash(time.time())
		self.AccountOrder=[]
	def withdraw(self,subAcc,amount=0):
		if type(amount) is not Decimal:
			print(amount)
			amount=Decimal(amount)
		if self.Balance[subAcc]<amount:
			print("Account "+str(self.ID)+": no withdraw-Insufficient fund")
			return False
		else:
			self.Balance[subAcc]-=amount
			print("Account "+str(self.ID)+": withdraw successfully "+ str(amount) +" from "+subAcc+" balance")
			return True		
	def deposit(self,subAcc='sell',amount=0):
		if type(amount) is not Decimal:
			amount=Decimal(str(amount))
		self.Balance[subAcc]+=amount
		return self.Balance[subAcc]
	def postOrder(self,side,price,amount):
		return self.Market.Exchange.OrderStack.postOrder(self,side,price,amount)
	def cancelOrder(self,orderID=None,order=None):
		if order is not None:
			orderID=order.ID
		if self is not self.Market.Exchange.OrderStack[orderID].Account:
			print("\nAccount "+ self.ID+" has no permission to cancel this order\n")
			return False
		else:
			self.unregister(orderID,order)
			return True
	def postedOrderList(self):
		"""
		get the list of order posted by this account
		"""
		return filter(lambda x: self.Market.Exchange.OrderStack[x].Account is self ,self.Market.Exchange.OrderStack().keys())