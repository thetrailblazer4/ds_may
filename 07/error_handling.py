'''
FileNotFoundError
NameError
'''

try:
	f = open('newfile.txt')
	# new_var = old_var

except NameError as e:
	print(e)

except FileNotFoundError as e:
	print(e)

except Exception as e:
	print(e)

else:
	print(f.read())

finally:
	print('Executing....')