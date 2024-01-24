# 1
tuple = "Maryam",
print(tuple[0])
print(type(tuple))

# 2
friends = ("Osama", "Ahmed", "Sayed")
friends = ("Elzero",) + friends[1:]

print(friends)
print(type(friends))
print(f"{len(friends)} Elements")

# 3
nums = (1, 2, 3)
letters = ("A", "B", "C")

newTuple = nums + letters
print(newTuple)
print(f"{len(newTuple)} Elements")

# 4
myTuple = (1, 2, 3, 4)
a, b, _, c = myTuple
print(f"{a}\n{b}\n{c}")

