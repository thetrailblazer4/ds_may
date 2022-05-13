prog_lang = ['Python', 'Java', 'C']


def find_index(to_search, target):
	for i, v in enumerate(to_search):
		if v == target:
			return i
	return 'Not Found!'

