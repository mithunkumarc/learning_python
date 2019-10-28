class Queue:
	def __init__(self):
		self.items = []

	def enqueue(self,element):
		self.items.insert(0, element)

	def dequeue(self):
		return self.items.pop()


myqueue = Queue()
myqueue.enqueue(3)
myqueue.enqueue(4)
myqueue.enqueue(5)
print(myqueue.items)
print(myqueue.dequeue())
print(myqueue.items)