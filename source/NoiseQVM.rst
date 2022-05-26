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

双门噪声模型同样也分为上述几种：DAMPING_KRAUS_OPERATOR、DEPHASING_KRAUS_OPERATOR、DECOHERENCE_KRAUS_OPERATOR、DEPOLARIZING_KRAUS_OPERATOR、BITFLIP_KRAUS_OPERATOR、BIT_PHASE_FLIP_OPRATOR、PHASE_DAMPING_OPRATOR。
它们的输入参数与单门噪声模型一致，双门噪声模型的kraus算符和表示与单门噪声模型存在着对应关系：假设单门噪声模型为： :math:`\{ K1, K2 \}` ，那么对应的双门噪声模型为
:math:`\{K1\otimes K1, K1\otimes K2, K2\otimes K1, K2\otimes K2\}`。


接口介绍
------------

pyqpanda当前支持的噪声模型

    .. code-block:: CMakeLists

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

设置一个噪声参数的使用方法如下：

    .. code-block:: python

        from pyqpanda import *
        import numpy as np

        qvm = NoiseQVM()
        qvm.init_qvm()
        q = qvm.qAlloc_many(4)
        c = qvm.cAlloc_many(4)
        
        # 未指定作用比特则对所有比特生效
        qvm.set_noise_model(NoiseModel.BITFLIP_KRAUS_OPERATOR, GateType.PAULI_X_GATE, 0.1)
        # 制定比特时，仅对指定的比特生效
        qvm.set_noise_model(NoiseModel.BITFLIP_KRAUS_OPERATOR, GateType.RY_GATE, 0.1, [q[0], q[1]])
        # 双门指定比特时, 需要同时指定两个比特，且对比特的顺序敏感
        qvm.set_noise_model(NoiseModel.DAMPING_KRAUS_OPERATOR, GateType.CNOT_GATE, 0.1, [[q[0], q[1]], [q[1], q[2]]])

第一个参数为噪声模型类型，第二个参数为量子逻辑门类型，第三个参数为噪声模型所需的参数。

设置三个噪声参数的使用方法如下：

    .. code-block:: python

        # 未指定作用比特则对所有比特生效
        qvm.set_noise_model(NoiseModel.DECOHERENCE_KRAUS_OPERATOR, GateType.PAULI_Y_GATE, 5, 2, 0.01)
        # 制定比特时，仅对指定的比特生效
        qvm.set_noise_model(NoiseModel.DECOHERENCE_KRAUS_OPERATOR, GateType.Y_HALF_PI, 5, 2, 0.01, [q[0], q[1]])
        # 双门指定比特时, 需要同时指定两个比特，且对比特的顺序敏感
        qvm.set_noise_model(NoiseModel.DECOHERENCE_KRAUS_OPERATOR, GateType.CZ_GATE, 5, 2, 0.01, [[q[0], q[1]], [q[1], q[0]]])


含噪声虚拟机还支持设置设置带有角度的量子逻辑门的转转角度误差，其接口使用方式如下：

    .. code-block:: python

        qvm.set_rotation_error(0.05)

即设置角度旋转误差为0.05。

设置测量误差, 其使用方法与上面的方法类似，只不过不需要指定量子逻辑门的类型

    .. code-block:: python

        qvm.set_measure_error(NoiseModel.DEPOLARIZING_KRAUS_OPERATOR, 0.1)   

设置reset噪声：

    .. code-block:: python

        p0 = 0.9
        p1 = 0.05
        qvm.set_reset_error(p0, p1)  
    
p0 表示重置到 :math:`\left|0\right\rangle`\ 的概率，p1表示重置到 :math:`\left|1\right\rangle`\ 的概率，未被重置的概率为 1-p0-p1

设置读取误差：

    .. code-block:: python

        f0 = 0.9
        f1 = 0.85
        qvm.set_readout_error([[f0, 1 - f0], [1 - f1, f1]])

表示在读取q0时0读为0的概率为0.9，读为1的概率为1 - f0，
1读为1的概率为0.85，读为0的概率为1 - f1

实例
------------

    .. code-block:: python

        from pyqpanda import *
        import numpy as np

        if __name__ == "__main__":
            qvm = NoiseQVM()
            qvm.init_qvm()
            q = qvm.qAlloc_many(4)
            c = qvm.cAlloc_many(4)

            qvm.set_noise_model(NoiseModel.BITFLIP_KRAUS_OPERATOR, GateType.PAULI_X_GATE, 0.1)
            qv0 = [q[0], q[1]]
            qvm.set_noise_model(NoiseModel.DEPHASING_KRAUS_OPERATOR, GateType.HADAMARD_GATE, 0.1, qv0)
            qves = [[q[0], q[1]], [q[1], q[2]]]
            qvm.set_noise_model(NoiseModel.DAMPING_KRAUS_OPERATOR, GateType.CNOT_GATE, 0.1, qves)

            f0 = 0.9
            f1 = 0.85
            qvm.set_readout_error([[f0, 1 - f0], [1 - f1, f1]])
            qvm.set_rotation_error(0.05)

            prog = QProg()
            prog << X(q[0]) << H(q[0]) \
                 << CNOT(q[0], q[1]) \
                 << CNOT(q[1], q[2]) \
                 << CNOT(q[2], q[3]) \
                 << measure_all(q, c)

            result = qvm.run_with_configuration(prog, c, 1000)
            print(result)

运行结果：

    .. code-block:: python

        {'0000': 347, '0001': 55, '0010': 50, '0011': 43, '0100': 41, '0101': 18, '0110': 16, '0111': 34, '1000': 50, '1001': 18, '1010': 18, '1011': 37, '1100': 15, '1101': 49, '1110': 42, '1111': 167}
