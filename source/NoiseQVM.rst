.. _NoiseQVM:

含噪声量子虚拟机
===================

在真实的量子计算机中，受制于量子比特自身的物理特性，常常存在不可避免的计算误差。为了能在量子虚拟机中更好的模拟这种误差，在 :ref:`QuantumMachine` 的基础上，
QPanda2带来了含噪声量子虚拟机。含噪声量子虚拟机的模拟更贴近真实的量子计算机，我们可以自定义支持的逻辑门类型，自定义逻辑门支持的噪声模型，
通过这些自定义形式，我们使用QPanda2开发量子程序的现实应用程度将更高。

噪声模型介绍
--------------------------------------

DAMPING_KRAUS_OPERATOR
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

DAMPING_KRAUS_OPERATOR是量子比特的弛豫过程噪声模型，它的kraus算符和表示方法如下所示：

:math:`K_1 = \begin{bmatrix} 1 & 0 \\ 0 & \sqrt{1 - p} \end{bmatrix},   K_2 = \begin{bmatrix} 0 & \sqrt{p} \\ 0 & 0 \end{bmatrix}`

需要一个噪声参数。

DEPHASING_KRAUS_OPERATOR
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

DEPHASING_KRAUS_OPERATOR是量子比特的退相位过程噪声模型，它的kraus算符和表示方法如下所示：

:math:`K_1 = \begin{bmatrix} \sqrt{1 - p} & 0 \\ 0 & \sqrt{1 - p} \end{bmatrix},   K_2 = \begin{bmatrix} \sqrt{p} & 0 \\ 0 & -\sqrt{p} \end{bmatrix}`

需要一个噪声参数。

DECOHERENCE_KRAUS_OPERATOR
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

DECOHERENCE_KRAUS_OPERATOR是退相干噪声模型，为上述两种噪声模型的综合，他们的关系如下所示：

:math:`P_{damping} = 1 - e^{-\frac{t_{gate}}{T_1}}, P_{dephasing} = 0.5 \times (1 - e^{-(\frac{t_{gate}}{T_2} - \frac{t_{gate}}{2T_1})})`

:math:`K_1 = K_{1_{damping}}K_{1_{dephasing}}, K_2 = K_{1_{damping}}K_{2_{dephasing}},`

:math:`K_3 = K_{2_{damping}}K_{1_{dephasing}}, K_4 = K_{2_{damping}}K_{2_{dephasing}}`

需要三个噪声参数。

DEPOLARIZING_KRAUS_OPERATOR
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

DEPOLARIZING_KRAUS_OPERATOR去极化噪声模型，即单量子比特有一定的概率被完全混合态I/2代替, 它的kraus算符和表示方法如下所示：

:math:`K_1 = \sqrt{1 - 3p/4} × I, K_2 = \sqrt{p}/2 × X` 

:math:`K_3 = \sqrt{p}/2 × Y, K_4 = \sqrt{p}/2 × Z`

其中I、X、Y、Z分别代表其量子逻辑门对应的矩阵

需要一个参数

BITFLIP_KRAUS_OPERATOR
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

BITFLIP_KRAUS_OPERATOR是比特反转噪声模型，它的kraus算符和表示方法如下所示：

:math:`K_1 = \begin{bmatrix} \sqrt{1 - p} & 0 \\ 0 & \sqrt{1 - p} \end{bmatrix}, K_2 = \begin{bmatrix} 0 & \sqrt{p} \\ \sqrt{p} & 0 \end{bmatrix}`

需要一个噪声参数。

BIT_PHASE_FLIP_OPRATOR
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

BIT_PHASE_FLIP_OPRATOR是比特-相位反转噪声模型，它的kraus算符和表示方法如下所示：

:math:`K_1 = \begin{bmatrix} \sqrt{1 - p} & 0 \\ 0 & \sqrt{1 - p} \end{bmatrix}, K_2 = \begin{bmatrix} 0 & -i \times \sqrt{p} \\ i \times \sqrt{p} & 0 \end{bmatrix}`

需要一个噪声参数。

PHASE_DAMPING_OPRATOR
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PHASE_DAMPING_OPRATOR是相位阻尼噪声模型，它的kraus算符和表示方法如下所示：

:math:`K_1 = \begin{bmatrix} 1 & 0 \\ 0 & \sqrt{1 - p} \end{bmatrix}, K_2 = \begin{bmatrix} 0 & 0 \\ 0 & \sqrt{p} \end{bmatrix}`

需要一个噪声参数。

双门噪声模型
>>>>>>>>>>>>>>

双门噪声模型同样也分为六种：DAMPING_KRAUS_OPERATOR、DEPHASING_KRAUS_OPERATOR、DECOHERENCE_KRAUS_OPERATOR、DEPOLARIZING_KRAUS_OPERATOR、BITFLIP_KRAUS_OPERATOR、BIT_PHASE_FLIP_OPRATOR、PHASE_DAMPING_OPRATOR。
它们的输入参数与单门噪声模型一致，双门噪声模型的kraus算符和表示与单门噪声模型存在着对应关系：假设单门噪声模型为： :math:`\{ K1, K2 \}` ，那么对应的双门噪声模型为
:math:`\{K1\otimes K1, K1\otimes K2, K2\otimes K1, K2\otimes K2\}`。


接口介绍
------------

pyqpanda当前支持的噪声模型

.. code-block:: python

    class NoiseModel(__pybind11_builtins.pybind11_object):
        """
        Members:
        
        DAMPING_KRAUS_OPERATOR
        
        DECOHERENCE_KRAUS_OPERATOR
        
        DEPHASING_KRAUS_OPERATOR
        
        PAULI_KRAUS_MAP
        
        DECOHERENCE_KRAUS_OPERATOR_P1_P2
        
        BITFLIP_KRAUS_OPERATOR
        
        DEPOLARIZING_KRAUS_OPERATOR
        
        BIT_PHASE_FLIP_OPRATOR
        
        PHASE_DAMPING_OPRATOR
        """

设置量子逻辑门噪声模型的接口如下：

     .. code-block:: python

        set_noise_model(NoiseModel model, GateType type, list params_vec)

第一个参数为噪声模型类型，第二个参数为量子逻辑门类型，第三个参数为噪声模型所需的参数。

假设希望设定RX,RY的噪声模型为DECOHERENCE_KRAUS_OPERATOR，CNOT的噪声模型为DEPHASING_KRAUS_OPERATOR，可以按下面的方式构建量子虚拟机：

    .. code-block:: python

        qvm = NoiseQVM()
        qvm.set_noise_model(NoiseModel.DECOHERENCE_KRAUS_OPERATOR, GateType.RX_GATE, [5.0, 2.0, 0.03]) # T1: 5.0, T2: 2.0, t_gate: 0.03
        qvm.set_noise_model(NoiseModel.DECOHERENCE_KRAUS_OPERATOR, GateType.RY_GATE, [5.0, 2.0, 0.03])
        qvm.set_noise_model(NoiseModel.DECOHERENCE_KRAUS_OPERATOR, GateType.CNOT_GATE, [5.0, 2.0, 0.06])
        qvm.init_qvm()

含噪声虚拟机还支持设置设置带有角度的量子逻辑门的转转角度误差，其接口使用方式如下：

    .. code-block:: python

        qvm.set_rotation_angle_error(0.1)

即设置角度旋转误差为0.1。

含噪声虚拟机同样支持直接设置KRAUS矩阵的方法，其接口使用方式如下：
    
    .. code-block:: python

        prob = 0.05
        k1 = [1 - prob,0,0,1 - prob]
        k2 = [0, complex(0, -np.sqrt(prob)), complex(0, np.sqrt(prob)), 0]
        noise = [k1, k2]
        machine.set_noise_kraus_matrix(GateType.PAULI_X_GATE, noise)
     
即设置KRAUS矩阵k1，k2。

含噪声虚拟机更加支持直接设置自定义酉矩阵以及矩阵对应概率的方法，其接口使用方式如下：

    .. code-block:: python
    
        prob = 0.05
        matrix_i = [ 1, 0, 0, 1 ];
        matrix_x = [ 0, 1, 1, 0 ];
        machine.set_noise_unitary_matrix(GateType.PAULI_X_GATE, [matrix_i, matrix_x], [1-prob, prob]);

即设置自定义矩阵列表以及对应的概率列表。

实例
------------

    .. code-block:: python

        from pyqpanda import *
        import numpy as np

        if __name__ == "__main__":
            qvm = NoiseQVM()

            # 设置噪声模型参数
            noise_rate = 0.001
            qvm.set_noise_model(NoiseModel.DEPHASING_KRAUS_OPERATOR, GateType.RX_GATE, [noise_rate])
            qvm.set_noise_model(NoiseModel.DEPHASING_KRAUS_OPERATOR, GateType.CNOT_GATE, [2 * noise_rate])

            # 设置角度旋转误差为0.1
            qvm.set_rotation_angle_error(0.1)

            qvm.init_qvm()
            qubits = qvm.qAlloc_many(4)
            cbits = qvm.cAlloc_many(4)

            # 构建量子程序
            prog = QProg()
            for i in range(0, len(qubits)):
                prog.insert(H(qubits[i]))

            for i in range(0, len(qubits) - 1):
                prog.insert(CNOT(qubits[i], qubits[i + 1]))
            
            prog.insert(measure_all(qubits, cbits))

            # 量子程序运行1000次，并返回测量结果
            result = qvm.run_with_configuration(prog, cbits, 1000)

            # 打印量子态在量子程序多次运行结果中出现的次数
            print(result)

            qvm.finalize()

运行结果：

    .. code-block:: python

        {'0000': 56, '0001': 60, '0010': 68, '0011': 59, '0100': 58, '0101': 71, '0110': 62, '0111': 63, '1000': 67, '1001': 74, '1010': 65, '1011': 58, '1100': 61, '1101': 61, '1110': 58, '1111': 59}
