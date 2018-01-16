import Stack
import Order
from decimal import *
class OrderStack(Stack.Stack):
	"""
	This class represent a stack that holds all the orders from all the accounts
	in the market
	"""
	def __init__(self,exchange):
		Stack.Stack.__init__(self)
		self.Exchange=exchange
		
	def postOrder(self,Account=None,side='buy',price=0,amount=0,order=None):
		"""
		side will be the side where the order will resides
		Ex: if the want to buy 3 BTC with price of 3000 and you are in
		the market of 'BTC-USD', the side will be 'buy'
		"""
		if order is not None:
			if order.Posted is True:
				print("No order posted-order object might have been used")
				return -1
		else:
			if Account is None:
				print("No order is posted-no account was provided")
				return -1
			else:
				price=Decimal(price)
				amount=Decimal(amount)
				order=Order.Order(Account,side,price,amount)
		charge=False
		if side is 'buy':
			 charge=Account.withdraw(side,price*amount) 
		else:
			charge=Account.withdraw(side,amount)
		if charge is False:
			return -1
		else:
			if self.register(order) is False:
				return -1
			else:
				order.Posted=True
				print("\n"+order.Side.upper()+" order "+str(order.ID)+" from account "+str(order.Account.ID)+" is posted\n")
				return order.ID	

	def destroyOrder(self,orderID=None,order=None):
		"""take off the order from the stack"""
		self.unregister(orderID,order)

	def fillOrder(self,orderID=None,order=None):
		"""When the order is filled, the opposite sub account 
		will be deposit the amount of asset specified in the order 'amount'
		For example: if an order {'side':'sell','price':1500,'amount':2} is filled
		the Account.Balance['buy'] will be deposited an amount of
		price*amount"""
		#locate where the order resides
		if order is not None:
			orderID=order.ID
		side=self.Stack[orderID].Side
		amount=0
		#calculate the amount to deposit basing on the side of the order
		if side is 'sell':
			amount=self[orderID].Price*self.Stack[orderID].Amount
		else:
			amount=self[orderID].Amount
		#deposit to the opposite account, if buy order, deposit into sell account,and vice
		side=self.invertSide(side)
		self[orderID].Account.deposit(side,amount)
		#Take order off the stack
		print("\n"+order.Side.upper()+" order "+str(self[orderID].ID)+" of "+ str(self[orderID].Price) +" has been filled")
		self.destroyOrder(orderID)

	def isFilled(self,orderID=None,order=None):
		"""
		This function will check if an order can be filled or not
		In this beta state, the function will assume an order will be filled
		if ,in case of sell order, its price is lower than the lowest offer on the market
		or if, in case of buy order, its price is higher than the highest offer on the market 
		"""
		if order is None:
			order=self[orderID]
			bestOffer=order.Account.Market.OrderBook[self.invertSide(order.Side)][0][0]
		result=((order.Side is 'sell') is (bestOffer > order.Price)) and (bestOffer is not order.Price)
#		if order.Side is 'sell':
#			if order.Price < bestOffer:
#				return True
#		else:
#			if order.Price > bestOffer:
#				return True
		return result

	def onUpdate(self):
		"""
		This function is called every time a market get updated
		"""
		#fill all the order that satisfied
		for x in filter(self.isFilled,self().keys()):
			self[x].fill()

	def invertSide(self,side):
		if side is 'sell':
			return 'buy'
		else:
			return 'sell'