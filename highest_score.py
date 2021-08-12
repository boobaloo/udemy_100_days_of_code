# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
# print(student_scores)
# 🚨 Don't change the code above 👆

# Write your code below this row 👇

highest_score = student_scores[0]
number_of_iterations = len(student_scores)
# print(f"Number of iterations: {number_of_iterations}")

while number_of_iterations > 1:
  for n in range(1, len(student_scores)):
    if student_scores[n] > highest_score:
      highest_score = student_scores[n]
      number_of_iterations -= 1
    else:
      number_of_iterations -= 1

print(f"Highest_score is equal to: {highest_score}")
