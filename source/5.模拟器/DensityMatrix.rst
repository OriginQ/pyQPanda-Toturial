.. _密度矩阵模拟器:

密度矩阵模拟器
=================

目前量子计算机的主要局限在于通用量子计算机所需的量子系统规模非常大，技术实现困难，因而人们主要利用中小规模量子体系，解决特定问题。

对于纯态和混合态量子比特系统，需要找到一种在低比特情况下，正确模拟噪声测量以及对哈密顿算符期望进行求解，而 ``密度矩阵模拟器`` 提供这一问题的解决方案。


.. _密度矩阵介绍:

密度矩阵基础
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

密度矩阵是表达量子态的另一种方式。而密度矩阵模拟器用于求解量子线路对应的密度矩阵，以及计算量子态概率分布、模拟含噪声量子线路和计算哈密顿量期望值等等。

使用介绍
>>>>>>>>>>>>>>>>
----

``pyqpanda`` 中可以通过 ``DensityMatrixSimulator`` 类实现用密度矩阵模拟器。和许多其他模拟器的使用方法一样，都具有相同的量子虚拟机接口:

.. class:: DensityMatrixSimulator(QuantumMachine)

    该类是用于模拟密度矩阵的量子虚拟机。
    该类提供了一系列方法用于模拟N比特的密度矩阵和约化密度矩阵的计算，以及直接获取不同噪声环境下量子线路模拟后的概率分布

    .. method:: get_density_matrix(prog: QProg) -> numpy.ndarray[numpy.complex128[m,n]]

        执行量子程序并获取完整的密度矩阵。

        :param prog: 量子程序。
        :type prog: QProg
        :return: 完整的密度矩阵。
        :rtype: numpy.ndarray[numpy.complex128[m,n]]
        :raises run_fail: 获取密度矩阵时发生错误。

    .. method:: get_expectation(prog: QProg, hamiltonian: List[Tuple[Dict[int,str],float]], qubits: QVec) -> float
                get_expectation(prog: QProg, hamiltonian: List[Tuple[Dict[int,str],float]], qubits: List[int]) -> float

        执行量子程序并计算给定哈密顿量的期望值。

        :param prog: 量子程序。
        :type prog: QProg
        :param hamiltonian: 哈密顿量。
        :type hamiltonian: List[Tuple[Dict[int,str],float]]
        :param qubits: 选定的量子比特或量子比特列表。
        :type qubits: QVec or List[int]
        :return: 选定量子比特上的哈密顿量期望值。
        :rtype: float
        :raises run_fail: 计算期望值时发生错误。

    .. method:: get_probabilities(prog: QProg) -> List[float]
                get_probabilities(prog: QProg, qubits: QVec) -> List[float]
                get_probabilities(prog: QProg, qubits: List[int]) -> List[float]
                get_probabilities(prog: QProg, indices: List[str]) -> List[float]

        执行量子程序并获取所有可能性的概率。

        :param prog: 量子程序。
        :type prog: QProg
        :param qubits: 选定的量子比特或量子比特列表。
        :type qubits: QVec or List[int]
        :param indices: 选定的二进制索引列表。
        :type indices: List[str]
        :return: 量子程序的概率结果。
        :rtype: List[float]
        :raises run_fail: 获取概率时发生错误。

    .. method:: get_probability(prog: QProg, index: int) -> float
                get_probability(prog: QProg, index: str) -> float

        执行量子程序并获取给定索引的概率。

        :param prog: 量子程序。
        :type prog: QProg
        :param index: 测量索引（在 [0,2^N - 1] 范围内）。
        :type index: int or str
        :return: 量子程序的概率结果。
        :rtype: float
        :raises run_fail: 获取概率时发生错误。

    .. method:: get_reduced_density_matrix(prog: QProg, qubits: QVec) -> numpy.ndarray[numpy.complex128[m,n]]
                get_reduced_density_matrix(prog: QProg, qubits: List[int]) -> numpy.ndarray[numpy.complex128[m,n]]

        执行量子程序并获取选定量子比特的约化密度矩阵。

        :param prog: 量子程序。
        :type prog: QProg
        :param qubits: 选定的量子比特或量子比特列表。
        :type qubits: QVec or List[int]
        :return: 约化密度矩阵。
        :rtype: numpy.ndarray[numpy.complex128[m,n]]
        :raises run_fail: 获取约化密度矩阵时发生错误。

    .. method:: init_qvm(is_double_precision: bool = True) -> None

        初始化量子虚拟机。

        :param is_double_precision: 是否使用双精度（默认为 True）。
        :type is_double_precision: bool, optional

    .. method:: set_noise_model(arg0: numpy.ndarray[numpy.complex128[m,n]]) -> None
                set_noise_model(arg0: numpy.ndarray[numpy.complex128[m,n]], arg1: List[GateType]) -> None
                set_noise_model(arg0: List[numpy.ndarray[numpy.complex128[m,n]]]) -> None
                set_noise_model(arg0: List[numpy.ndarray[numpy.complex128[m,n]]], arg1: List[GateType]) -> None
                set_noise_model(arg0: NoiseModel, arg1: GateType, arg2: float) -> None
                set_noise_model(arg0: NoiseModel, arg1: List[GateType], arg2: float) -> None
                set_noise_model(arg0: NoiseModel, arg1: GateType, arg2: float, arg3: QVec) -> None
                set_noise_model(arg0: NoiseModel, arg1: List[GateType], arg2: float, arg3: QVec) -> None
                set_noise_model(arg0: NoiseModel, arg1: GateType, arg2: float, arg3: List[QVec]) -> None
                set_noise_model(arg0: NoiseModel, arg1: GateType, arg2: float, arg3: float, arg4: float) -> None
                set_noise_model(arg0: NoiseModel, arg1: List[GateType], arg2: float, arg3: float, arg4: float) -> None
                set_noise_model(arg0: NoiseModel, arg1: GateType, arg2: float, arg3: float, arg4: float, arg5: QVec) -> None
                set_noise_model(arg0: NoiseModel, arg1: List[GateType], arg2: float, arg3: float, arg4: float, arg5: QVec) -> None
                set_noise_model(arg0: NoiseModel, arg1: GateType, arg2: float, arg3: float, arg4: float, arg5: List[QVec]) -> None

        该方法用于设置噪声模型，以在模拟中引入量子门的错误。

        :param arg0: 噪声模型参数，可能的类型包括 numpy 数组、噪声模型、量子门类型（GateType）、浮点数等。
        :type arg0: numpy.ndarray[numpy.complex128[m,n]] or List[numpy.ndarray[numpy.complex128[m,n]]] or NoiseModel or GateType or float
        :param arg1: 噪声模型的参数，具体类型取决于参数类型。
        :type arg1: Varies (See detailed descriptions)
        :param arg2: 噪声强度，表示引入的错误概率。
        :type arg2: float
        :param arg3: 选定的量子比特列表（或量子比特），用于针对特定比特引入噪声（部分参数可能会用到）。
        :type arg3: QVec or List[QVec] or QVec
        :param arg4: 更多参数，具体类型和用途取决于参数类型。
        :type arg4: Varies (See detailed descriptions)
        :param arg5: 更多参数，具体类型和用途取决于参数类型。
        :type arg5: Varies (See detailed descriptions)
        :return: 无返回值。
        :rtype: None

完整示例代码
>>>>>>>>>>

.. _密度矩阵模拟器示例程序:
以下示例展示了密度矩阵模拟器计算部分接口的使用方式

    .. code-block:: python

        from numpy import pi
        from pyqpanda import *

        machine = DensityMatrixSimulator()
        machine.init_qvm()

        q = machine.qAlloc_many(2)
        c = machine.cAlloc_many(2)

        prog = QProg()
        prog.insert(H(q[0]))\
            .insert(Y(q[1]))\
            .insert(RY(q[0], pi / 3))\
            .insert(RX(q[1], pi / 6))\
            .insert(RX(q[1], pi / 9))\
            .insert(CZ(q[0], q[1]))

        # 获取对应量子程序的密度矩阵
        print(machine.get_density_matrix(prog))

        # 获取对应量子程序的在指定量子比特下的约化密度矩阵
        print(machine.get_reduced_density_matrix(prog, [0]))

        # 获取对应量子程序指定量子态的概率
        print("quantum state 00 probability : ", machine.get_probability(prog, "00"))

        # 获取对应量子程序所有量子态的概率分布
        print(machine.get_probabilities(prog))

        # 获取对应量子程序指定哈密顿量下演化的期望值
        operator = 0.23 * x(1) + 0.2 * y(1) + 1.6 * z(0)
        expval = machine.get_expectation(prog,operator.to_hamiltonian(False),[0, 1])
        print(expval)

        # 设置噪声模型和参数
        machine.set_noise_model(NoiseModel.BITFLIP_KRAUS_OPERATOR, GateType.HADAMARD_GATE, 0.3)
        machine.set_noise_model(NoiseModel.BITFLIP_KRAUS_OPERATOR, GateType.CZ_GATE, 0.3)

        # 获取加入噪声后，密度矩阵信息和概率分布
        print(machine.get_density_matrix(prog))
        print(machine.get_probabilities(prog))

        machine.finalize()

    
    输出结果如下：

    .. code-block:: python

        # 对应量子程序的密度矩阵
        [[ 0.01196435+0.j  0.04465155+0.j  0.-0.02565762j  1.+0.09575556j]
        [ 0.04465155+0.j   0.16664185+0.j  0.-0.09575556j  1.+0.35736463j]
        [ 0.+0.02565762j   0.+0.09575556j  0.05502295+0.j -0.20534845+0.j]
        [-0.-0.09575556j  -0.-0.3573646j  -0.20534845+0.j  0.76637085-0.j]]

        # 对应量子程序的在指定量子比特下的约化密度矩阵
        [[ 0.0669873+0.j -0.1606969+0.j]
        [-0.1606969+0.j  0.9330127+0.j]]

        # 对应量子程序指定量子态的概率
        quantum state 00 probability :  0.01196434643886035

        # 对应量子程序所有量子态的概率分布
        [0.01196434643886035, 0.1666418487178699, 0.05502295166892035, 0.7663708531743493]

        # 对应量子程序指定哈密顿量下演化的期望值
        -1.5183234356888893 

        # 加入噪声后，密度矩阵信息
        [[ 0.12138551+0.j  -0.03034845+0.j  0.+0.03569962j 1.+0.03830222j]
        [-0.03034845+0.j  0.25005696+0.j  0.-0.03830222j 1.+0.09698317j]
        [ 0.-0.03569962j  0.+0.03830222j  0.2054094 +0.j -0.13034845+0.j]
        [ 0.-0.03830222j  0.-0.09698317j -0.13034845+0.j 0.42314812+0.j]]

        # 加入噪声后，概率分布
        [0.12138551462195893, 0.25005696344073314, 0.20540940462115326, 0.4231481173161546]
       
除此之外，密度矩阵的噪声可以叠加，参考下面的一个简单的例子，对于如下的简单线路

    .. code-block:: python

        from numpy import pi
        from pyqpanda import *

        machine = DensityMatrixSimulator()
        machine.init_qvm()

        prog = QProg()
        q = machine.qAlloc_many(2)
        c = machine.cAlloc_many(2)

        prog.insert(X(q[0]))\
            .insert(CNOT(q[0], q[1]))

        density_matrix1 = machine.get_density_matrix(prog)

        print(density_matrix1)


当我们同时对所有X门设置触发两次比特翻转噪声时，密度矩阵的演化如下：

    .. code-block:: python

        machine.set_noise_model(NoiseModel.BITFLIP_KRAUS_OPERATOR, GateType.PAULI_X_GATE, 0.3)
        print(machine.get_density_matrix(prog))

        machine.set_noise_model(NoiseModel.BITFLIP_KRAUS_OPERATOR, GateType.PAULI_X_GATE, 0.3)
        print(machine.get_density_matrix(prog))

运行结果如下：

    .. code-block:: python

        # 第一次施加的噪声
        [[0.3+0.j 0. +0.j 0. +0.j 0. +0.j]
        [0. +0.j 0. +0.j 0. +0.j 0. +0.j]
        [0. +0.j 0. +0.j 0. +0.j 0. +0.j]
        [0. +0.j 0. +0.j 0. +0.j 0.7+0.j]]

        # 噪声再次叠加的结果
        [[0.42+0.j 0. +0.j 0. +0.j 0. +0.j]
        [0. +0.j 0. +0.j 0. +0.j 0. +0.j]
        [0. +0.j 0. +0.j 0. +0.j 0. +0.j]
        [0. +0.j 0. +0.j 0. +0.j 0.58+0.j]]

