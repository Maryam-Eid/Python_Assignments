import my_mod
from my_mod import say_welcome
from my_mod import say_welcome as new_welcome

# 2
print(my_mod.say_welcome("Maryam"))
print(my_mod.say_hello("Maryam"))

# 3
print(new_welcome("Maryam"))

# 4
print(say_welcome("Maryam"))

