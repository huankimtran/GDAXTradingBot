import gdax
import numpy
from decimal import *
from TradingStack import *
class OrderBook:
	"""
	Represent the orderbook of the market
	"""
	np=numpy
	plc=gdax.PublicClient()
	def __init__(self,mk,level=2):
		"""
		self.Market holds the market thsi order book belongs to
		self.Level indicates the amount of data receive
		1 means only the lowest sell and the highest buy
		2 means some other offers
		3 means the hold orderbook - might cause problem because of paging needed
		self.OrderBook holds the current data of the order book of the market
		"""
		self.Market=mk
		self.Level=level
		self.OrderBook=self.getMarketData(self.Level)
		
	def data2Float(self,dta,quick=False):
		"""dta has the structure of the data return from 
		the function gdax.PublicClient().get_product_order_book()
		if quick is True, all results will be in float,
		otherwise, Decimal will be used

		NOT USED ANYMORE
		"""
		rt={'bids':[],'asks':[]}
		for [price,sz,numb] in dta['bids']:
			if quick is False:
				rt['bids'].append([Decimal(price),Decimal(sz),Decimal(numb)])
			else:
				rt['bids'].append([float(price),float(sz),float(numb)])				
		for [price,sz,numb] in dta['asks']:
			if quick is False:
				rt['asks'].append([Decimal(price),Decimal(sz),Decimal(numb)])
			else:
				rt['asks'].append([float(price),float(sz),float(numb)])				
		return rt

	def marketDataParser(self,data,quick=True):
		"""data is the structure returned by the get_product_order_book method
			data structure returned from this method are two tupple representing the
		buy and sell order book.
		Both tupple have structure (price,size,numb-order,sum-size,sum-vl)
		the highest and lowest buy and sell offer respectively have index of 0"""
		rt={'bids':[],'asks':[]}
		for [price,sz,numb] in data['bids']:
			if quick is False:
				rt['bids'].append([Decimal(price),Decimal(sz),Decimal(numb)])
			else:
				rt['bids'].append([float(price),float(sz),float(numb)])				
		for [price,sz,numb] in data['asks']:
			if quick is False:
				rt['asks'].append([Decimal(price),Decimal(sz),Decimal(numb)])
			else:
				rt['asks'].append([float(price),float(sz),float(numb)])				
		Buy=[]	#[price,size,numb-order,sum-size,sum-vl]
		if quick is False:
			lastVL=Decimal(0)		
			sumsz=Decimal(0)
		else:
			lastVL=0		
			sumsz=0
		for [pr,sz,nb] in rt['bids']:
			lastVL=pr*sz+lastVL
			sumsz+=sz				
			Buy.append((pr,sz,nb,sumsz,lastVL)) 
								
		Sell=[]	#(price,size,numb-order,sum-size,sum-vl)
		if quick is False:
			lastVL=Decimal(0)		
			sumsz=Decimal(0)
		else:
			lastVL=0		
			sumsz=0
		for [pr,sz,nb] in rt['asks']:
			lastVL=pr*sz+lastVL
			sumsz+=sz				
			Sell.append((pr,sz,nb,sumsz, lastVL)) 
		return {'buy':Buy,'sell':Sell}

	def getMarketData(self,lv,quick=False):
	    return self.marketDataParser(OrderBook.plc.get_product_order_book(self.Market.MarketName,level=lv),quick=quick)
	
	def onUpdate(self):
		self.OrderBook=self.getMarketData(self.Level)
	def __call__(self):
		return self.OrderBook
	def __getitem__(self,index):
		return self.OrderBook[index]