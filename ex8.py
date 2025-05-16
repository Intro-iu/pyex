import numpy as np
import matplotlib.pyplot as plt
# Chinese for MacOS
plt.rcParams["font.family"] = "Arial Unicode MS"
# 1. 使用 matplotlib 库完成图像的绘制
x = np.linspace(-1, 1, 100)
y = 2*x + 1
plt.plot(x, y)
plt.show()
# 2. 使用 Matplotlib 绘制简单折线图
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
plt.plot(x, y)
plt.show()
# 3. 使用 Matplotlib 绘制条形图
x = ["广东", "北京", "上海", "深圳", "杭州", "天津"]
y = [100, 200, 300, 400, 500, 600]
plt.bar(x, y)
plt.show()
# 4. 使用 Matplotlib 绘制面积图
x = ["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"]
y = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200]
plt.plot(x, y)
plt.fill_between(x, y)
# 5. 完成以下图像的绘制，其中曲线函数y=cos(2 pi t)exp(-t)+0.8;z=0.5cos(x^2)+0.8，标出y在[pi/3, pi]的积分面积
x = np.linspace(0, 6.0, 100)
y = np.cos(2*np.pi*x)*np.exp(-x)+0.8
z = 0.5*np.cos(x**2)+0.8
plt.plot(x, y)
plt.plot(x, z)
plt.fill_between(x, y, z, where=(x>=np.pi/3) & (x<=np.pi), alpha=0.5)
plt.show()