import Exchange
from decimal import *

a=Exchange.Exchange()
mk=a.MarketStack.register('ETH-USD')
newAcc=mk.newAccount('1000000','100')
newAcc.postOrder('buy','1165.09','10')
newAcc.postOrder('sell','1168.00','10')