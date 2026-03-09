name = input("Enter student's name: ")
m1 = float(input("Enter mark for Subject 1: "))
m2 = float(input("Enter mark for Subject 2: "))
m3 = float(input("Enter mark for Subject 3: "))

average = (m1 + m2 + m3) / 3

print("--- Result ---")
print(f"Name: {name}")
print(f"Average: {average:.1f}")