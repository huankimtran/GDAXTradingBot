import Stack
import Market
class MarketStack(Stack.Stack):
	def __init__(self,exchange):
		Stack.Stack.__init__(self)
		self.Exchange=exchange
	def getMarket(self,marketName,updateTick=0.5,register=False):
		marketName=marketName.upper().replace(" ","")
		if hash(marketName) in self.Stack.keys():
			return self.Stack[haresh(marketName)]
		else:
			if register is True:
				return self.register(marketName,self.Exchange,updateTick)
			else:
				return None
	def register(self,marketName,updateTick=0.5,override=False):
		"""
		Create and add the market with marketName to the stack
		return a market
		"""
		marketName=marketName.upper().replace(" ","")
		if hash(marketName) in self.Stack.keys():
			if override is False:
				print("\nNo market created,a market with the same name is already in the stack\n")
				return self.Stack[hash(marketName)]
			else:
				print("\nMarket overriden,a market with the same name is already in the stack\n")
		self.Stack[hash(marketName)]=Market.Market(marketName,self.Exchange,updateTick)
		return self.Stack[hash(marketName)]