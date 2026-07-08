# list 
# mutable data type

ingredients = ["flour", "sugar", "eggs", "milk"]
ingredients.append("butter")  # Adding an item to the list
print(f"Ingredients: {ingredients}")
ingredients.pop()  # Removing the last item from the list
print(f"Ingredients after pop: {ingredients}")


# // change list 
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
# // add items without replacing existing items
chai_ingredients = ["water", "tea leaves", "milk", "sugar"]
# Concatenating two lists add at specific index
all_ingredients = ingredients.insert(2, chai_ingredients)
print(f"All ingredients: {ingredients}")

# add list items using extend() method
more_ingredients = ["cardamom", "ginger"]
ingredients.extend(more_ingredients)
print(f"Ingredients after extending: {ingredients}")

# min, max 
ingredients[2].remove("sugar")  # Removing a specific item from the list
print(f"Ingredients after removing sugar: {ingredients}")

# If there are more than one item with the specified value, the remove() method removes the first occurrence:
# list comprehension
f = ["apple", "banana", "cherry", "kiwi", "mango"]
for x in f:
    if "a" in x:
        print(x)

#  copy list 
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()

# list(thislist)

       