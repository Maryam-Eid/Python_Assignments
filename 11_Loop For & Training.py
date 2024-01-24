# 1
myNums = [15, 81, 5, 17, 20, 21, 13]
myNums.sort(reverse=True)
count = 0

for num in myNums:
    if num % 5 == 0:
        count += 1
        print(f"{count} => {num}")
else:
    print("All Numbers Printed")

# 2
num = 1
while num <= 20:
    if num == 6 or num == 8 or num == 12:
        num += 1
        continue

    print(str(num).zfill(2))
    num += 1
else:
    print("All Numbers Printed")

# 3
myRanks = {
    'Math': 'A',
    "Science": 'B',
    'Drawing': 'A',
    'Sports': 'C'
}

points = 0
total = 0
for rank in myRanks:
    if myRanks[rank] == 'A':
        points = 100
    elif myRanks[rank] == 'B':
        points = 80
    elif myRanks[rank] == 'C':
        points = 40

    total += points
    print(f"My Rank in {rank} Is {myRanks[rank]} And This Equal {points} Points")
else:
    print(f"Total Points Is {total}")

# 4
students = {
    "Ahmed": {
        "Math": "A",
        "Science": "D",
        "Draw": "B",
        "Sports": "C",
        "Thinking": "A"
    },
    "Sayed": {
        "Math": "B",
        "Science": "B",
        "Draw": "B",
        "Sports": "D",
        "Thinking": "A"
    },
    "Mahmoud": {
        "Math": "D",
        "Science": "A",
        "Draw": "A",
        "Sports": "B",
        "Thinking": "B"
    }
}

# items()
points = 0
total = 0
for student, subjects in students.items():
    print("-" * 30)
    print(f"-- Student Name => {student} ")
    print("-" * 30)
    for subject, rank in subjects.items():
        if rank == 'A':
            points = 100
        elif rank == 'B':
            points = 80
        elif rank == 'C':
            points = 40
        elif rank == 'D':
            points = 20
        total += points
        print(f"- {subject} => {points} Points")
    print(f"Total Points For {student} Is {total}")
    total = 0


# regular way
points = 0
total = 0
for student in students:
    print("-" * 30)
    print(f"-- Student Name => {student} ")
    print("-" * 30)
    for subject in students[student]:
        if students[student][subject] == 'A':
            points = 100
        elif students[student][subject] == 'B':
            points = 80
        elif students[student][subject] == 'C':
            points = 40
        elif students[student][subject] == 'D':
            points = 20
        total += points
        print(f"- {subject} => {points} Points")
    print(f"Total Points For {student} Is {total}")
    total = 0
