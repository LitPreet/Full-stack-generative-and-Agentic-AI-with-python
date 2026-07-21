# walrus operator 
# value = 6
# remainder = value % 2
# if remainder:
#     print(f"{value} is divisible by 2");

# with walrus 
value = 7
if remainder := value % 2 == 0:
    print(f"{value} is divisible by 2");
else:
    print("not divisble")