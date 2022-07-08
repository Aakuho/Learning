class Vector:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self) -> str: 
        return f"x: {self.x}, y: {self.y}"

    def __len__(self):
        return 10 # im lazy

    def __call__(self):
        print("Class 'Vector' has been called")

v2 = Vector(12, 5)