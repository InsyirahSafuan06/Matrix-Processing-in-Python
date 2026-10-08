import numpy as np
import matplotlib.pyplot as plt

marks = np.array([
 [78, 85, 82, 88],
 [90, 88, 91, 86],
 [70, 75, 72, 80]
])

print(marks)
print(type(marks))
print(marks.dtype)
print(marks.shape)
print(marks.size)
print(marks.ndim)
print(marks[1])
print(marks[:, 1])
print(marks[0, 0:2])


avg = marks.mean(axis=1)
print(avg)
print(marks.max())

new_marks = marks + 5
print(new_marks)

students = ["A", "B", "C"]
plt.bar(students, avg)
plt.title("Average Marks of Students")
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.show()