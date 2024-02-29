def find_maximum(numbers, compare):
    maxim= numbers[0]

    for num in numbers[1:]:
        maxim = compare(maxim, num)

    return maxim

numbers = [9, 10, 2, 11, 15, 22]

greater = lambda x, y: x if x > y else y

maxim = find_maximum(numbers, greater)

print(maxim)
