import numpy as np
import matplotlib.pyplot as plt

# パラメータ b を設定
b = 1.0

# x を 0 と 1 の間(排他的)で細かく取る
# log( x/(1-x) ) は x=0,1 で発散するため、極端に0や1に近い点は避ける
x = np.linspace(0.0001, 0.9999, 500)

# y = log(x/(1-x)) + b を計算
y = np.log(x/(1 - x)) + b

# プロット
plt.figure(figsize=(6, 4))
plt.plot(x, y, label=r'$y = \ln\left(\frac{x}{1-x}\right) + b$')

# 軸ラベルなどを設定
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()