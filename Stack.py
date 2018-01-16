import time

class Stack:
	"""
	This class represent a container to hold all the element in which
	EACH ELEMENT HAS TO HAVE A FIELD 'ID' that holds the unique number which
	will be used to identify this element in this stack
	Field ID is a number return from the hash() function
	"""
	def __init__(self,*Elements):
		self.Stack={}
		#add initial accounts
		if len(Elements) is not 0:
			map(lambda x:self.Stack.update,map(lambda x: {x.ID:x},Elements))

	def register(self,element,override=False):
		"""
		if override is True, new element with the used id 
		can override old element in the stack
		"""
		if element.ID in self.Stack.keys():
			if override is False:
				print("Nothing got registered-overiding with no permission")
				return False
		self.Stack[element.ID]=element			
		return True

	def unregister(self,ID=None,Element=None):
		if Element is not None:
			ID=Element.ID
		if ID is not None:
			if ID in self.Stack.keys():
				del self.Stack[ID]
				return True
		return False

	def find(self,ID):
		return self.Stack[ID]

	def generateNew(self,elementType,override=False,*constructorPara):
		element=None
		if len(constructorPara) is not 0:	
			element=elementType(*constructorPara)
		else:
			element=elementType()
		if 'ID' not in dir(element):
			print('Non-compatible type. Type does not have field ID')
			return -1
		else:
			element.ID=hash(time.time())			
		self.register(element,override)
		return element
	def __call__(self):
		return self.Stack
	def __getitem__(self,index):
		return self.Stack[index]


