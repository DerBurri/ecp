import numpy as np

def euclidean_distance(x1, x2):
    return np.sqrt(np.sum((x1-x2)**2))
# Test case 1: Same point
a = np.array([1, 2, 3])
b = np.array([1, 2, 3])
expected_output = 0.0
output = euclidean_distance(a, b)
assert np.isclose(output, expected_output), f"Test case 1 failed: Expected {expected_output}, but got {output}"

# Test case 2: Different points
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
expected_output = np.sqrt(27)
output = euclidean_distance(a, b)
assert np.isclose(output, expected_output), f"Test case 2 failed: Expected {expected_output}, but got {output}"

# Test case 3: Zero vector
a = np.array([0, 0, 0])
b = np.array([1, 2, 3])
expected_output = np.sqrt(14)
output = euclidean_distance(a, b)
assert np.isclose(output, expected_output), f"Test case 3 failed: Expected {expected_output}, but got {output}"

# Test case 4: Negative values
a = np.array([-1, -2, -3])
b = np.array([4, 5, 6])
expected_output = np.sqrt(99)
output = euclidean_distance(a, b)
assert np.isclose(output, expected_output), f"Test case 4 failed: Expected {expected_output}, but got {output}"

print("All test cases passed!")# Test case 5: Random points
a = np.array([1, 2, 3])
b = np.array([7, 8, 9])
expected_output = np.sqrt(108)
output = euclidean_distance(a, b)
assert np.isclose(output, expected_output), f"Test case 5 failed: Expected {expected_output}, but got {output}"

# Test case 6: Large vectors
a = np.array([1000, 2000, 3000])
b = np.array([4000, 5000, 6000])
expected_output = np.sqrt(27000000)
output = euclidean_distance(a, b)
assert np.isclose(output, expected_output), f"Test case 6 failed: Expected {expected_output}, but got {output}"

# Test case 7: Negative values
a = np.array([-1, -2, -3])
b = np.array([-4, -5, -6])
expected_output = np.sqrt(27)
output = euclidean_distance(a, b)
assert np.isclose(output, expected_output), f"Test case 7 failed: Expected {expected_output}, but got {output}"

print("All additional test cases passed!")