class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__ (self):
        return f'Rectangle(width={self.width}, height={self.height})'
    
    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        area = (self.width * self.height)
        return area

    def get_perimeter(self):
        perimeter = (2 * self.width + 2 * self.height)
        return perimeter

    def get_diagonal(self):
        diagonal = ((self.width ** 2 + self.height ** 2) ** .5) # Hypotenuse
        return diagonal

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            picture = ''
            for _ in range(self.height):
                picture += f'{"*" * self.width}\n'
            return picture 
        
    def get_amount_inside(self, other_shape):
        fit_width = self.width // other_shape.width # integer division: how many times it fits in width
        fit_height = self.height // other_shape.height # integer division: how many times it fits in height
        return fit_width * fit_height


class Square(Rectangle): # subclass of rectangle

    def __init__(self, side):
        self.side = side
        super().__init__(width = side, height = side)

    def __str__ (self):
        return f'Square(side={self.side})'
    
    # all three should stay in sync
    def set_side(self, side): 
            self.side = side
            self.width = side
            self.height = side
    # preserve the square shape even if someone calls inherited methods.
    def set_width(self, width):
        self.side = width
        self.width = width
        self.height = width
    def set_height(self, height):
        self.side = height
        self.width = height
        self.height = height

r1 = Rectangle(width= 4, height= 6)
print(r1.get_picture())


rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))