# 1
name = input("what's Your Name? ").strip().title()
print(f"Hello {name}, Happy To See You Here.")

# 2
age = int(input("What's Your Age? "))
if age < 16:
    print("Hello Your Age Is Under 16, Some Articles Is Not Suitable For You")
else:
    print(f"Hello Your Age Is {age}, All Articles Is Suitable For You")

# 3
firstName = input("What's Your First Name? ").strip().capitalize()
secondName = input("What's Your Second Name? ").strip().capitalize()
print(f"Hello, {firstName} {secondName[0]}.")

# 4
email = input("What's Your Email? ").strip().lower()
print(f"Your Name Is {email[:email.index('@')].capitalize()}")
print(f"Email Service Provider Is {email[email.index('@') + 1:email.index('.')]} ")
print(f"Top Level Domain Is sa {email[email.index('.') + 1 :]}")
