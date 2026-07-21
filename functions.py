# functions 

def print_order(name, designation):
    print(f"{name} works as {designation}")

print_order("Preet","FF")
   

#    local scope 
def my_fun():
    x = 200
    print(x)

my_fun()  

# function within function 
def out_fun():
    x = 700
    def in_fun():
        print(x)
    in_fun()    
out_fun()


# global scope 
# Global variables are available from within any scope, global and local.

x = 300

def myfunc():
  print(x)

myfunc()

print(x)

def myfunc1():
  global x
  x = 300

myfunc1()

print(x)

# Python follows the LEGB rule when looking up variable names, and searches for them in this order:

# Local - Inside the current function
# Enclosing - Inside enclosing functions (from inner to outer)
# Global - At the top level of the module
# Built-in - In Python's built-in namespace


# Rule of thumb
# No keyword → assigning to a variable inside a function creates a new local variable.
# nonlocal → modify a variable from the nearest enclosing function.
# global → modify a variable defined at the module (global) level.

# A good way to remember it is:

# Local → "This function's own variable."
# Nonlocal → "My parent function's variable."
# Global → "The module's variable that everyone can access."

o = "global"

def outer():
   x = "enclosing"
   def inner():
      x = "local"
      print("inner", x)
   inner()

   print("Outer:", x)
outer() 

print("global", o)          

