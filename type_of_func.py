# type of functions 
# pure vs impure 

# lamdas (anonymous funct)

def pure_chai(cups):
    return cups * 3

total_chai = 0

# not recommend 
def impure_chai(cups):
    global total_chai
    total_chai += cups


def pour_chai(n):
    if n == 0:
        return "All cups poured"
    return pour_chai(n-1)

print(pour_chai(3))

# A lambda function is a small anonymous function.

# A lambda function can take any number of arguments, but can only have one expression.

# lambda arguments : expression

chai_type = ["ginger","kadak","light","kadak"]

strong_chai = list(filter(lambda chai: chai == "kadak", chai_type))
print(strong_chai)