def custom_sort(strings):
    print(sorted(strings, key= lambda x: (len(x), x)))

strings = ['esophagus', 'hello', 'goodbye', 'hi', 'by', 'greetings']

custom_sort(strings)