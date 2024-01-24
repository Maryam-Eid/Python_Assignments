# 1
values = (0, 1, 2)

# Since there is a '1', the condition evaluates to True
if any(values):
    my_var = 0

my_list = [True, 1, 1, ["A", "B"], 10.5, my_var]

# True, true, false (my_var)
# The overall condition => True
if all(my_list[:4]) or all(my_list[:6]) or all(my_list[:]):

    # Good will be printed
    print("Good")

else:

    print("Bad")

print("#" * 10)

# 2
v = 40

my_range = list(range(v))

# v(v + 1) / 2  + ( v ** v % v) = 820
# v(v + 1) / 2  + 0 = 820
# v(v + 1) = 1640
# v^2 + v - 1640 = 0
# (v − 40)(v + 41) = 0
# v + 40 = 0 => v = 40
print(sum(my_range, v) + pow(v, v, v))  # 820

print("#" * 10)

# 3
n = 20

l = list(range(n))

# (n(n + 1) / 2 ) / n + 1 = 10
# n(n + 1) / 2(n + 1) = 10
# n / 2 = 10 => n = 20
if round(sum(l) / n) == max(0, 3, 10, 2, -100, -23, 9):
    print("Good")

# Output => Good

print("#" * 10)


# 4

def my_all(items):
    for item in items:
        if not item:
            return False
    return True


def my_any(items):
    for item in items:
        if item:
            return True
    return False


def my_min(items):
    min = items[0]
    for item in items[1:]:
        if item < min:
            min = item
    return min


def my_max(items):
    max = items[0]
    for item in items[1:]:
        if item > max:
            max = item
    return max


print(my_all([1, 2, 3]))  # True
print(my_all([1, 2, 3, []]))  # False
print("#" * 10)
print(my_any([0, 1, [], False]))  # True
print(my_any([(), 0, False]))  # False
print("#" * 10)
print(my_min([10, 100, -20, -100, 50]))  # -100
print(my_min((10, 100, -20, -100, 50)))  # -100
print("#" * 10)
print(my_max([10, 100, -20, -100, 50, 700]))  # 700
print(my_max((10, 100, -20, -100, 50, 700)))  # 700
