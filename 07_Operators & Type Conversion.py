# 1
print(bool("Hi"))
print(bool(True))
print(bool(0 | 1))
print(bool(1 + 2))
print(bool(""))
print(bool(not True))
print(bool(0 & 1))
print(bool(1 - 1))

# 2
html = 80
css = 60
javascript = 70
print(html > 50 and css > 50 and javascript > 50)

# 3
numOne = 10
numTwo = 20
num = 20

print(num > numOne or num > numTwo)
print(num > numOne and num > numTwo)

# 4
numOne = 10
numTwo = 20
result = numOne + numTwo
print(result)
result **= 3  # pow(result, 3)
print(result)
result %= 26000
print(result)
result /= 5
print(result)
result = str(result)
print(type(result))