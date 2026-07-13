# conditionals 
# snack suggestions 

# snack = input("What snack do you want? ").lower()

# print("You chose: " + snack)

# if snack == "cookies" or snack == "chips":
#     print(f"Good choice! {snack.capitalize()} are delicious. we will serve it")
# else:
#         print(f"Sorry, we don't have {snack}. Please choose cookies or chips.")
    

    # building a chai price calculator 

cup = input("Choose your cup size (small/medium/large): ").lower()

if cup == "small":
    price = 2.50
    print(f"The price for a {cup} cup of chai is ${price:.2f}")
elif cup == "medium":
    price = 3.50
    print(f"The price for a {cup} cup of chai is ${price:.2f}")
elif cup == "large":
    price = 4.50
    print(f"The price for a {cup} cup of chai is ${price:.2f}")