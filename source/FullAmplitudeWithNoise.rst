.. _QuantumMachine:

全振幅量子虚拟机噪声模拟
=========================

在真实的量子计算机中，受制于量子比特自身的物理特性，常常存在不可避免的计算误差。为了能在量子虚拟机中更好的模拟这种误差，在全振幅虚拟机中，
支持对噪声进行模拟，含噪声模拟的量子虚拟机更贴近真实的量子计算机。我们可以自定义噪声类型影响到的量子比特，自定义逻辑门支持的噪声模型，
通过这些自定义形式，我们使用QPanda2开发量子程序的现实应用程度将更高。

物理背景
--------------------------------------
纯态，混合态
>>>>>>>>>>>>>>>>
量子计算中，量子比特使用态矢来表示，在没有噪声的理想状态下，量子比特在逻辑门的演化下一直处于纯态(pure state)：

.. math::
    \begin{aligned}
    |\psi \rangle = |\varphi\rangle = \alpha|0\rangle + \beta|1\rangle
    \end{aligned}

当有噪声干扰时，系统会演化到混合态(mixed state)。混合态 :math:`|\psi\rangle` 无法使用纯态的线性叠加来表示，通常用系综(ensemble)来表示：

.. math::

   \begin{aligned}
	 \{|\varphi_1\rangle, |\varphi_2\rangle, ..., |\varphi_n\rangle\} \\
	 \{p_1, p_2, ..., p_n\}
   \end{aligned}
	
系统 :math:`|\psi\rangle` 的最终状态，以 :math:`p_1` 的概率处于纯态 :math:`|\varphi_1\rangle = \alpha_1|0\rangle + \beta_1|1\rangle` ，以 :math:`p_2` 的概率处于纯态  :math:`|\varphi_2\rangle= \alpha_2|0\rangle + \beta_2|1\rangle` ，以此类推。

混合态不是纯态的线性叠加。假设系统处于 :math:`\{|0\rangle, |1\rangle\}，\{\frac{1}{2},\frac{1}{2}\}` 的混合态，
表示系统最终的状态，50%的概率处于 :math:`|0\rangle`, 50%的概率处于 :math:`|1\rangle`。
多次重复测量得到的结果与态 :math:`\frac{1}{\sqrt 2}|0\rangle + \frac{1}{\sqrt 2}|1\rangle` 相同，但两者的量子态却完全不同。

密度矩阵
>>>>>>>>>>>>>
对于混合态，态矢已难以完整的表示系统的量子态，一般使用密度矩阵来描述：

.. math::
    \begin{aligned}
    \rho = \sum_{i}^{n} p_i|\varphi_i\rangle\langle\varphi_i|
    \end{aligned}

对于纯态，可简化为

.. math::	
	\rho = |\varphi\rangle\langle\varphi|

回到前文所述的混合态，其密度矩阵为：

.. math:: 
    \rho = \frac{1}{2}|0\rangle\langle 0| + \frac{1}{2}|1\rangle\langle 1|
    = \frac{1}{2} 
	\begin{bmatrix}
		1&0\\
		0&1
	\end{bmatrix}

而相同测量结果的 :math:`|\psi\rangle = \frac{1}{\sqrt 2}|0\rangle + \frac{1}{\sqrt 2}|1\rangle` 纯态，其密度矩阵为：

.. math:: 
    \rho = |\psi\rangle\langle\psi| 
    = \frac{1}{2} 
	\begin{bmatrix}
		1&1\\
		1&1
	\end{bmatrix}

由密度矩阵可见，两者的量子态是完全不同的。

对于纯态，有 :math:`tr(\rho^2) = 1`, 混合态 :math:`tr(\rho^2) < 1`。:math:`tr(A)` 表示求矩阵 :math:`A` 的迹，即n维矩阵 :math:`A` 中对角线上元素之和。

对于一般的酉矩阵逻辑门，用密度矩阵表示其对系统的态演化：

.. math:: 
    \rho^{\prime} = U{\rho}U^{\dagger}

使用密度矩阵表示测量结果，测量得到结果m的概率为：

.. math:: 
    p(m) = tr(M_{m}^{\dagger}M_m\rho)

上式中 :math:`M_m` 叫做测量算子，通常也叫做投影算符。以我们的计算基 :math:`|0\rangle` 为例，其投影到 :math:`|0\rangle` 的投影算符为 :math:`|0\rangle\langle 0|` ,
因此，测量得到  :math:`|0\rangle` 的概率为：

.. math:: 
    p(|0\rangle) = tr(|0\rangle\langle 0||0\rangle\langle 0|\rho)

以之前混合态和纯态的例子计算其测量结果为：

.. math:: 
    \begin{aligned}
    混合态： p(|0\rangle) = tr(
        \frac{1}{2} 
       \begin{bmatrix}
		1&0\\
		0&0
	   \end{bmatrix}
       \begin{bmatrix}
		1&0\\
		0&0
	   \end{bmatrix}
       \begin{bmatrix}
		1&0\\
		0&1
	   \end{bmatrix}
    )
    =\frac{1}{2} \\
    纯态： p(|0\rangle) = tr(
        \frac{1}{2} 
       \begin{bmatrix}
		1&0\\
		0&0
	   \end{bmatrix}
       \begin{bmatrix}
		1&0\\
		0&0
	   \end{bmatrix}
       \begin{bmatrix}
		1&1\\
		1&1
	   \end{bmatrix}
    )
    =\frac{1}{2} \\
    \end{aligned}

噪声对系统的演化
>>>>>>>>>>>>>>>>>>>
量子计算机，作为一个孤立系统，不受外界干扰时，一直处于纯态。当外界噪音干扰与计算机比特耦合之后，计算机加上外界整个系统处于纯态。但对于计算机这个系统，则其处于混合态。

我们可以用一个简单的模型来等效演示

初始态两比特为 :math:`|\psi_{1}\psi_0\rangle` 其中，:math:`|\psi_0\rangle` 代表我们的量子计算机系统， :math:`|\psi_1\rangle` 表示外界。当外界对计算机无干扰时，:math:`|\psi_0\rangle` 是个孤立系统，当逻辑门施加在 :math:`|\psi_0\rangle` 上时，其始终为纯态。
如果模拟外界对量子计算机的干扰，将两个比特制备为纠缠态，即外界对计算机造成了噪声干扰。对于两个比特的整个系统来讲，仍然处于纯态。此时整个系统处于

.. math:: 
    |\psi_{1}\psi_0\rangle = \frac{1}{\sqrt{2}}|00\rangle+\frac{1}{{\sqrt{2}}}|11\rangle

但当只看0比特位时，即我们的量子计算机，其态矢不能从中分离出来，表示为纯态的线性叠加，:math:`|\psi_0\rangle\neq\frac{1}{\sqrt{2}}|0\rangle+\frac{1}{{\sqrt{2}}}|1\rangle`,
此时单独对于 :math:`|\psi_0\rangle` 来讲，其已经处于混合态（由约化密度矩阵可知）。测量得到50%概率为 :math:`|0\rangle`， 50%的概率为 :math:`|1\rangle`。



噪声对包含计算机和环境的整个系统的演化算子是酉的，但仅对于计算机量子态的来看，则可能是非酉的。
因此，对于噪声对计算机系统量子态的演化，通常使用算子和表示(operator-sum representation)：

.. math:: 
    \rho^{\prime} = \sum\limits_{i}{K_i}{\rho} {K_i}^{\dagger}

其中 :math:`K_i` 为表示噪声演化的Kraus算子，满足

.. math:: 
     \sum\limits_{i}K_{i}^{\dagger} K_{i} = 1


噪声模型介绍
--------------------------------------

QPanda2为我们提供了丰富的噪声模型，我们可以自定义噪声模型和量子逻辑门的对应关系。噪声模型主要分为两种：单门噪声模型和双门噪声模型。

单门噪声模型
>>>>>>>>>>>>>>

DAMPING_KRAUS_OPERATOR
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

DAMPING_KRAUS_OPERATOR是量子比特的弛豫过程噪声模型，它的kraus算符和表示方法如下所示：

:math:`K_1 = \begin{bmatrix} 1 & 0 \\ 0 & \sqrt{1 - p} \end{bmatrix},   K_2 = \begin{bmatrix} 0 & \sqrt{p} \\ 0 & 0 \end{bmatrix}`

需要一个噪声参数 :math:`p` ，为取值 :math:`[0, 1]` 之间的实数，意义为发生噪声影响的概率。

假设初始态处于 :math:`|\psi\rangle = \frac{1}{\sqrt 2}|0\rangle + \frac{1}{\sqrt 2}|1\rangle` 使用算子和表示来演化噪声的影响：

.. math:: 
    \rho^{\prime} = K_1\rho K_{1}^{\dagger} + K_2\rho K_{2}^{\dagger} = \frac{1}{2} \begin{bmatrix} 1+p &  \sqrt{1 - p}\\ \sqrt{1 - p} & 1 - p \end{bmatrix}

测量得到结果的概率分别为：

.. math:: 
    \begin{align}
    p(|0\rangle) = \frac{1}{2}(1+p) \\
    p(|1\rangle) = \frac{1}{2}(1-p) 
    \end{align}

由 :math:`tr(\rho^2) = \frac{1}{2}(2-p+p^2)` 可见，当 :math:`p=0` 或 :math:`1` 时，系统仍为纯态；当 :math:`p=(0, 1)` 时，系统处于混合态。
可见，当 :math:`p` 为 :math:`0` 时，即没有噪声影响，量子态保持不变；若 :math:`p` 为 :math:`1` 时，必定发生弛豫，演化为态 :math:`|0\rangle`。

后面的噪声演化过程不再演示，读者可以自行演算。


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

全振幅虚拟机在进行含噪声模拟时，只需要在初始化前设置一些量子逻辑门的噪声模型和对应的参数即可。

目前QPanda2中含噪声量子逻辑门支持的噪声模型有：

    .. code-block:: python

        class NoiseModel:
            BITFLIP_KRAUS_OPERATOR
            BIT_PHASE_FLIP_OPRATOR
            DAMPING_KRAUS_OPERATOR
            DECOHERENCE_KRAUS_OPERATOR
            DEPHASING_KRAUS_OPERATOR
            DEPOLARIZING_KRAUS_OPERATOR
            PAULI_KRAUS_MAP
            PHASE_DAMPING_OPRATOR

使用 :code:`Noise` 类接口设置噪声模型参数：

.. code-block:: python

    def add_noise_model(self, noise_model: NoiseModel, gate_type: GateType, prob: float) -> None:
    def add_noise_model(self, noise_model: NoiseModel, gate_types: List[GateType], prob: float) -> None:
    def add_noise_model(self, noise_model: NoiseModel, gate_type: GateType, prob: float, qubits: QVec) -> None:
    def add_noise_model(self, noise_model: NoiseModel, gate_types: List[GateType], prob: float, qubits: QVec) -> None:
    def add_noise_model(self, noise_model: NoiseModel, gate_type: GateType, prob: float, qubits: List[QVec]) -> None:

第一个参数为噪声模型类型，第二个参数为量子逻辑门类型，第三个参数为噪声模型所需的参数, 第四个参数是对单个比特设置噪声参数（包含单门和双门），若没有第四个参数则对所有的比特设置相应的噪声模型。

对于需要输入三个参数的噪声类型，接口如下：

.. code-block:: python

    def add_noise_model(self, noise_model: NoiseModel, gate_type: GateType, t1: float, t2: float, t_gate: float) -> None:
    def add_noise_model(self, noise_model: NoiseModel, gate_types: List[GateType], t1: float, t2: float, t_gate: float) -> None:
    def add_noise_model(self, noise_model: NoiseModel, gate_type: GateType, t1: float, t2: float, t_gate: float, qubits: QVec) -> None:
    def add_noise_model(self, noise_model: NoiseModel, gate_types: List[GateType], t1: float, t2: float, t_gate: float, qubits: QVec) -> None:
    def add_noise_model(self, noise_model: NoiseModel, gate_type: GateType, t1: float, t2: float, t_gate: float, qubits: List[QVec]) -> None:

接口参数意义与之前的接口类似

除此之外，噪声模型还支持设置测量噪声：

.. code-block:: python

    def add_measure_error(self, noise_model: NoiseModel, prob: float, qubits: QVec = ...) -> None:
    def add_measure_error(self, noise_model: NoiseModel, t1: float, t2: float, t_gate: float, qubits: QVec = ...) -> None:

用法类似于量子逻辑门的噪声模型，第一个参数为噪声模型类型，后面的参数和量子逻辑门的噪声参数。该噪声是指执行测量操作本身带入到系统的噪声。

重置噪声：

.. code-block:: python

    def add_reset_error(self, p0: float, p1: float, qubits: QVec) -> None:

p0 表示重置到 :math:`\ket{0}` 的概率，p1表示重置到 :math:`\ket{1}` 的概率，未被重置的概率为 1-p0-p1。
    

读出噪声：

.. code-block:: python

    def add_readout_error(self, prob_list: List[List[float]], qubits: QVec = ...) -> None:

:c:var:`probs_list` 为四个元素，两两一组，如 :code:`probs_list = {{f0, 1 - f0},{1 - f1, f1}};`， 
表示当测量终态为 :math:`\ket{0}` ，读出为0的概率为f0，读出为1的概率为1-f0；当测量终态为 :math:`\ket{1}` 时，读出为0的概率为1-f1，读出为1的概率为f1。

第二个参数为读出噪声作用的比特。

读出噪声不是量子噪声，而是经典仪器从低温量子态获取到结果，到室温过程中环境造成的干扰。

噪声模型还支持设置带有相位角旋转的量子逻辑门的旋转误差，其接口使用方式如下：

.. code-block:: python

   def set_rotation_error(self, error: float) -> None:


实例
----------------

.. code-block:: python
    
    from pyqpanda import *
    import numpy as np

    if __name__ == "__main__":
        qvm = CPUQVM()
        qvm.init_qvm()
        q = qvm.qAlloc_many(4)
        c = qvm.cAlloc_many(4)

        # 创建噪声模型，并添加设置噪声参数
        noise = Noise()
        noise.add_noise_model(NoiseModel.BITFLIP_KRAUS_OPERATOR, GateType.PAULI_X_GATE, 0.1)
        qv0 = [q[0], q[1]]
        noise.add_noise_model(NoiseModel.DEPHASING_KRAUS_OPERATOR, GateType.HADAMARD_GATE, 0.1, qv0)
        qves = [[q[0], q[1]], [q[1], q[2]]]
        noise.add_noise_model(NoiseModel.DAMPING_KRAUS_OPERATOR, GateType.CNOT_GATE, 0.1, qves)

        f0 = 0.9
        f1 = 0.85
        noise.add_readout_error([[f0, 1 - f0], [1 - f1, f1]])
        noise.set_rotation_error(0.05)

        prog = QProg()
        prog << X(q[0]) << H(q[0]) \
             << CNOT(q[0], q[1]) \
             << CNOT(q[1], q[2]) \
             << CNOT(q[2], q[3]) \
             << measure_all(q, c)

        # 运行量子程序时，加入噪声模型。默认为空噪声模型，即无噪声
        result = qvm.run_with_configuration(prog, c, 1000, noise)
        print(result)

运行结果：

    .. code-block:: python
        
        {'0000': 347, '0001': 55, '0010': 50, '0011': 43, '0100': 41, '0101': 18, '0110': 16, '0111': 34, '1000': 50, '1001': 18, '1010': 18, '1011': 37, '1100': 15, '1101': 49, '1110': 42, '1111': 167}

程序在无噪声的理想情况下，结果应该当为等概率的 0000 和 1111。结果中的其他测量值，为噪声带来的影响。
