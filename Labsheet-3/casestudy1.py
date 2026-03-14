import numpy as np

# 1. Create a NumPy array to store marks of 50 students in 5 subjects
# Random marks between 0 and 100
marks = np.random.randint(0, 101, (50, 5))

print("Marks of 50 students in 5 subjects:\n", marks)

# 2. Display marks of first 10 students
print("\nMarks of first 10 students:")
print(marks[0:10])

# 3. Calculate total and average marks for each student
total_marks = np.sum(marks, axis=1)
average_marks = np.mean(marks, axis=1)

print("\nTotal marks of each student:")
print(total_marks)

print("\nAverage marks of each student:")
print(average_marks)

# 4. Find highest and lowest marks in each subject
highest_marks = np.max(marks, axis=0)
lowest_marks = np.min(marks, axis=0)

print("\nHighest marks in each subject:")
print(highest_marks)

print("\nLowest marks in each subject:")
print(lowest_marks)

# 5. Reshape the array to display subject-wise instead of student-wise
subject_wise = marks.T
print("\nSubject-wise marks:")
print(subject_wise)

# 6. Split dataset into two arrays (first 25 and last 25 students)
first_25 = marks[:25]
last_25 = marks[25:]

print("\nFirst 25 students:")
print(first_25)

print("\nLast 25 students:")
print(last_25)

# 7. Save dataset to file and load it again
np.savetxt("student_marks.csv", marks, delimiter=",", fmt="%d")

loaded_data = np.loadtxt("student_marks.csv", delimiter=",")

print("\nLoaded data from file:")
print(loaded_data)