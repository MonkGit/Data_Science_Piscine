import timeit

def get_gmails_with_loop():
    emails = ['john@gmail.com', 'james@gmail.com','alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com'] * 5 
    new_list = []

    for elem in emails:
        if elem[-9:] == 'gmail.com':
            new_list.append(elem)

    return (new_list)

def get_gmails_list_comprehension():
    emails = ['john@gmail.com', 'james@gmail.com','alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com'] * 5
    new_list = [element for element in emails if element[-9:] == 'gmail.com']


    return (new_list)

if __name__ == '__main__':
    
    iter_time = timeit.timeit(get_gmails_with_loop, number=90000000)
    comprehension_time = timeit.timeit(get_gmails_list_comprehension, number=90000000)
    if iter_time < comprehension_time:
        print('“it is better to use a loop')
        print(str(iter_time) + ' vs ' + str(comprehension_time))
    else:
        print('it is better to use a list comprehension')
        print(str(comprehension_time) + ' vs ' + str(iter_time))
 
    