#Clasify_Age
def age():
    age = int(input("Enter your age: "))
    if age <= 12:
        print("You are a CHILD.")
    elif age <= 19:
        print("Your are a TEEN.")
    elif age <= 64:
        print("You are a ADULT.")
    elif age >= 65:
        print("You are a SENIOR.")

age()

while True:
    a = input("Run again?:")
    if a == "Yes":
        age()

    else:
        b = input("CONFIRMED")
        break