from functools import reduce


# 1
def remove_chars(string):
    return string[1:-1]


friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]

cleaned_list = list(map(remove_chars, friends_map))

for name in cleaned_list:
    print(name)

print("#" * 10)

for name in map(lambda name: name[1:-1], friends_map):
    print(name)

print("#" * 10)


# 2
def get_names(name):
    return name[-1] == "m"


friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]

names = list(filter(get_names, friends_filter))

for name in names:
    print(name)

print("#" * 10)

for name in filter(lambda name: name[-1] == "m", friends_filter):
    print(name)

print("#" * 10)


# 3

def mul(x, y):
    return x * y


nums = [2, 4, 6, 2]

print(reduce(mul, nums))
print("#" * 10)
print(reduce(lambda x, y: x * y, nums))
print("#" * 10)

# 4
skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")

for index, skill in enumerate(reversed(skills), 50):
    if isinstance(skill, int):
        continue
    print(f"{index} - {skill}")

