#encoding=utf-8  
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score


# x、y 座標
x = np.arange(1, 5, 1)
num = [1, 2.1, 3, 4]
y = np.array(num)

# 多項式擬合
f1 = np.polyfit(x, y, 1)
p1 = np.poly1d(f1)
print(p1)
print(p1[1])
print(p1[0])

#擬合y值
yvals = p1(x) 

# 計算 r2_score
r2=r2_score(num,yvals)
print(r2)

#繪圖
plot1 = plt.plot(x, y, 's',label='Data')
plot2 = plt.plot(x, yvals, 'r',label='polyfit values')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc=2) #指定legend的位置左上角
plt.title('Linear Fit')
plt.show()
