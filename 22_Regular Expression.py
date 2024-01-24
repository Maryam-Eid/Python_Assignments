import re

# 1
print(re.findall(r'\D\b', "eeeeE llllLl lllzzZzzzz eroe operationr pollo "))
print("#" * 10)

# 2
print(re.findall(r'\bLElzero', "EElzero11 LElzero111 ZElzero1111 EElzero11111 RElzero111111 OElzero1111111"))
print("#" * 10)

# 3
print(re.findall(r'\+*\(\d{4}\)\D\d{2,}-\d{4}',
                 "+(0100) 600-1234 +(0100) 60-1234 (0100) 6000-1234 01006001234 0100 600 1234 (0100) 600-1 (0100) 600-12"))
print("#" * 10)

# 4
print(re.findall(r'(https?://)(www\.)?(elzero)(.org)?(.com)?(:8888)?(/link)(.php)?(.py)?',
                 "http://www.elzero.org:8888/link.php https://elzero.org:8888/link.ph http://www.elzero.com/link.py https://elzero.com/link.py http://www.elzero.net https://elzero.net"))
print("#" * 10)

# 5
print("1st Method")
print(re.findall(r'[h-t]',
                 "http https abcd abcd"))

print("2nd Method")
print(re.findall(r'[^a-d\s]',
                 "http https abcd abcd"))

print("3rd Method")
print(re.findall(r'h\w+',
                 "http https abcd abcd"))

print("4th Method")
print(re.findall(r'https?',
                 "http https abcd abcd"))

print("5th Method")
print(re.findall(r'http|s',
                 "http https abcd abcd"))

