def intersection(list1, list2):
    intersect = list(filter(lambda x: x in list2, list1))
    return intersect

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

intersect = intersection(list1, list2)

print(intersect)
