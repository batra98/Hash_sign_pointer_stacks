import random
from Crypto.Util import number
import gensafeprime


def generate_prime(n):
	if (n==2):
		p = 2
		g = 1
	elif (n==3):
	    p = 5
	    g = 2
	elif (n==4):
	    p = 11
	    g = 2
	elif (n==5):
	    p = 23
	    g = 11
	else:
		p = gensafeprime.generate(n)
		q = (p-1)//2

		t = 1
		while t == 1:
			h = number.getRandomRange(2,p-2)
			t = pow(h,2,p)

		g = h

	return (p,g)


class Node():
	def __init__(self,x):
		self.next = None
		self.data = x

class Stacks(object):
	def __init__(self):
		self.isEmpty = True
		self.head = None
		self.size = 0
		self.top = None
		self.stack = {}
		self.p,self.g = generate_prime(256)

	def push(self,x):
		pass

	def pop(self):
		pass

	def get_size(self):
		print(self.size)

	def get_top(self):
		print(self.top.data)

	def printstack(self):
		pass

	def Hashing(self,x,y,k):
		h = pow(self.g,x+k*y,self.p)
		return h

	def Signing(self,m):
		x = random.randrange(1,self.p,1)
		y = pow(self.g,x,self.p)
		r = random.randrange(1,self.p,1)
		t = pow(self.g,r,self.p)
		c = Hashing(t,m,y)
		z = c*x+r

		return t,z

	def printstack(self):
		temp = self.head


		if self.isEmpty == False:

			while self.stack[temp].next != None:
				print(self.stack[temp].data)
				temp = self.stack[temp].next 

			print(self.stack[temp].data)
		
		else:
			print()



class StacksPointer(Stacks):
	

	def push(self,x):

		if self.isEmpty == True:
			node = Node(x)
			self.stack[id(node)] = node
			self.top = node
			self.size = self.size+1
			self.isEmpty = False
			self.head = id(node)
		else:
			node = Node(x)

			temp = self.head

			while self.stack[temp].next != None:
				temp = self.stack[temp].next

			self.stack[temp].next = id(node)
			self.stack[id(node)] = node
			self.top = node
			self.size = self.size + 1

	def pop(self):

		if self.isEmpty == True:
			return
		else:
			temp = self.head

			if self.size != 1:
				while self.stack[self.stack[temp].next].next != None:
					temp = self.stack[temp].next

				self.stack.pop(self.stack[temp].next)
				self.stack[temp].next = None
				self.top = self.stack[temp]
			else:
				self.stack.pop(temp)
				self.head = None
				self.top = None
				self.isEmpty = True
			self.size = self.size - 1

	

	


class StacksHashPointer(Stacks):

	def push(self,x):
		c = self.Hashing(x,self.g,self.p)
		node = Node(x)
		if self.isEmpty == True:
			self.stack[(id(node),c)] = node
			self.top = node
			self.size = self.size+1
			self.isEmpty = False
			self.head = (id(node),c)
		else:
		
			temp = self.head

			while self.stack[temp].next != None:
				temp = self.stack[temp].next

			self.stack[temp].next = (id(node),c)
			self.stack[(id(node),c)] = node
			self.top = node
			self.size = self.size + 1

	def pop(self):

		if self.isEmpty == True:
			return
		else:
			temp = self.head

			if self.size != 1:
				while self.stack[self.stack[temp].next].next != None:
					temp = self.stack[temp].next

				self.stack.pop(self.stack[temp].next)
				self.stack[temp].next = None
				self.top = self.stack[temp]
			else:
				self.stack.pop(temp)
				self.head = None
				self.top = None
				self.isEmpty = True
			self.size = self.size - 1

# class StacksHashSignPointer(Stacks):
# 	def push(self,x):
# 		c = self.Hashing(x,self.g,self.p)
	








c = StacksHashPointer()
c.push(1)

c.pop()
c.push(1)
c.push(1)

c.pop()
c.push(1)
c.push(2)
c.push(3)
c.get_size()
c.get_size()
c.push(4)
c.get_top()
c.push(1)

c.pop()
c.push(1)

c.pop()
c.pop()
c.push(5)
c.printstack()

for keys in c.stack:
	print(keys)