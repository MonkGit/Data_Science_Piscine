import sys
from random import randint

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

        def __init__(self, data):
            self.data = data
            self.count = self.counts()
            self.fractions = self.fractions()

        def counts(self):
            heads = [x[0] for x in self.data]
            tails = [y[1] for y in self.data]
            return [sum(heads), sum(tails)]

        def fractions(self):
            heads_fraction = (self.count[0] / (self.count[0] + self.count[1])) * 100
            tails_fraction = (self.count[1] / (self.count[0] + self.count[1])) * 100
            return [heads_fraction, tails_fraction]


    class Analytics(Calculations):

        def __init__(self, n_steps):
            self.n_steps = n_steps
            self.predict = self.predict_random()
            self.predict_last = self.predict_last()

        def predict_random(self):
            predict_dict = {0: [0, 1], 1: [1, 0]}
            return [predict_dict[randint(0, 1)] for x in range(self.n_steps)]

        def predict_last(self):
            return self.predict[-1]

if __name__ == '__main__':
    if len(sys.argv) == 2:
        file_reader = Research(sys.argv[1]).file_reader()
        element = Research.Calculations(file_reader)
        predict = Research.Analytics(8)
        fractions = Research.Calculations.fractions(element)
        print(element.data)
        print(element.count[0], element.count[1])
        print(round(fractions[0], 2), round(fractions[1], 2))
        print(predict.predict)
        print(predict.predict_last)