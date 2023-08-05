print("Welcome to the system")
a = int(input("Please write the first number"))
b = int(input("Please write the second number"))
c = int(input("Please write the third number"))

if a < b < c:
    print("{} is the largest number.".format(c))
elif a < c < b:
    print("{} is the largest number.".format(b))
elif b < a < c:
    print("{} is the largest number.".format(c))
elif b < c < a:
    print("{} is the largest number.".format(a))
elif c < b < a:
    print("{} is the largest number.".format(a))
elif c < a < b:
    print("{} is the largest number.".format(b))
