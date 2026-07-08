#  strings
name = "Alice"
greeting = f"Hello, {name}!"
print(greeting)

desc = "Aromatic and bold"
print(f"First word of description: {desc[0:8]}")
print(f"First word of description: {desc[0:8:1]}") #
print(f"First word of description: {desc[0:8:2]}") # skip every 2 char
print(f"First word of description: {desc[12:]}")
print(f"Reversed description: {desc[::-1]}")

label_text = "Hello Thère!"
print(f"Label text: {label_text}")
encoded_text = label_text.encode("utf-8")
print(f"Encoded text: {encoded_text}")

decoded_text = encoded_text.decode("utf-8")
print(f"Decoded text: {decoded_text}")