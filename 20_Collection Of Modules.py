from PIL import Image

# 1
my_list = ["E", "Z", "R", 1, 2, 3]
my_tuple = ("L", "E", "O")
my_data = []

for data in zip(my_list, my_tuple):
    my_data.append(data[0])
    my_data.append(data[1])

final_string = "".join(my_data)

print(final_string)  # Elzero
print("#" * 10)

# 2
my_list1 = ["E", "L", "Z", "E", "R", "O", 1, 2]
my_tuple = ("E", "Z", "R", 1, 2, "E", "R", "O")
my_list2 = ("L", "E", "O", 1, 2, "E", "R", "O")
my_data2 = []

for item1, item2, item3 in zip(my_list1, my_tuple, my_list2):
    if isinstance(item1, str):
        my_data2.append(item1)

final_string2 = "".join(my_data)

print(final_string2)
print("#" * 10)

# 3
my_image = Image.open(r"Images\elzero-pillow.png")
my_image.crop((400, 0, 800, 400)).convert("L").save(r"Images\L.png")
my_image.crop((0, 400, 1200, 800)).convert("L").rotate(180).save(r"Images\ERO.png")


# 4
def say_hello_to(someone):
    """
    parameter(someone) => Person Name
    Function To Say Hello To Anyone
    """
    return "Hello, " + someone


print(say_hello_to("Osama"))  # "Hello Osama"

help(say_hello_to)
print("#" * 10)

# 5
"""
This module defines a simple function for greeting people.
"""

myFriends = ["Ahmed", "Osama", "Sayed"]


def say_hello(some_peoples):
    """
    Print a greeting message for each person in the provided list.
    Returns: none
    """
    for someone in some_peoples:
        print(f"Hello, {someone}")


say_hello(myFriends)
