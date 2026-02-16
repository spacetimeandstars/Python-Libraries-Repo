# 3. Given the 2D array arr = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])

import numpy as np
arr = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])
print("Original array:")
print(arr)

# a) Extract the first two rows and the last column.

extracted = arr[:2, -1:]
print("Extracted first two rows and last column:")
print(extracted)

# b) Modify the second row to contain [1, 2, 3].

arr[1] = [1, 2, 3]

# c) Print the updated array.

print("Updated array:")