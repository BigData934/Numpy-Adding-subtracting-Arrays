


import numpy as np
from pprint import pprint


array_a = np.array([[1,2,3],[4,5,6]])
array_b = np.array([[3,1,1],[6,5,2]])
print("a:")
pprint(array_a)
print("b:")
pprint(array_b)

print("----")

print("Array a + b:")
a_plus_b = array_a + array_b
pprint(a_plus_b)
print("----")

print("Array a - b:")
a_minus_b = array_a - array_b
pprint(a_minus_b)
print("----")
