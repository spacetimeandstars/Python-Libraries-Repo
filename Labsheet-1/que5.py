# 5. a) Create two arrays arr1 and arr2 of shapes (2, 3) and (2, 2), respectively.

import numpy as np
arr1 = np.random.randint(1, 10, size=(2, 3))
arr2 = np.random.randint(1, 10, size=(2, 2))

# b) Concatenate them horizontally to create a new array.

concatenated = np.concatenate((arr1, arr2), axis=1)
print("Concatenated array:")
print(concatenated)

# c) Split the concatenated array into two equal parts along the columns.

split_arrays = np.hsplit(concatenated, 2)
print("Split arrays:")
for i, part in enumerate(split_arrays):
    print(f"Part {i+1}:")
    print(part)