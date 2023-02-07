import os

my_file = os.path.join(os.getcwd(), "fruits.txt")

f = open(my_file)
fruits = f.read().split("\n")
print(fruits)