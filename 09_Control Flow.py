# 1
num1 = int(input("Enter 1st Number: ").strip())
num2 = int(input("Enter 2nd Number: ").strip())
op = input("Available Operations: +, -, *, /, % ").strip()

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
elif op == "%":
    print(num1 % num2)
else:
    print("Invalid Operation :)")

# 2
age = int(input("What's Your Age? "))
print("App Is Suitable For You" if age > 16 else "App Is Not Suitable For You")

# 3
age = int(input("What's Your Age? "))

if age > 100 or age < 10:
    print("Age is out of range")
else:
    months = age * 12
    weeks = months * 4
    days = weeks * 7
    hours = days * 24
    minutes = hours * 60
    seconds = minutes * 60
    print(f"Your Age In Months Is {months} Months")
    print(f"Your Age In weeks Is {weeks} weeks")
    print(f"Your Age In days Is {days} days")
    print(f"Your Age In hours Is {hours} hours")
    print(f"Your Age In minutes Is {minutes} minutes")
    print(f"Your Age In seconds Is {seconds} seconds")

# 4
country = input("Input Your Country ").strip().capitalize()
countries = ["Egypt", "Palestine", "Syria", "Yemen", "KSA", "USA", "Bahrain", "England"]
price = 100
discount = 30

if country in countries:
    print(f"Your Country Eligible For Discount And The Price After Discount Is ${price - discount}")
else:
    print(f"Your Country Not Eligible For Discount And The Price Is ${price}")