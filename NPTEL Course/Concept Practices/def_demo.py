x = 200			#global scope
def f1():
	a = 10
	b = a + 20
	print(b)
	b = b + x	# x is looked up in local scope. As not present, it is looked up globaly where it is found.
	print(b)
f1()
def f2():
	b = "hello"	# as b's life was local upto f1(), we can again use it here
	print(b)
	def f3():
		c = " world"
		d = b + c	# here b is looked up in enclosing scope after not finding it locally
		print(d)
		y = str(x) + " is the new global result"
		print(y)
	f3()
f2()