import matplotlib.pyplot as plt  #matplotlib에서 pyplot모듈을 가져옴

class MObject:  #MObject 클래스를 정의
    
    def __init__(self,_axes=None):  #클래스 생성자 method define
        self.figure = None 
        self.axes = None
        if self.axes == None:
            if _axes == None:
                self.figure, self.axes = plt.subplots(  #ax값이 지정이 안되있으면 5,5 로 지정함
                    figsize=(5,5)
                )
                 # self.fig = plt.figure(
                #     figsize=(5,5),
                #     facecolor = 'w',
                # )
                # self.axes = self.fig.add_axes(
                #     (0.1,0.1,0.8,0.8),
                # )
            else:
                self.axes = _axes  #ax값이 지정되있으면 그 값을 사용함
        else:
            if _axes == None:  #ax값이 전달되지 않았으면 아무 작업도 수행하지 않음
                pass
            else:
                self.axes = _axes

    def draw(self):  #
        pass # to be implemented

    def __call__(self):
        return self.draw()

    def show(self):
        plt.show()