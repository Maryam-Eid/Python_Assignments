# 1
def calculate(num1, num2, op="a"):
    op = op.lower()
    if op == "add" or op == "a":
        print(num1 + num2)
    elif op == "subtract" or op == "s":
        print(num1 - num2)
    elif op == "multiply" or op == "m":
        print(num1 * num2)
    else:
        print("invalid Operator")


calculate(10, 20)  # 30
calculate(10, 20, "AdD")  # 30
calculate(10, 20, "a")  # 30
calculate(10, 20, "A")  # 30

calculate(10, 20, "S")  # -10
calculate(10, 20, "subTRACT")  # -10

calculate(10, 20, "Multiply")  # 200
calculate(10, 20, "m")  # 200


# 2
def add(*nums):
    result = 0
    for num in nums:
        if num == 5:
            result -= num
        elif num == 10:
            continue
        else:
            result += num
    print(result)


add(10, 20, 30, 10, 15)  # 65
add(10, 20, 30, 10, 15, 5, 100)  # 160


# 3
def show_skills(name, *skills):
    if not skills:
        print(f"Hello {name} You Have No Skills To Show")
    else:
        print(f"Hello {name} Your Skills Is")
        for skill in skills:
            print(skill)

show_skills("Osama", "HTML", "CSS", "JS", "Python")
show_skills("Ahmed")


# 4
def say_hello(name="Unknown", age="Unknown", country="Unknown"):
    print(f"Hello {name} Your Age Is {age} And You Live In {country}")


say_hello("Osama", 38, "Egypt")
say_hello()
