# Create a 4x4 NumPy array of random integers between 10 and 99. Perform the following:

arr = np.random.randint(10, 100, size=(4, 4))
print("Original array:")
print(arr)

# a) Replace all elements greater than 50 with 0.

arr[arr > 50] = 0
print("Array after replacing elements greater than 50 with 0:")
print(arr)

# b) Find the sum of all elements in the array.

sum_of_elements = np.sum(arr)