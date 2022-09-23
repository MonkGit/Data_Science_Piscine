import timeit 
import random
from collections import Counter


def dict_from_list(list):
	dict_all = {}
	for element in list:
		if element not in dict_all:
			dict_all[element] = 1
		else:
			dict_all[element] += 1
	return dict_all

def my_top(list):
	my_dict = dict_from_list(list)
	sorted_list = sorted(my_dict.items(), key=lambda item: -int(item[1]))
	top_list = sorted_list[:10]
	my_top_dict = dict((x, y) for x, y in top_list)
	return my_top_dict

def counter_dict(list):
	return dict(Counter(list))

def counter_top(list):
	return Counter(list).most_common(10)

def my_time(func_name, list):
	times = timeit.timeit(lambda: func_name(list), number = 1)
	return times

if __name__ == '__main__':
	
	list = [random.randint(0, 100) for i in range(1000000)]
	try:
		print('my function:', my_time(dict_from_list, list))
		print('Counter:', my_time(counter_dict, list))
		print('my top:', my_time(my_top, list))
		print('Counter\'s top:', my_time(counter_top, list))
	except:
		raise Exception('Something went wrong')