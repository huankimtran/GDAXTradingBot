import Stack
import time

class item:
	def __init__(self):
		self.ID=0
		self.value=time.time()
class test(Stack.Stack):
	def printOut(self):
		print(self.Stack)

a=item()
b=test()
b.register(a)
b.printOut()