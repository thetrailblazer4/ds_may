# # f = open('demo_file.txt', 'r')

# # print(f.read())

# # f.close()

# # print(f.closed)


# with open('demo_file.txt', 'r') as f:

# 	for i in f:
# 		print(i, end='')
# 	# f_content = f.readline()
# 	# print(f_content, end='')

# 	# f_content = f.readline()
# 	# print(f_content, end='')

# 	# f_content = f.readline()
# 	# print(f_content, end='')

# 	# f_content = f.readline()
# 	# print(f_content, end='')
	



# # print(f.closed)


# with open('demofile.txt', 'w') as f:
# 	f.write('Demo')
# 	f.seek(0)
# 	f.write('Testing')
	# pass

with open('demo_file.txt', 'r') as rf:
	with open('demo_file_copy.txt', 'w') as wf:
		for line in rf:
			wf.write(line)