import time
import decimal
class Order:
	def __init__(self,Account,side,price=0,amount=0):
		self.ID=hash(time.time())
		self.Account=Account
		self.Side=side
		self.Price=decimal.Decimal(price)
		self.Amount=decimal.Decimal(amount)
		self.Posted=False
	def post(self):
		return self.Account.Market.Exchange.OrderStack.postOrder(order=self)
	def cancel(self):
		return self.Account.Market.Exchange.OrderStack.destroyOrder(order=self)
	def fill(self):
		return self.Account.Market.Exchange.OrderStack.fillOrder(order=self)

