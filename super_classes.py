inventory = []

class Rectangle:
    def __init__(self, length, width, color):
        self.id = id
        self.length = length
        self.width = width
        self.color = color

class Cube(Rectangle):

    def __init__(self, length, width, height, color='bland white'):
        super().__init__(length, width, color)
        self.height = height
        inventory.append(self)

    def volume(self):
        cubeVolume = self.length * self.width * self.height
        return cubeVolume
    
    def __repr__(self):
        return f'Cube height: {self.height}'

cube1 = Cube(2, 4, 6, 'sky blue')
cube2 = Cube(50, 100, 777, 'crystal clear')
cube3 = Cube(1, 1, 1, 'neon pink')

print(inventory)

if cube1.color == "sky blue":
    print(f'Your {cube1.color} cube has a length of {cube1.length}, width of {cube1.width}, and a height of {cube1.height}.')
    print(f'The volume of your cube is {cube1.volume()}.')
else:
    print(f'Your cube has no specified color but has a length of {cube1.length}, width of {cube1.width}, and a height of {cube1.height}.')
    print(f'The volume of your cube is {cube1.volume()}.')


