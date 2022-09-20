import sys

class Research:
    path_to_file: str

    def __init__(self, file_name):
        self.path_to_file = file_name
    
    
    def file_reader(self, has_header=True):
        with open(self.path_to_file, 'r') as file:
            lines = file.readlines()
        header = lines[0].split(',')
        if len(header) != 2:
            raise Exception('Invalid header')
        if header[0] == '0' or header[0] == '1': 
            has_header=False
        data = []
        if has_header:
            for line in lines[1:]:
                data.append(line.strip())
        else:
            for line in lines:
                data.append(line.strip())
        for line in data:
            if line != '0,1' and line != '1,0':
                raise Exception('Invalid data')
        list_of_data = list(map(lambda x : x.split(','), data))
        for elem in list_of_data:
            elem[0] = int(elem[0])
            elem[1] = int(elem[1])   
        return list_of_data 

    class Calculations:

        def counts(self, data):
            heads = [x[0] for x in data]
            tails = [y[1] for y in data]
            return [sum(heads), sum(tails)]

        def fractions(self, counts):
            heads_fraction = (counts[0] / (counts[0] + counts[1])) * 100
            tails_fraction = (counts[1] / (counts[0] + counts[1])) * 100
            return [heads_fraction, tails_fraction]
            

if __name__ == '__main__':
    if len(sys.argv) == 2:
        research = Research(sys.argv[1])
        file_reader = research.file_reader()
        print(file_reader)
        counts = research.Calculations().counts(file_reader)
        print(counts[0], counts[1])
        fractions = research.Calculations().fractions(counts)
        print(fractions[0], fractions[1])
