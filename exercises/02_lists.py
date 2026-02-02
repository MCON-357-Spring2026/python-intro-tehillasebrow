"""
TODO:
1. Create list of favorite foods
2. Print first and last
3. Add one item
4. Remove one item
5. Print all items with loop
6. List comprehension for the lengths of each food item -
 create a new list where each item is  the length of the corresponding food item in the original list.
"""
print("Create list of favorite foods")
favoriteFoods=["pasta", "cholent", "cheesecake"]
print("Print first and last")
print(favoriteFoods[0])
print(favoriteFoods[-1])
print("Add one item")
favoriteFoods.append("ice cream")
print("Remove one item")
favoriteFoods.remove("cholent")
print("Print all items with loop")
for item in favoriteFoods:
    print(item)
print("List comprehension for the lengths of each item -")
foodLength=[len(item) for item in favoriteFoods]
print(foodLength)
