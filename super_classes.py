class Rectangle:
    def __init__(self, length, width, color):
        self.length = length
        self.width = width
        self.color = color

class Cube(Rectangle):
    def __init__(self, length, width, height, color='bland white'):
        super().__init__(length, width, color)
        self.height = height

    def volume(self):
        cubeVolume = self.length * self.width * self.height
        return cubeVolume
    
    def printColor(self):
        return self.color

cube1 = Cube(2, 4, 6, 'sky blue')

if cube1.color == "sky blue":
    print(f'Your {cube1.color} cube has a length of {cube1.length}, width of {cube1.width}, and a height of {cube1.height}.')
    print(f'The volume of your cube is {cube1.volume()}.')
else:
    print(f'Your cube has no specified color but has a length of {cube1.length}, width of {cube1.width}, and a height of {cube1.height}.')
    print(f'The volume of your cube is {cube1.volume()}.')


