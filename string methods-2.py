numbers = [15,23,49,6,20,23]
print(max(numbers))
print(sum(numbers))
print(sum(numbers)/len(numbers))
print(numbers[1:6])
print(numbers[::-1])
b = sorted(numbers)
print(b[1])
numbers.pop(3)
print(numbers)
numbers = [15,23,49,6,20,23]
print(numbers.count(23))
numbers2 = [2,6,89]
numbers_new = numbers + numbers2
print(numbers_new)
print(sorted(list(dict.fromkeys(numbers_new))))