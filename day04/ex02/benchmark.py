import timeit
import sys

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

def find_gmails(x):
        if '@gmail.com' in x:
            return x

def get_gmail_with_map():

    return(map(find_gmails, emails))

def get_gmail_with_filter():
    
    return(filter(find_gmails, emails))

if __name__ == '__main__':
    if len(sys.argv) == 3:
        try:
            x = int(sys.argv[2])
            if sys.argv[1] == 'map':
                print(timeit.timeit(get_gmail_with_map, number=x))
            if sys.argv[1] == 'list_comprehension':
                print(timeit.timeit(get_gmails_list_comprehension, number=x))
            if sys.argv[1] == 'loop':
                print(timeit.timeit(get_gmails_with_loop, number=x))
            if sys.argv[1] == 'filter':
                print(timeit.timeit(get_gmail_with_filter, number=x))
        except:
            raise Exception ('Something went wrong')