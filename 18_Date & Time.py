import datetime

# 1
print(f"Days From 2021-06-25 To {datetime.datetime.now()} is:", (datetime.datetime.now() - datetime.datetime(2021, 6, 25)).days)
print("#" * 10)

# 2
today = datetime.datetime.now()
print(today.strftime("%Y-%m-%d"))
print(today.strftime("%b %d, %Y"))
print(today.strftime("%d - %b - %Y"))
print(today.strftime("%d / %b / %y"))
print(today.strftime("%d / %B / %Y"))
print(today.strftime("%a, %d %B %Y"))