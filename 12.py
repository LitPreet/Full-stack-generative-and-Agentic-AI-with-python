# enumerate 
# The Python enumerate() function is a built-in tool that allows you to loop over an iterable while keeping track of both the index and the value of each item simultaneously.
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")

tasks = ["Write code", "Review PR", "Deploy app"]

# enumerate(iterable, start=0)
# iterable: Any object that supports iteration (e.g., list, tuple, string, dictionary).
# start (Optional): The integer value where the counter begins (defaults to

for position, task in enumerate(tasks, start=1):
    print(f"{position}: {task}")


    # zip 
    # In Python, the zip() function is a built-in utility that aggregates elements from two or more iterables (such as lists, tuples, or strings) into a single iterator of tuples. It

    names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

for name, score in zip(names, scores):
    print(f"{name} scored {score}")