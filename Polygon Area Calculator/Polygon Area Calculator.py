class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def __str__(self):
        class_name = type(self).__name__
        return f"{class_name}(width={self.width}, height={self.height})"

    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height 
    
    def get_area(self):
        area = self.width * self.height
        return area

    def get_perimeter(self):
        perimeter = 2 * self.width + 2 * self.height
        return perimeter

    def get_diagonal(self):
        diagonal = ((self.width ** 2 + self.height ** 2) ** 0.5)
        return diagonal

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        line = '*' * self.width + '\n'
        picture = line * self.height
        return picture 

    def get_amount_inside(self, other):
        min_width = self.width // other.width
        min_height = self.height // other.height 
        return min_width*min_height

class Square(Rectangle):
    
    def __init__(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        class_name = type(self).__name__
        return f'{class_name}(side={self.width})'

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, side):
        self.width = side
        self.height = side

    def set_height(self, side):
        self.width = side
        self.height = side
