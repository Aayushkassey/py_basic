"""my_set = {1, 3, 7, 2, 3, 4, 4, 5, "apple", "banana", "ink"}
print(my_set)"""

my_set = [1, 2, 7, 3, 8, 9, "hi", "hello", 8, 9, 10]
my_data= list((dict.fromkeys(my_set)))
print(my_data)