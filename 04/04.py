# def demo(greeting, name='You'):
# 	return f"{greeting} {name} message!"


# print(demo('Hi'))



def emp_info(*args, **kwargs):
	print(args)
	print(kwargs)


emp_info('python', 'Java', 'C', name='John', age=27)