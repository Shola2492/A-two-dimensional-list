# 2 dimentional list 
# it is a list made up of list 2dlist = [list1, list2, list3]
# a grid or matrix of data kind of an excel spreadsheet


# 
# fruit =      ["Apple", "Orange", "Banana", "Coconut"]  # when lined up correctly it represents a grid or matrix
# vegetables = ["Ugwu", "Carrots", "Potatoes"]           # with rows or column
# meat =       ["Chicken", "Fish", "Turkey"]             # Each individual list resembles a row
#                                                        each element resembles a column
# groceries = [fruit, vegetables, meat]

# To access an element from a 2D list you'd need two indexes in place of one
# print(groceries[1][0]) 
# print(groceries[0]) It will bring out an entire list "fruit list"
# print(groceries[0][1]) For one of the elements found within one of the rows you'd need two indexes


# you dont necessarily need to give it a name
["Apple", "Orange", "Banana"]
["Ugwu", "Carrots", "Potatoes"]
["Chicken", "Fish", "Turkey"]


# Add every list and seperate with a comma ","
groceries = [["Apple", "Orange", "Banana"],
             ["Ugwu", "Carrots", "Potatoes"],
             ["Chicken", "Fish", "Turkey"]]

# Using nested loops we can iterates all items found on 2D collection

for collection in groceries:
    for food in collection:
        print(food, end=" ") # To make it arranged horizontally 
    print()