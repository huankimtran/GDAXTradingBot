import gdax
import numpy
import threading
from sets import *
from decimal import *
from TradingStack import *
from OrderBook import *
from OrderStack import *
from AccountStack import *
class Market:
	def __init__(self,marketName,exchange,updateTick=0.5):
		"""
		id: the id of the Market ex: 'ETH-USD','BTC-USD',...
		updateTick: the time elapse between two call the the updateMarket function
		to draw the data from GDAX to update the current in this computer
		"""
		self.ID=hash(marketName)
		self.MarketName=marketName
		self.UpdateTick=updateTick
		self.Exchange=exchange
		self.OrderBook= OrderBook(self)
		self.TradeStack= TradeStack(self)
		self.MarketUpdateThread= threading.Timer(0,self.updateMarket)
		self.MarketUpdateThread.start()

	def updateMarket(self):
		while True:
			self.OrderBook.onUpdate()
			time.sleep(self.UpdateTick/3)
			self.TradeStack.onUpdate()
			time.sleep(self.UpdateTick/3)
			self.Exchange.OrderStack.onUpdate()
			time.sleep(self.UpdateTick/3)

	def __del__(self):
		self.MarketUpdateThread.cancel()

	def newAccount(self,balcBuy=0,balcSell=0):
		return self.Exchange.AccountStack.newAccount(self,balcBuy,balcSell)

