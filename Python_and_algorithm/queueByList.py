class queueByList(object):
	def __init__(self):
		self.queue = []

	def put(self,item):
		self.queue.append(item)
		return self.queue

	def get(self):
		return print(self.queue.pop(0))

	def size(self):
		return print(len(self.queue))

	def is_empty(self):
		return print(self.queue == [])

	def show(self):
		return print(self.queue)



if __name__ == '__main__':
	q=queueByList()
	q.put(2)
	q.put(3)
	q.size()
	q.is_empty()
	q.get()
	q.show()
	q.get()
	q.is_empty()
