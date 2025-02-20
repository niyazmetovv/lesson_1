import math


class Vector():
    #constructor
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    #to print out
    def __str__(self):
        return f'({self.x}, {self.y}, {self.z})'
    #to add
    def __add__(self, other):
       if isinstance(other, Vector):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
       else:
           return "Invalid input"
    #to sub
    def __sub__(self, other):
        if isinstance(other, Vector):
         return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
        else:
            return "Invalid input"

        # dot product
    def dot(self, other):
            if isinstance(other, Vector):
                return self.x * other.x + self.y * other.y + self.z * other.z
            else:
                return "Invalid input"
    #to multiply (scalar)
    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.dot(other)
        elif isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other, self.z * other)
        else:
            return"Invalid input"

    #to divide
    def __truediv__(self, other):
      if isinstance(other, Vector):
        return Vector(self.x / other.x, self.y / other.y, self.z / other.z)
      else:
          return "Invalid input"
    #magnitude
    def magnitude(self):
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    #normalize
    def normalize(self):
        magnitude = self.magnitude()
        if magnitude == 0:
            return "Invalid input"
        return Vector(round(self.x / magnitude, 3),
                      round(self.y / magnitude, 3),
                      round(self.z / magnitude, 3))
    def __rmul__(self, other):
        return self * other


# Create vectors
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

# Print the vector
print(v1)

# Addition
v3 = v1 + v2
print(v3)

# Subtraction
v4 = v2 - v1
print(v4)

# Dot product
dot_product = v1 * v2
print(dot_product)

# Scalar multiplication
v5 = 3 * v1
print(v5)

# Magnitude
print(v1.magnitude())

# Normalization
v_unit = v1.normalize()
print(v_unit)
