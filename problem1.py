def sum_of_digits(num):
    sum_total = lambda n: sum(int(digit) for digit in str(n))
    print(sum_total(num))

sum_of_digits(1111)