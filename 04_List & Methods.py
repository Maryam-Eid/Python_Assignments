# 1
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
print(friends[0])
print(friends[-5])
print(friends[4])
print(friends[-1])

# 2
print(friends[::2])
print(friends[1::2])

# 3
print(friends[1:-1])
print(friends[-2:])

# 4
friends[-1], friends[-2] = "Elzero", "Elzero"

# 5
friends = ["Osame", "Ahmed", "Sayed"]
friends.insert(0, "Nasser")
friends += ["Salem"]

print(friends)

# 6
del friends[0:2]
print(friends)
friends.pop()
print(friends)

# 7
employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]

newList = friends + employees + school
print(newList)

# 8
newList.sort()
print(newList)
newList.sort(reverse=True)
print(newList)

# 9
print(len(newList))

# 10
technologies = ["Hrml", "CSS", "JS", "Python", ["Django", "Flack", "Web"]]
print(technologies[-1][0])
print(technologies[-1][-1])
