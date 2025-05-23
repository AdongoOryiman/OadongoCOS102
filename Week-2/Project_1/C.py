print("\t\t\tWelcome to the AgeTranspose Alg.")
print("\nNOTICE:Ensure to leave a space between name & age!")
name_1 = input("[User 1]Enter your first name and age: ")
name_2 = input("[User 2]Enter your first name and age: ")

user_1 = name_1.split()
user_2 = name_2.split()

print(f"Name: {user_1[0]}, Age: {user_2[1]}")
print(f"Name: {user_2[0]}, Age: {user_1[1]}")