
class Research:

    def file_reader():
        with open('data.csv', 'r') as file_to_read:
            return(file_to_read.read())

if __name__ == '__main__':
    print(Research.file_reader())