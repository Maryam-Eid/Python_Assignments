# 1
NUM = input("Add Your Number: ")

try:
    if len(NUM) > 1:
        raise IndexError("Only One Character Allowed")

    if not NUM.isdigit():
        raise Exception("Invalid Input: Only Numbers Allowed")

    num = int(NUM)

    if num == 0:
        raise ValueError("Number Must Be Larger Than 0")

    print("#" * 20)
    print(f"The Number Is {num}")
    print("#" * 20)

except IndexError as e:
    print(f"IndexError: {e}")
except ValueError as e:
    print(f"ValueError: {e}")
except Exception:
    print("Exception: Only Numbers Allowed")

print("#" * 10)
# 2
LETTER = input("Add Letter From A to Z: ")

try:
    if len(LETTER) != 1:
        raise ValueError("You Must Write One Character Only")

    if not ('A' <= LETTER <= 'Z'):
        raise ValueError("The Letter Not In A - Z")

except ValueError as e:
    print(f"ValueError: {e}")

else:
    print(f"You Typed {LETTER}")

print("#" * 10)


# 3
def calculate(num1, num2) -> int:
    return num1 + num2


print(calculate(20, 30))
