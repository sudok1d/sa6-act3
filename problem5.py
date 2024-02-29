def list_to_n(values, n):
    print(list(map(lambda x: x ** n, values)))


values = [5, 4, 3, 2, 1]

list_to_n(values, 3)