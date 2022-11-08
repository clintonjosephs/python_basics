# Data structures in Python
# Sets, lists, tuples, dictionaries

def lists():
    # List can be used to store multiple items in a single variable that can be ordered or modified. Lists also allows duplicate items.
    my_fruits = ["apple", "banana", "cherry", "banana", "cherry"]
    # list methods are append, clear, copy, count, extend, index, insert, pop, remove, reverse, sort
    my_fruits.append("orange")

    my_fruits[2] = "kiwi"
    print(my_fruits)

    for fruit in my_fruits:
        print(fruit)

    for index in range(len(my_fruits)):
        display_number = index + 1
        fruit_name = my_fruits[index]
        print(f"{display_number} - {fruit_name}")

def dictionaries():
    # Dictionaries are used to store data values in key:value pairs. A dictionary is a collection which is ordered*, changeable and does not allow duplicates.
    my_dict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    print(my_dict["brand"])

def sets():
    # Sets are used to store multiple items in a single variable. A set is a collection which is both unordered and unindexed. Sets are written with curly brackets.
    # The main difference between a list and a set is that a set cannot have duplicate items.
    my_set = {"apple", "banana", "cherry"}
    print(my_set)

def tuples():
    # Tuples are used to store multiple items in a single variable. A tuple is a collection which is ordered and unchangeable. Tuples are written with round brackets.
    # The main difference between a list and a tuple is that a list is mutable, while a tuple is immutable.
    my_tuple = ("apple", "banana", "cherry")
    print(my_tuple)
