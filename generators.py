# Generators
# Generators are functions that can pause and resume their execution.
# you save memory
# you dont want immediate execution 

# def get_chai_list():
#     yield "cup1"
#     yield "cup2"
#     yield "cup3"
#     yield "cup4"

# chai = get_chai_list()
# print(next(chai))
# print(next(chai))
# print(next(chai))


def infinite_chai():
    count = 1
    while True:
        yield f"refill #{count}"
        count += 1

refill = infinite_chai()

for _ in range(3):
    print(next(refill))