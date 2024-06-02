import matplotlib.pyplot as plt
import matplotlib.patches as patches
from oop_point import Point

class Rectangle(Point):
    
    def __init__(self, x, y, height, width, _axes=None):
        super().__init__(x, y, _axes)
        self.height = height
        self.width = width
        
    def draw(self):
        super().draw()
        rect = patches.Rectangle(
            (self.x, self.y),
            height = self.height,
            width = self.width,
            fc = 'b',
            ec = 'k'
            )
        
        self.axes.add_patch(rect)
        return self.axes
    
if __name__ == "__main__":
        a = Rectangle(3, 3, 2, 3)
        a.draw()
        a.show()