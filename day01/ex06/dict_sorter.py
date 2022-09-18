
if __name__ == '__main__':

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
    
    d = {key: int(value) for key, value in list_of_tuples}
    a = sorted(d.items(), key=lambda x: (-x[1], x[0]))
    for i in a:
        print(i[0])
    
    # dict1 = dict(list_of_tuples)
    # dict2s = dict(sorted(dict1.items(), key=lambda item: (-int(item[1]), item[0])))
    # for k, v in dict2s.items():
    #    print(k)
   
