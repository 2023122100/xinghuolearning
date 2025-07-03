import numpy as np
from math import cos, sin, factorial


def exp_i_pauli(sigma):
        return cos(1) * np.eye(2) + 1j *sin(1) * sigma

def verify_ex():
    sigma_x = np.array([[0, 1], [1, 0]], dtype=complex)
    sigma_y = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sigma_z = np.array([[1, 0], [0, -1]], dtype=complex)

    #def e^...
    

    exp_i_sigma_x = exp_i_pauli(sigma_x)
    exp_i_sigma_y = exp_i_pauli(sigma_y)
    exp_i_sigma_z = exp_i_pauli(sigma_z)

    print("e^{i sigma_x} =")
    print(exp_i_sigma_x)
    print("\ne^{i sigma_y} =")
    print(exp_i_sigma_y)
    print("\ne^{i sigma_z} =")
    print(exp_i_sigma_z)


# e^{iθP} 
def exp_taylor(P, theta, N=20):
    result = np.zeros_like(P, dtype=complex)
    for k in range(N):
        term = (1j * theta)**k / factorial(k) * np.linalg.matrix_power(P, k)
        result += term
    return result

# 解析公式
def exp_analytic(P, theta):
    return cos(theta) * np.eye(2) + 1j * sin(theta) * P

def taylor():
    sigma_x = np.array([[0, 1], [1, 0]], dtype=complex)
    sigma_y = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sigma_z = np.array([[1, 0], [0, -1]], dtype=complex)

    # 测试 theta = 1
    theta = 1.0
    P = sigma_x  

    # 泰勒级数计算
    exp_taylor_P = exp_taylor(P, theta, N=20)
    print("泰勒级数展开 (N=20):\n", exp_taylor_P)

    # 解析公式计算
    exp_analytic_P = exp_analytic(P, theta)
    print("\n解析公式计算:\n", exp_analytic_P)

    # 比较误差
    error = np.linalg.norm(exp_taylor_P - exp_analytic_P)
    print("\n误差 (Frobenius 范数):", error)

def main():
    verify_ex()
    taylor()
  

if __name__ == "__main__":
    main()


# 若P^是幂零矩阵（如P^**2=0），则泰勒级数会在有限项终止，结果为：e**i(theta)P^ = I + i(theta)P^