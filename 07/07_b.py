# import csv

# # with open('copy_sample.csv', 'r') as csv_file:
# # 	data = csv.DictReader(csv_file, delimiter='\t')

# # 	for i in data:
# # 		print(i['email'])

# with open('sample.csv', 'r') as csv_file:
# 	data = csv.DictReader(csv_file)

# 	with open('new_copy_sample.csv', 'w') as new_file:
# 		fieldnames = ['first_name',	'last_name', 'email']
# 		new_data = csv.DictWriter(new_file, fieldnames, delimiter=',')

# 		new_data.writeheader()

# 		for i in data:
# 			new_data.writerow(i)