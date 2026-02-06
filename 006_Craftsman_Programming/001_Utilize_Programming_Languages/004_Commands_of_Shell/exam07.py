numbers = [1, 2, 3, 4, 5]
odd_numbers = {1, 3, 5}
new_set = {7, 9}
last_num = numbers.pop()
odd_numbers.add(last_num)
numbers.remove(3)
odd_numbers.update(new_set)
print(odd_numbers)