import numpy as np
import pandas as pd

arr1 = np.array([[1,2,3],[4,5,6]])

arr2 = np.array([[7,8,9],[10,11,12]])

arr = np.concatenate((arr1,arr2),axis = 1)

print(arr)

def print_all(arr1, arr2, arr):
    print(arr1)
    print(arr2)
    print(arr)