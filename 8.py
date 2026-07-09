# dictionary 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(f"Brand: {thisdict['brand']}, Model: {thisdict['model']}, Year: {thisdict['year']}")

# Changeable
# Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.

# Duplicates Not Allowed
# Dictionaries cannot have two items with the same key:

# Get Keys
# The keys() method will return a list of all the keys in the dictionary.

# Example
# Get a list of the keys:

x = thisdict.keys()
print(f"Keys: {x}")

# Get a list of the values:

x = thisdict.values()
print(x)

# Change Values
# You can change the value of a specific item by referring to its key name:
thisdict["year"] = 2021
print(thisdict)

# The update() method will update the dictionary with the items from the given argument.

# adding an item 
thisdict["color"] = "red"
print(thisdict)

thisdict.update({"color": "blue"})
print(thisdict)

# removing an item
remove_item = thisdict.pop("model")
print(thisdict)

# loop 
for x in thisdict:
  print(x)

#   You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.

# There are ways to make a copy, one way is to use the built-in Dictionary method copy().

mydict = thisdict.copy()
print(mydict)
