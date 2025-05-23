print("\t\t\tWelcome Izinfin Taxify")
age = int(input("Enter your age: "))
nwx = int(input("Enter your number of working experience years: "))

print("# Note: ATR stands for Annual Tax Revenue")
if age >= 55 and nwx > 25:
    print("Your ATR is N5,600,000")
elif age >= 45 and nwx > 20:
    print("Your ATR is N4,480,000")
elif age >= 35 and nwx > 10:
    print("Your ATR is N1,500,000")
elif age < 35 and nwx < 10:
    print("Your ATR is N550,000")
else:
    print("Oops, you ran into an error!")