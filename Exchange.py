import gdax
from AccountStack import *
from MarketStack import *
from OrderStack import *

class Exchange:
	"""
	class represent the entire exchange
	hold markets list
	hold user list
	hold account list
	"""
	plc=gdax.PublicClient()
	def __init__(self):
		self.MarketStack= MarketStack(self)
		self.AccountStack= AccountStack(self)
		self.OrderStack= OrderStack(self)
		
