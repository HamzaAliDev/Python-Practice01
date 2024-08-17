# Grade Calculator:
# Write a Python program that takes a percentage as input and prints the corresponding grade.
# 90-100: A
# 80-89: B
# 70-79: C
# 60-69: D
# Below 60: F

percent = float(input("Enter your percentage: "))

if percent >= 90 and percent <=100:
    print('A')
elif percent >=80 and percent <= 89:
    print('B')
elif percent >=70 and percent <= 79:
    print('C')
elif percent >=60 and percent <= 69:
    print('D')
elif percent < 60:
    print('F')
else:
    print("Invalid Percentage")