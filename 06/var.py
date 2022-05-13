# LEGB --> Local, Enclosing, Global, Builtin

# x = 'global x'

# def demo(z):
# 	x = 'local x'
# 	print(z)


# demo('local z')

# print(z)
		
# import builtins

# print(dir(builtins))


# num = [7,3,1,3,4,6,2]

# def max():
# 	pass

# print(max(num))

x = 'global x'

def outer():
	x = 'outer x'

	def inner():
		x = 'inner x'
		print(x)

	inner()
	print(x)

outer()
print(x)
