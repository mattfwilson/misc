cubeVolume = 2

class Rectangle:
    def __init__(self, length, width, color):
        self.length = length
        self.width = width
        self.color = color

class Square(Rectangle):
    def __init__(self, length, width, color):
        super().__init__(length, width, color)

    def area(self):
        return self.length * self.width

class Cube(Rectangle):
    def __init__(self, length, width, height, color):
        super().__init__(length, width, color)
        self.height = height
    
    def volume(self):
        cubeVolume = self.length * self.width * self.height
        return cubeVolume
    
    def printColor(self, color):
        return color

square1 = Square(8, 5, 'Blue')
print(square1.area())

cube1 = Cube(2, 4, 6, 'Green')
print(cube1.printColor('Red'))