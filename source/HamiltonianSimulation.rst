.. _HamiltonianSimulation:

哈密顿量模拟
=========================

哈密顿量以威廉·罗文·汉密尔顿（William Rowan Hamilton）命名，他也创造了牛顿力学的革命性改革，现在称为哈米尔顿力学，这在量子物理学中是重要的。
哈密顿量是所有粒子的动能的总和加上与系统相关的粒子的势能。 对于不同的情况或数量的粒子，哈密顿量是不同的，因为它包括粒子的动能之和以及对应于这种情况的势能函数。



指数上的哈密顿量
>>>>>>>>>>>>>>>>

在量子力学中，波函数 :math:`\Psi( |t \rangle)` 的时间演化由含时薛定谔方程控制。

将普朗克常量视为1，将积分上下限分别定为 t、0，并经过一系列数学运算后，可以得到 :math:`\Psi( |t \rangle) = e^{-iHt} \Psi( |0 \rangle)`



哈密顿量模拟的复杂性
>>>>>>>>>>>>>>>>>>>>>>>

哈密顿量（哈密顿算符）在数学上被表示为Hermitian矩阵,而随着qubit数量的增加，其希尔伯特空间是指数增长的，相对应的哈密顿量的维度也是呈指数增长。
因此，需要使用一些近似方法，最简单的近似方法就是在关于矩阵的矩阵的泰勒展开式  :math:`\Psi( |t \rangle) \approx  (I-iHt) \Psi( |0 \rangle)` 
通过更高阶的近似，可以得到更高的精度逼近。


模拟步骤及相关接口介绍
>>>>>>>>>>>>>>>>>>>>>>>

step1:构造相关矩阵；

step2:构造模拟线路；

step3:使用 ``QOperator`` 操作将线路构造成算符操作，并获取线路的对应矩阵；

step4:使用 ``expMat()`` 接口计算 ``e`` 的复数矩阵的真实值；

step5:使用 ``average_gate_fidelity()`` 接口计算两个矩阵的相似度。


示例
>>>>>>>>>>>>>>>>

Pauli-算符模拟
----------------
.. code-block:: python

    import math
    import numpy as np
    import pyqpanda as pq

    if __name__ == "__main__":
        pq.init(pq.QMachineType.CPU)
        q = pq.qAlloc_many(4)

        # 构建pauli 算子
        X = np.mat([[0, 1], [1, 0]])
        Y = np.mat([[0, -1j], [1j, 0]])
        Z = np.mat([[1, 0], [0, -1]])
        t = np.pi

        circuit_x = pq.create_empty_circuit()
        circuit_y = pq.create_empty_circuit()
        circuit_z = pq.create_empty_circuit()

        # 构造Hamiltonian Operator
        circuit_x << pq.H(q[0]) \
                << pq.X(q[0]) \
                << pq.RZ(q[0], -t) \
                << pq.X(q[0]) \
                << pq.RZ(q[0], t) \
                << pq.H(q[0])

        circuit_y << pq.RX(q[0], t / 2) \
                << pq.X(q[0]) \
                << pq.RZ(q[0], -t) \
                << pq.X(q[0]) \
                << pq.RZ(q[0], t) \
                << pq.RX(q[0], -t / 2)

        circuit_z << pq.X(q[0]) \
                << pq.RZ(q[0], -t) \
                << pq.X(q[0]) \
                << pq.RZ(q[0], t)

        operator_x = pq.QOperator(circuit_x)
        operator_y = pq.QOperator(circuit_y)
        operator_z = pq.QOperator(circuit_z)

        unitary_x = operator_x.get_matrix()
        unitary_y = operator_y.get_matrix()
        unitary_z = operator_z.get_matrix()

        conf = complex(0, -1)
        U_x = pq.expMat(conf, X, t)
        U_y = pq.expMat(conf, Y, t)
        U_z = pq.expMat(conf, Z, t)

        f_ave_x = pq.average_gate_fidelity(U_x, unitary_x)
        f_ave_y = pq.average_gate_fidelity(U_y, unitary_y)
        f_ave_z = pq.average_gate_fidelity(U_z, unitary_z)

        print("Pauli-X Average Gate Fidelity: F = {:f}".format(f_ave_x))
        print("Pauli-Y Average Gate Fidelity: F = {:f}".format(f_ave_y))
        print("Pauli-Z Average Gate Fidelity: F = {:f}".format(f_ave_z))


运行结果如下：

::

    Pauli-X Average Gate Fidelity: F = 1.000000
    Pauli-Y Average Gate Fidelity: F = 1.000000
    Pauli-Z Average Gate Fidelity: F = 1.000000