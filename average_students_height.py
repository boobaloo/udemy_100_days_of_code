# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

overall_height = sum(student_heights)
number_of_students = len(student_heights)
print(round(overall_height/number_of_students))
# Write your code below this row 👇

