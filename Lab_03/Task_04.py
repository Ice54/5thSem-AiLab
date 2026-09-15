import pandas as pd
import numpy as np

arr1=np.array([1,2,3,4,5,6,7,8,9,10])
arr2 =np.array([11, 8, 7, 5, 6, 5, 3, 4, 7, 1])

euclidean_distance = np.sqrt(np.sum(np.square(arr1-arr2)))

print("Euclidean Distance= " + str(euclidean_distance))