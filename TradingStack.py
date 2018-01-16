from sets import *
from decimal import *
import gdax as plc
import Exchange
class TradeStack:
	"""
	This class is a container that holds the data of buy and sell on the market
	"""
	def __init__(self,Mk):
		"""
		self.Market is the market object that this TradeStack belongs to
		self.Total represent the sum of values of all sell and sum of buy of the Market
		self.TradeIDStack contains all the transaction ID to filter out new
		transaction from the newly updated data
		self.Data holds all the data of all the transaction. Each transaction
		is kept with an dictionary of structure : 
		{"time": "2014-11-07T22:19:28.578544Z"
		,"trade_id": 74,"price": "10.00000000"
		,"size": "0.01000000","side": "buy"}
		"""
		self.Market=Mk
		self.Total={'sell':Decimal('0'),'buy':Decimal('0')}
		self.TradeIDStack=Set()
		self.Data={'sell':[],'buy':[]}
	def onUpdate(self):
		#filter out new data from the data received from sever
		newData=filter(lambda x:x['trade_id'] not in self.TradeIDStack,self.getTrade())
		#add the transaction id into the TradeIDStack so that next time
		#the data will be recognized as old data
		map(self.TradeIDStack.add,map(lambda x:x['trade_id'],newData))
		#save the transaction data to self.Data
		map(lambda x:self.Data[x['side']].append(x),newData)
		#calculate the total amount of trade and sell
		def addUpTrade(x):
			self.Total[x['side']]+=(Decimal(x['price'])*Decimal(x['size']))
		map(addUpTrade,newData)
	def getTrade(self):
		return Exchange.Exchange.plc.get_product_trades(product_id=self.Market.MarketName)