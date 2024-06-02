import matplotlib.pyplot as plt #matplotlib라이브러리의 pyplot모듈을 plt로 가져옴
from oop_MObject import MObject

class Point(MObject):

    def __init__(self, x, y, _axes=None): #클래스의 생성자 메서드 정의
        super().__init__(_axes) #MObject의 생성자를 호출하여 객체를 초기화
        self.x = x
        self.y = y
        if _axes != None:  #_axes 값이 있다면 제공된 axes값을 사용함
            self.axes = _axes

    def draw(self):
        self.axes.plot(self.x, self.y, marker='o', c='r')
        return self.axes


if __name__ == "__main__":
    a = Point(3,3)
    a.draw()
    a.show()