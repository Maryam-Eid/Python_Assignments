# 1
def reverse_string(my_string):
    for c in reversed(my_string):
        yield c


for c in reverse_string("Elzero"):
    print(c)

print("#" * 10)


# 2
def decorator(func):
    def wrapper():
        print("Sugar Added From Decorators")
        func()
        print("#" * 20)

    return wrapper


@decorator
def make_tea():
    print("Tea Created")


@decorator
def make_coffee():
    print("Coffee Created")


make_tea()
make_coffee()
