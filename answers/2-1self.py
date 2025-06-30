# import
import numpy as np
import matplotlib.pyplot as plt

#def旋转矩阵
def rotation_matrix(theta):
    return np.array([
        [np.cos(theta), np.sin(theta)],
        [-np.sin(theta), np.cos(theta)]
    ])

#初始向量
v = np.array([1, 0])

#建图
plt.figure(figsize=(8, 8))
ax = plt.gca()

#创原始向量
ax.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color='black', label='Original vector (1, 0)')

#不同旋转角度
angles = [np.pi/6, np.pi/4, np.pi/3, np.pi/2]
colors = ['red', 'pink', 'green', 'blue']
#计算旋转后向量
for theta, color in zip(angles, colors):
    R = rotation_matrix(theta)
    v_rotated = R @ v
#绘图
    ax.quiver(0, 0, v_rotated[0], v_rotated[1], angles='xy', scale_units='xy', scale=1, 
             color=color, label=f'Rotated by {theta/np.pi:.2f}π radians ({np.degrees(theta):.0f}°)')

#坐标轴绘制
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')
ax.grid(True)
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
plt.title('Vector Rotation by R(θ)')
plt.legend()
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()