import numpy as np

arr1 = np.array([1, 2, 3, 4, 5, 6, 7])

print("Mean: " + str(np.mean(arr1)))
print("Median: " + str(np.median(arr1)))
print("Standard Deviation: " + str(np.std(arr1)))
print("Variance: " + str(np.var(arr1)))
print("50th percentile: " + str(np.percentile(arr1, 50)))
