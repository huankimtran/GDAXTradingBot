import gdax

plc= gdax.PublicClient()
USDMarket={'BCH':'BCH-USD','BTC':'BTC-USD'}
BTCMarket={'BCH':'BCH-BTC'}
def getUSDRate(self,productName):
	price=self.plc.get_product_order_book(USDMarket[productName],level=1)
	return price
def getBTCRate(self,productName):
	price=self.plc.get_product_order_book(BTCMarket[productName],level=1)
	return price
def buyWhat(self,productName):
	USDBTCRate=self.getUSDRate('BTC')
	USDMarketRate=self.getUSDRate(productName)
	BTCMarketRate=self.getBTCRate(productName)
	if BTCMarketRate > USDMarketRate
