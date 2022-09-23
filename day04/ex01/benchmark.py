import timeit

emails = ['john@gmail.com', 'james@gmail.com','alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com'] * 5

def get_gmails_with_loop():
    new_list = []

    for elem in emails:
        if elem[-9:] == 'gmail.com':
            new_list.append(elem)

    return (new_list)

def get_gmails_list_comprehension():
    new_list = [element for element in emails if element[-9:] == 'gmail.com']

    return (new_list)

def get_gmail_with_map():

    def find_gmails(x):
        if '@gmail.com' in x:
            return x

    return(map(find_gmails, emails))

    

if __name__ == '__main__':
 
    iter_time = timeit.timeit(get_gmails_with_loop, number=(9 * 10**7))
    comprehension_time = timeit.timeit(get_gmails_list_comprehension, number=(9 * 10 **7))
    map_time = timeit.timeit(get_gmail_with_map, number=(9 * 10**7))

    if iter_time < comprehension_time and iter_time < map_time:
        print('“it is better to use a loop')
    elif comprehension_time < iter_time and comprehension_time < map_time:
        print('it is better to use a list comprehension')
    else:
        print('it is better to use a map')
    sorted_result = sorted([iter_time, comprehension_time, map_time])
    print(str(sorted_result[0]) + ' vs ' + str(sorted_result[1]) + ' vs ' + str(sorted_result[2]))
   