# Comprehensions in Python provide a short and clear way to create new sequences from existing iterables.

# Improve readability by replacing long loops with a single statement.
# Encourage modular and clean coding practices.
# Commonly used in data processing, web development, and automation tasks.
# Reduce errors by minimizing lines of code.
# Work well with functions like zip(), enumerate(), map(), and lambda.

# 1. List Comprehensions
# List comprehensions allow for the creation of lists in a single line, improving efficiency and readability. They follow a specific pattern to transform or filter data from an existing iterable.
# : Generating a list of even numbers

# Syntax:

# [expression for item in iterable if condition]
a = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
# bina comprehension k loop chalana pdega and append krna hoga coz we want to create a new list from it
even_num = [e_num for e_num in a if e_num %2 == 0]
# print(even_num)

menu = ["Iced Lemon tea", "Iced Peach tea", "Green Tea", "Ginger Tea"]
# iced_tea = [tea for tea in menu if "Iced" in tea]
iced_tea = [tea for tea in menu if len(tea) >  12]
# print(iced_tea)



# 2. set comprehension 
# when you want unique ones use sets
unique_even = {u_ev for u_ev in a if u_ev % 2 == 0}
# print(unique_even)

recipes = {
    "Masala Chai":["ginger", "clove", "cardamom"],
    "Elaichi Chai":["milk", "cardamom"],
    "Spicy Chai":["ginger","black pepper","clove"]
}
unique_spice = {spice for ingrediants in recipes.values() for spice in ingrediants }
# print(unique_spice)

# 3. Dictionary comprehension
tea_prices_inr = {
    "Masala chai": 40,
    "Lemon chai": 90,
    "Green chai": 80
}
tea_prices_usd = {tea:price / 80 for tea, price in tea_prices_inr.items()}
# print(tea_prices_usd)

# 4. Generator comprehensions
# Generator Comprehensions create iterators that generate values lazily, making them memory-efficient as elements are computed only when accessed.
daily_sales = [ 5,10,12,15,18,7,3,9]
total_cupes = sum(sale for sale in daily_sales if sale > 5)
print(total_cupes)