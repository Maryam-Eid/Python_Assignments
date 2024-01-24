# 1
myList = [1, 2, 3, 3, 4, 5, 1]
uniqueList = list(set(myList))
print(uniqueList)
print(type(uniqueList))
uniqueList.pop()
print(uniqueList)

# 2
nums = {1, 2, 3}
letters = {"A", "B", "C"}
print(nums | letters)
print(nums.union(letters))
nums.update(letters)
print(nums)

# 3
mySet = {1, 2, 3}
letters = {"A", "B", "C"}

print(mySet)
mySet.clear()
print(mySet)
mySet.add("A")
mySet.add("B")
print(mySet)
mySet.discard("C")

# 4
setOne = {1, 2, 3}
setTwo = {1, 2, 3, 4, 5, 6}
print(setOne.issubset(setTwo))

# 5
skillsDic = {
    "HTML": 90,
    "CSS": 80,
    "Python": 30
}

print(f"HTML Progress Is {skillsDic['HTML']}%")
print(f"CSS Progress Is {skillsDic['CSS']}%")
print(f"Python Progress Is {skillsDic['Python']}%")

skillsDic["AI"] = 20
print(f"AI Progress Is {skillsDic['AI']}%")
