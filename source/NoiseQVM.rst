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

DECOHERENCE_KRAUS_OPERATOR_P1_P2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

DECOHERENCE_KRAUS_OPERATOR_P1_P2是上述两种噪声模型的综合，他们的关系如下所示：

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

双门噪声模型同样也分为三种：DOUBLE_DAMPING_KRAUS_OPERATOR、DOUBLE_DEPHASING_KRAUS_OPERATOR、DOUBLE_DECOHERENCE_KRAUS_OPERATOR。
它们的输入参数与单门噪声模型一致，双门噪声模型的kraus算符和表示与单门噪声模型存在着对应关系：假设单门噪声模型为： :math:`\{ K1, K2 \}` ，那么对应的双门噪声模型为
:math:`\{K1\otimes K1, K1\otimes K2, K2\otimes K1, K2\otimes K2\}`。


接口介绍
------------

含噪声量子虚拟机的接口和其他量子虚拟机的接口大部分是相同的，但含噪声量子虚拟机不能使用PMEASURE系列的概率测量接口。此外QPanda2给它重载了一个init成员函数，
该成员函数可接收一个dict类型的参数，我们可以在参数中定义含噪声量子虚拟机支持的量子逻辑门类型和
噪声模型，dict的结构如下所示：

     .. code-block:: c

              {
                  “gates”:[.....],
                  "noisemodel":{.....}}              
              }

假设我们希望自定含噪声量子虚拟机支持的逻辑门是RX、RY、CNOT，并且希望设定RX,RY的噪声模型为DECOHERENCE_KRAUS_OPERATOR，那么我们把dict构造成以下形式：

     .. code-block:: c

              {
                  “gates”:[["RX","RY"],["CNOT"]],
                  "noisemodel":{"RX":[DECOHERENCE_KRAUS_OPERATOR,10.0,2.0,0.03],
                                "RY":[DECOHERENCE_KRAUS_OPERATOR,10.0,2.0,0.03]}}              
              }

这里先举个pyQPanda使用的例子：

     .. code-block:: python
          
	            dict = {"gates":[["RX","RY"],["CNOT"]],
                    "noisemodel":{"RX":[NoiseModel.DECOHERENCE_KRAUS_OPERATOR,10.0,2.0,0.03],
                                  "RY":[NoiseModel.DECOHERENCE_KRAUS_OPERATOR,10.0,2.0,0.03]
		    	    			 }
		                }              
	    
                qvm = NoiseQVM() 
                qvm.initQVM(dict)

实例
------------

    .. code-block:: python

        from pyqpanda import *
        import numpy as np

        if __name__ == "__main__":
            qvm = NoiseQVM();
            noise_rate = 0.001
            doc = {'noisemodel': {'H': [NoiseModel.DEPHASING_KRAUS_OPERATOR, noise_rate],
            'CNOT' : [NoiseModel.DEPHASING_KRAUS_OPERATOR, 2 * noise_rate]}}

            qvm.init_qvm(doc)
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
