.. _密度矩阵模拟器:

密度矩阵模拟器
=================
----

目前量子计算机的主要局限在于通用量子计算机所需的量子系统规模非常大，技术实现困难，因而人们主要利用中小规模量子体系，解决特定问题。

对于纯态和混合态量子比特系统，需要找到一种在低比特情况下，正确模拟噪声测量以及对哈密顿算符期望进行求解，而 ``密度矩阵模拟器`` 提供这一问题的解决方案。

密度矩阵相关学习可以参考 :ref:`密度矩阵介绍` 。

应用场景
>>>>>>>>>>>>>>>>
----

密度矩阵是表达量子态的另一种方式。而密度矩阵模拟器用于求解量子线路对应的密度矩阵，以及计算量子态概率分布、模拟含噪声量子线路和计算哈密顿量期望值等等。


使用介绍
>>>>>>>>>>>>>>>>
----

 ``pyqpanda`` 中可以通过 ``DensityMatrixSimulator`` 类实现用密度矩阵模拟器。和许多其他模拟器的使用方法一样，都具有相同的量子虚拟机接口，比如下述简单的使用示例代码:

    .. code-block:: python

        from numpy import pi
        from pyqpanda import *

        machine = DensityMatrixSimulator()
        machine.init_qvm()

        prog = QProg()
        q = machine.qAlloc_many(2)
        c = machine.cAlloc_many(2)

        prog.insert(hadamard_circuit(q))\
            .insert(Y(q[1]))\
            .insert(X(q[0]))\
            .insert(CNOT(q[0], q[1]))

        # get_density_matrix
        density_matrix = machine.get_density_matrix(prog)
        print(density_matrix)

完整示例代码
>>>>>>>>>>
----

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
       