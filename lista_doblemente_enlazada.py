
class Node(object):
	def __init__(self, value):
		self.previousNode = None
		self.nextNode = None
		self.value = value

def CreateList():
	return Node(0)

def AddNode(initialNode, newNode ):
	if (initialNode.value == newNode.value):
		newNode.nextNode = initialNode.nextNode
		newNode.previousNode = initialNode
		initialNode.nextNode = newNode

	elif(initialNode.value > newNode.value):
		if (initialNode.previousNode != None):
			if (initialNode.previousNode.value <= newNode.value):
				newNode.nextNode = initialNode
				newNode.previousNode = initialNode.previousNode
				initialNode.previousNode = newNode
				initialNode.previousNode.nextNode = newNode
			else:
				AddNode(initialNode.previousNode, newNode)

		else:
			newNode.nextNode = initialNode
			initialNode.previousNode = newNode			
	else:
		if (initialNode.nextNode != None):
			if (initialNode.nextNode.value >= newNode.value):
				newNode.nextNode = initialNode.nextNode 
				newNode.previousNode = initialNode
				initialNode.nextNode = newNode
				initialNode.nextNode.previousNode = newNode
			else:
				AddNode(initialNode.nextNode, newNode)
				
		else:
			initialNode.nextNode = newNode
			newNode.previousNode = initialNode


def FindFirst(initialNode):
	if (initialNode.previousNode != None):
		return	FindFirst(initialNode.previousNode)
	else:
		return initialNode

def ListNodes(initialNode):
	print(initialNode.value)
	if (initialNode.nextNode != None):
		ListNodes(initialNode.nextNode)
				
initialNode = CreateList()
AddNode(initialNode, Node(0))
AddNode(initialNode, Node(1))
AddNode(initialNode, Node(80))
AddNode(initialNode, Node(5))
AddNode(initialNode, Node(-1))

ListNodes(FindFirst(initialNode))