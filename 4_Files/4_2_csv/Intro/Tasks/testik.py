import numpy as np

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
index = [2, 3, 6]
new_a = np.delete(a, index)

print(new_a) #Prints `[1, 2, 5, 6, 8, 9]`
