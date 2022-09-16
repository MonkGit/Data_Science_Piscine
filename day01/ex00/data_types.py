def data_types():
    variables = (1, 'str', 4.2, True, [5, 5, 5], {'key': 'val'}, ('tuple', 12), {1, 2, 3, 4})

    print("[", end="")
    for var in variables:
        print(type(var).__name__, end="")
        if type(var).__name__ != 'set':
            print(", ", end="")
    print("]")


if __name__ == '__main__':
    data_types()