# 1
name = "Maryam"
age = "18"
country = "Egypt"

print("Hello '" + name + '\' , How You Doing \\ """ Your Age Is "' + age + '"" +  And Your Country Is:' + country)

# 2
print("Hello '" + name + '\' , How You Doing \\ \n""" Your Age Is "' + age + '"" + \nAnd Your Country Is:' + country)

# 3
name = "Elzero"

print(name[1])
print(name[2])
print(name[-1])

# 4
print(name[1:4])
print(name[::2])
print(name[-2::-2])

# 5
name = "#@#@Elzero#@#@"

print(name.strip("#@"))

# 6
n = "7"
print(n.zfill(4))
n = "1999"
print(n.zfill(4))

# 7
name = "Osama"
print(name.rjust(20, "@"))
name = "Osama_Elzero"
print(name.rjust(20, "@"))

# 8
name = "OSamA"
print(name.swapcase())
name = "osaMA"
print(name.swapcase())

# 9
msg = "I Love Python And Although Love Elzero Web School"
print(msg.find("Love"))

# 10
name = "Elzero"
print(name.index("z"))

# 11
msg = "I <3 Python And Although <3 Elzero Web School"
print(msg.replace("<3", "Love", 1))

# 12
print(msg.replace("<3", "Love"))

# 13
name = "Maryam"
age = 18

print(f"Hello, My Name Is {name} And Iam {age} Years Old and I Live in {country}.")

