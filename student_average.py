student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
  count = 0
  sum_of_h = 0
  for number in student_heights:
    count = count + 1
    sum_of_h = sum_of_h + number
  print(round(sum_of_h/count))
