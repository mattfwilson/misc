class Rectangle:
    def __init__(self, length, width, color):
        self.length = length
        self.width = width
        self.color = color

class Cube(Rectangle):
    def __init__(self, length, width, height, color='bland white'):
        super().__init__(length, width, color)
        self.height = height
    
    def measurements(self):
        return self.length, self.width, self.height

    def volume(self):
        cubeVolume = self.length * self.width * self.height
        return cubeVolume
    
    def printColor(self):
        return self.color

cube1 = Cube(2, 4, 6)
print(f'Your {cube1.printColor()} cube has a length of {cube1.measurements()[0]}, width of {cube1.measurements()[1]}, and a height of {cube1.measurements()[2]}.')
print(f'The volume of your cube is {cube1.volume()}.')
