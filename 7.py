# set 
# Set items are unordered, unchangeable, and do not allow duplicate values.

# access set items
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

protein_sources = {"chicken", "fish", "tofu", "beans", "eggs", "lentils"}
veg_sources = {"almonds","walnuts" "beans", "paneer", "lentils"}

common_sources = protein_sources.intersection(veg_sources)
common_sources = protein_sources & veg_sources
print(f"Common protein and veg sources: {common_sources}")

all_protein_sources = protein_sources | veg_sources
print(f"Only protein sources: {all_protein_sources}")