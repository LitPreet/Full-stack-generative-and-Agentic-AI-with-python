# tuples 
# this is new data type  
# it works in () parenthesis and immutable in nature

# tuple created 
spices = ("salt", "pepper", "turmeric", "cumin")

# access 
print(spices[0]) # salt

# last item of tuple
print(spices[-1]) # cumin

print(spices[1:3])

#updating typle is not possible as it is immutable
# convert to list and then update

spices_list = list(spices)
spices_list[0] = "chili"
spaces = tuple(spices_list)
print(spaces) # ('chili', 'pepper', 'turmeric', 'cumin')

# unpacking tuple
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

for fruit in fruits:
    print(fruit)