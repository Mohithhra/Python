password = input("Enter your password: ")

upper = 0
lower = 0
digit = 0
special = 0

for ch in password:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
    elif ch.isdigit():
        digit += 1
    else:
        special += 1

length = len(password)

if length < 6:
    print("Password Strength: Weak")
elif upper > 0 and lower > 0 and digit > 0 and special > 0 and length >= 8:
    print("Password Strength: Strong")
else:
    print("Password Strength: Medium")