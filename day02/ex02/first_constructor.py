import sys

class Research:
    path_to_file: str

    def __init__(self, file_name):
        self.path_to_file = file_name
    
    
    def file_reader(self):
        with open(self.path_to_file, 'r') as file:
            lines = file.readlines()
        header = lines[0].split(',')
        if len(header) != 2 or header[0] == '0'or header[0] == '1': 
            raise Exception('Invalid header')
        elif header[0].isspace() or header[1].isspace():
            raise Exception('Invalid header')
        data = []
        for line in lines[1:]:
            data.append(line.strip())
        for line in data:
            if line != '0,1' and line != '1,0':
                raise Exception('Invalid data')
        with open(self.path_to_file, 'r') as file2:
            result = file2.read()
        return(result)
    
    
    
if __name__ == '__main__':
    if len(sys.argv) == 2:
        print(Research(sys.argv[1]).file_reader())
