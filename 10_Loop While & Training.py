# 1
num = int(input("Enter The Number: "))
count = 0
while num <= 0:
    num = int(input("The Number Must Be Bigger Than 0 :) "))
else:
    while num > 1:
        if num == 7:
            num -= 1
            continue

        print(num - 1)
        count += 1
        num -= 1
    else:
        print(f"{count} Numbers Printed Successfully.")

# 2
friends = ["Mohamed", "Shady", "ahmed", "eman", "Sherif"]
count = 0
for i in friends:
    if i[0].isupper():
        print(i)
    else:
        count += 1
else:
    print(f"Friends Printed And Ignored Names Count Is {count}")

# 3
skills = ["HTML", "CSS", "JavaScript", "PHP", "Python"]

while skills:
    print(skills.pop(0))

# 4
myFriends = []
max = 4

while max:
    name = input("Enter The Name To Add: ")
    if name.isupper():
        print("Invalid Name")
        continue
    myFriends.append(name.capitalize())
    print(f"Friend {name} Added => 1st Letter Become Capital")
    max -= 1
    print(f"Names Left in List Is {max}")
else:
    print("List Is Full :)")