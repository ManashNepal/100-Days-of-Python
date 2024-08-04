# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
total_height = 0
student_count = 0
for height in student_heights:
  total_height += height
  student_count += 1
print(f"total height = {total_height}")
print(sum(student_heights))
print(f"number of students = {student_count}")
average_height = round(total_height/student_count)
print(f"average height = {average_height}")
# Write your code below this row 👇
