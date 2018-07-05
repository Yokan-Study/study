def sum10(number):
    # TODO
    sum = 0
    for i in number:
        sum += i
    return sum

one_to_ten = range(1,11)
result = sum10(one_to_ten)

print(result) 