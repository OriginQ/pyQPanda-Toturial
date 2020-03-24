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

:math:`K_1 = \begin{bmatrix} \sqrt{1 - p} & 0 \\ 0 & \sqrt{1 - p} \end{bmatrix},   K_2 = \begin{bmatrix} 0 & \sqrt{p} \\ 0 & 0 \end{bmatrix}`

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

双门噪声模型同样也分为六种：DAMPING_KRAUS_OPERATOR、DEPHASING_KRAUS_OPERATOR、DECOHERENCE_KRAUS_OPERATOR_P1_P2、BITFLIP_KRAUS_OPERATOR、BIT_PHASE_FLIP_OPRATOR、PHASE_DAMPING_OPRATOR。
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

实例
------------

    .. code-block:: python

        from pyqpanda import *
        import numpy as np

        if __name__ == "__main__":
            qvm = NoiseQVM()
            noise_rate = 0.001
            qvm.set_noise_model(NoiseModel.DEPHASING_KRAUS_OPERATOR, GateType.RX_GATE, [noise_rate])
            qvm.set_noise_model(NoiseModel.DEPHASING_KRAUS_OPERATOR, GateType.CNOT_GATE, [2 * noise_rate])

            qvm.init_qvm()
            qubits = qvm.qAlloc_many(4)
            cbits = qvm.cAlloc_many(4)

            prog = QProg()
            for i in range(0, len(qubits)):
                prog.insert(H(qubits[i]))

            for i in range(0, len(qubits) - 1):
                prog.insert(CNOT(qubits[i], qubits[i + 1]))
            
            prog.insert(measure_all(qubits, cbits))
            config = {'shots': 1000}
            result = qvm.run_with_configuration(prog, cbits, config)
            qvm.finalize()
            print(result)

运行结果：

    .. code-block:: python

        {'0000': 55, '0001': 59, '0010': 71, '0011': 64, '0100': 56, '0101': 67, '0110': 60, '0111': 57, '1000': 72, '1001': 73, '1010': 70, '1011': 68, '1100': 57, '1101': 56, '1110': 55, '1111': 60}
