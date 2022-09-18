
def to_dictionary():
    list_of_tuples = [
        ('Russia', '25'),
        ('France', '132'),
        ('Germany', '132'),
        ('Spain', '178'),
        ('Italy', '162'),
        ('Portugal', '17'),
        ('Finland', '3'),
        ('Hungary', '2'),
        ('The Netherlands', '28'),
        ('The USA', '610'),
        ('The United Kingdom', '95'),
        ('China', '83'),
        ('Iran', '76'),
        ('Turkey', '65'),
        ('Belgium', '34'),
        ('Canada', '28'),
        ('Switzerland', '26'),
        ('Brazil', '25'),
        ('Austria', '14'),
        ('Israel', '12')
    ]
    raw_dict = dict(list_of_tuples)

    # new_dict = {val : key for key, val in raw_dict.items()} #затрет повторяющиеся значения и сохранит последнее 
    # for key, val in new_dict.items():
    #     print("'" + key + "'" + ": " + "'" + val + "'")

    new_dict = {}
    for key in raw_dict:
        new_dict.setdefault(raw_dict[key], []).append(key) #сохранит все значения 

    for key, values in new_dict.items():
        for value in values:
            print("'" + key + "'" + ": " + "'" + value + "'")

if __name__ == '__main__':
    to_dictionary()

