# Program to calculate average marks and grade

m1 = float(input("Enter marks of subject 1: "))
m2 = float(input("Enter marks of subject 2: "))
m3 = float(input("Enter marks of subject 3: "))
m4 = float(input("Enter marks of subject 4: "))
m5 = float(input("Enter marks of subject 5: "))

average = (m1 + m2 + m3 + m4 + m5) / 5

if average >= 85:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 55:
    grade = "C"
elif average >= 40:
    grade = "D"
else:
    grade = "Fail"

print("Average Marks:", average)
print("Grade:", grade)