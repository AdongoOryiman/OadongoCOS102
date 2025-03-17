print("\n\t\tWelcome!")
while True:
 print("\n1. Simple Interest")
 print("2. Compound Interest")
 print("3. Annuity Plan")
 print("4. Exit")

 buffer = input("Kindly enter the number associated with what you want to calculate/do: ")

 if buffer == "1":
     p_1 = float(input("Enter the Principal Amount: "))
     r_1 = float(input("Enter the Rate of Interest: "))
     t_1 = float(input("Enter the Time Period: "))
     a = p_1 * (1.0 + (r_1/100.0) * t_1)
     print("Simple Interest = " + str(a))
 elif buffer == "2":
     p_2 = float(input("Enter the Principal Amount: "))
     r_2 = float(input("Enter the Rate of Interest: "))
     t_2 = float(input("Enter the Time Period: "))
     n = float(input("Enter the number of times the interest is compounded: "))
     b = p_2 * (1.0 + r_2/n) ** (n * t_2)
     print("Compound Interest = " + str(b))
 elif buffer == "3":
     p_3 = float(input("Enter the Principal Amount: "))
     r_3 = float(input("Enter the Rate of Interest: "))
     t_3 = float(input("Enter the Time Period: "))
     n = float(input("Enter the number of times the interest is compounded: "))
     c = p_3 * ((1.0 + r_3/n) ** (n * t_3) - 1.0) / (r_3/n)
     print("Annuity Plan = " + str(c))
 elif buffer == "4":
     break
 else:
     print("Invalid Input")