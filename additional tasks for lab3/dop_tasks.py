class MyShape:
    def __init__(self, color="DefaultColor", is_filled=True):
        self.color = color
        self.is_filled = is_filled

    def __str__(self):
        return f"MyShape: Color={self.color}, IsFilled={self.is_filled}"

    def getArea(self):
        return 0


class Rectangle(MyShape):
    def __init__(self, color="DefaultColor", is_filled=True, x_top_left=0, y_top_left=0, length=1, width=1):
        super().__init__(color, is_filled)
        self.x_top_left = x_top_left
        self.y_top_left = y_top_left
        self.length = length
        self.width = width

    def getArea(self):
        return self.length * self.width

    def __str__(self):
        return f"Rectangle: Color={self.color}, IsFilled={self.is_filled}, X={self.x_top_left}, Y={self.y_top_left}, Length={self.length}, Width={self.width}"


class Circle(MyShape):
    def __init__(self, color="DefaultColor", is_filled=True, x_center=0, y_center=0, radius=1):
        super().__init__(color, is_filled)
        self.x_center = x_center
        self.y_center = y_center
        self.radius = radius

    def getArea(self):
        return 3.14159 * self.radius**2  # Assuming pi as 3.14159

    def __str__(self):
        return f"Circle: Color={self.color}, IsFilled={self.is_filled}, X={self.x_center}, Y={self.y_center}, Radius={self.radius}"


# Console input for creating a Rectangle
def create_rectangle_from_input():
    color = input("Enter color for Rectangle: ")
    is_filled = input("Is the Rectangle filled? (True/False): ").lower() == 'true'
    x_top_left = float(input("Enter X coordinate of the top-left corner: "))
    y_top_left = float(input("Enter Y coordinate of the top-left corner: "))
    length = float(input("Enter length of the Rectangle: "))
    width = float(input("Enter width of the Rectangle: "))

    return Rectangle(color, is_filled, x_top_left, y_top_left, length, width)