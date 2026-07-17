# loops 
# The while Loop
# With the while loop we can execute a set of statements as long as a condition is true
i = 1
# for i in range(1,6):
#     print(f"serving chai task {i}")


adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

# for x in adj:
#   for y in fruits:
#     print(x, y)


while i < 6:
  print(f"serving chai task {i}")
  i += 1
      
#  The else block will NOT be executed if the loop is stopped by a break statement.
# break and continue statements      
while i < 6:
  print(f"serving chai task {i}")
  i += 1 
else:
  print("Chai is served")        

