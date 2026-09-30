"""HW4 Question 4

Please write a Vector3D class that represents a three-dimensional vector with x, y, and z 
components.

Make sure to write tests in test_q4.py.

Requirements:
- The constructor should initialize the x, y, and z components, all floats.
    For each component, if no value is provided, it should default to 0.0.
- Implement methods for add(other: Vector3D) -> Vector3D, 
    subtract(other: Vector3D) -> Vector3D, and multiply(scalar: float) -> Vector3D.
    Each should return a new Vector3D rather than mutating the current instance.
- Implement the __eq__(other: object) -> bool method to compare two vectors for equality.
    Two Vector3D instances are considered equal if their x, y, and z components are all equal.

Example usage:
v1 = Vector3D(1.0, 2.0, 3.0)
v2 = Vector3D(4.0, 5.0, 6.0)

v3 = v1.add(v2)
v4 = v1.subtract(v2)
v5 = v1.multiply(2.0)

print(v3)  # Vector3D(5.0, 7.0, 9.0)
print(v4)  # Vector3D(-3.0, -3.0, -3.0)
print(v5)  # Vector3D(2.0, 4.0, 6.0)
"""

class Vector3D:
    """Class representing a three-dimensional vector with x, y, and z components."""
