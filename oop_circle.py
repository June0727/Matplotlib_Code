import numpy as np
import matplotlib.pyplot as plt

# 방정식의 계수
a = 192.08
b = 176.4
c = 36

# t 값 생성
t_values = np.linspace(-1, 1, 400)

# 방정식 계산
y_values = a * t_values ** 4 + b * t_values ** 2 + c

# 그래프 그리기
plt.plot(t_values, y_values, label='192.08t^4 + 176.4t^2 + 36')
plt.xlabel('t')
plt.ylabel('y')
plt.title('Graph of 192.08t^4 + 176.4t^2 + 36')
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.show()