

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Sobrecarga del operador +
    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented
    
    # Representación del objeto
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

# Instancias de Vector
v1 = Vector(1, 2)
v2 = Vector(3, 4)

# Sobrecarga del operador +
v3 = v1 + v2
print(v3)  # Vector(4, 6)