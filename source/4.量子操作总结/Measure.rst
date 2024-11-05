.. _Measure:

量子测量
================

量子测量是量子力学中的基本概念之一，用于引入外界的干扰获取量子系统的信息。在量子计算中，量子测量是评估量子比特状态的一种方式，它对量子信息的提取和观测起着至关重要的作用。

在量子计算中，测量通常被建模为对量子比特的一种操作，该操作将一个或多个量子比特的状态映射到经典的位（0或1）上。测量的结果是随机的，遵循一定的概率分布，这与量子力学的本质相关。

测量操作可以通过一系列测量门来实现，这些门用于将量子比特状态映射到经典位。蒙特卡洛方法在量子测量中的应用是指使用随机数模拟量子测量的随机性。在蒙特卡洛方法中，我们可以随机生成一组数值，这些数值代表测量结果的概率分布。通过模拟大量的测量，我们可以得到相应的统计数据，从而逼近真实的量子测量结果。

需要注意的是，量子测量会破坏量子系统的纯态，使其坍缩到一个确定的经典状态上。这个过程被称为量子态的“坍缩”或“投影”，而坍缩后的状态是测量结果所对应的状态。

在量子线路中用如下图标表示：

.. image:: images/QGate_measure.png
    :width: 65

.. _api_introduction:

接口介绍
----------------

本章主要介绍获得量子测量对象、根据配置运行含有量子测量的量子程序、快速测量。

在量子程序中我们需要对某个量子比特做测量操作，并把测量结果存储到经典寄存器上，可以通过下面的方式获得一个测量对象：

.. function:: Measure(qubit: Union[Qubit, int], cbit: Union[ClassicalCondition, CBit]) -> QMeasure

    此函数用于创建一个量子测量节点，用于测量给定的量子比特，并将测量结果存储在指定的经典比特中。

    :param qubit: 要测量的量子比特。可以是量子比特对象或量子比特的索引。
    :type qubit: Union[Qubit, int]
    :param cbit: 存储量子测量结果的经典比特。可以是经典比特对象或经典比特的索引。
    :type cbit: Union[ClassicalCondition, CBit]
    :return: 一个量子测量节点，表示测量操作。
    :rtype: QMeasure

如果想测量所有的量子比特并将其存储到对应的经典寄存器上，可以使用 **measure_all** ：

.. function:: measure_all(qubit_list: Union[QVec, List[int]], cbit_list: List[ClassicalCondition]) -> QProg

    创建一组量子测量节点
    =============================

    此函数用于创建一组量子测量节点，用于同时测量给定的多个量子比特，并将测量结果分别存储在对应的经典比特中。

    :param qubit_list: 要测量的量子比特列表。可以是量子比特对象列表或量子比特的索引列表。
    :type qubit_list: Union[QVec, List[int]]
    :param cbit_list: 存储量子测量结果的经典比特列表。
    :type cbit_list: List[ClassicalCondition]
    :return: 一个量子程序，包含一组量子测量节点，表示同时对多个量子比特进行测量。
    :rtype: QProg

.. note:: ``measure_all`` 的返回值类型是 ``QProg``。

在得到含有量子测量的程序后，我们可以调用 ``directly_run`` 或 ``run_with_configuration`` 来得到量子程序的测量结果。

1. **直接运行量子程序并返回运行的结果** ：directly_run

.. function:: directly_run(self, qprog: QProg, noise_model: Noise = NoiseModel()) -> Dict[str, bool]

    该方法用于直接运行量子程序，无需预先初始化。在使用此方法之前，请确保已进行初始化（init）操作。

    :param qprog: 要运行的量子程序。
    :type qprog: QProg
    :param noise_model: 噪声模型，默认为无噪声模型。噪声模型目前仅在 CPUQVM 上生效。
    :type noise_model: Noise, optional
    :return: 量子程序执行结果的字典，包含两个键值对。第一个键为最终量子比特寄存器状态，第二个键为其测量概率。
    :rtype: Dict[str, bool]

    示例用法::

        from pyqpanda import *
        qvm = CPUQVM()
        qvm.init_qvm()
        qubits = qvm.qAlloc_many(4)
        cbits = qvm.cAlloc_many(4)

        prog = QProg()
        prog << H(qubits[0])\
             << CNOT(qubits[0], qubits[1])\
             << CNOT(qubits[1], qubits[2])\
             << CNOT(qubits[2], qubits[3])\
             << Measure(qubits[0], cbits[0])

        result = qvm.directly_run(prog)

2. **统计量子程序多次运行的测量结果** : run_with_configuration

.. function:: run_with_configuration(self, qprog: QProg, cbit_list: Union[List[ClassicalCondition], List[int]], data: dict, noise_model: Noise = NoiseModel()) -> Dict[str, int]

    此函数用于以配置信息运行量子程序，并返回在不同运行次数下的执行结果。

    :param qprog: 要运行的量子程序。
    :type qprog: QProg
    :param cbit_list: 存储测量结果的经典比特列表或经典比特索引列表。
    :type cbit_list: Union[List[ClassicalCondition], List[int]]
    :param data: 配置信息，用于不同运行次数的设置。
    :type data: dict
    :param noise_model: 噪声模型，用于模拟噪声影响。默认为无噪声模型。
    :type noise_model: Noise, optional
    :return: 在不同运行次数下的执行结果。结果以字典形式返回，键为量子态的二进制字符串表示，值为对应的命中次数。
    :rtype: Dict[str, int]

.. function:: run_with_configuration(self, qprog: QProg, shot: int, noise_model: Noise = NoiseModel()) -> Dict[str, int]

    此函数用于以配置信息运行量子程序，并返回在指定运行次数下的执行结果。

    :param qprog: 要运行的量子程序。
    :type qprog: QProg
    :param shot: 运行次数。
    :type shot: int
    :param noise_model: 噪声模型，用于模拟噪声影响。默认为无噪声模型。
    :type noise_model: Noise, optional
    :return: 在指定运行次数下的执行结果。结果以字典形式返回，键为量子态的二进制字符串表示，值为对应的命中次数。
    :rtype: Dict[str, int]

    示例用法::

        from pyqpanda import *
        
        machine = CPUQVM()
        machine.init_qvm()

        qubits = machine.qAlloc_many(3)
        cbits = machine.cAlloc_many(3)

        prog = QProg()
        prog << H(qubits[0])\
             << H(qubits[0])\
             << H(qubits[1])\
             << H(qubits[2])\
             << measure_all(qubits, cbits)
        result = run_with_configuration(prog, 1000)

实例
----------

    .. code-block:: python

        from pyqpanda import *

        if __name__ == "__main__":
            qvm = CPUQVM()
            qvm.init_qvm()
            qubits = qvm.qAlloc_many(4)
            cbits = qvm.cAlloc_many(4)

            # 构建量子程序
            prog = QProg()
            prog << H(qubits[0])\
                 << H(qubits[1])\
                 << H(qubits[2])\
                 << H(qubits[3])\
                 << measure_all(qubits, cbits)

            # 量子程序运行1000次，并返回测量结果
            result = qvm.run_with_configuration(prog, cbits, 1000)

            # 打印测量结果
            print(result)


运行结果：

    .. code-block:: python

        {'0000': 59, '0001': 69, '0010': 52, '0011': 62, 
        '0100': 63, '0101': 67, '0110': 79, '0111': 47, 
        '1000': 73, '1001': 59, '1010': 72, '1011': 60, 
        '1100': 61, '1101': 71, '1110': 50, '1111': 56}


.. _`get_expectation`:

3. **获取哈密顿期望** : get_expectation

    哈密顿期望是指系统处于某个量子态时，哈密顿算符在该量子态下的平均值。它描述了系统在该量子态下的平均能量。哈密顿期望的数学表达式为：
        ⟨H⟩ψ=⟨ψ|H|ψ⟩
    其中，⟨ψ| 是波函数的共轭，H 是哈密顿算符，|ψ⟩ 是波函数。这个期望值可以通过对哈密顿算符和波函数进行内积运算来求得。

.. function:: get_expectation(self: pyqpanda.pyQPanda.QuantumMachine, qprog: pyqpanda.pyQPanda.QProg, hamiltonian: List[Tuple[Dict[int, str], float]], qubit_list: pyqpanda.pyQPanda.QVec) -> float

    此函数用于在虚拟机中获取哈密顿期望

    :param self: QuantumMachine，get_expectation是其成员函数
    :type self: pyqpanda.pyQPanda.QuantumMachine
    :param qprog: 要运行的量子程序。
    :type qprog: QProg
    :param hamiltonian: 选择的哈密顿。
    :type hamitonian: List[Tuple[Dict[int, str], float]]
    :param qubit_list: 要测量的qubit的列表。
    :type qubit_list: pyqpanda.pyQPanda.QVec
    :return: 哈密顿期望的值
    :rtype: float

    示例

     .. code-block:: python

        from pyqpanda import *

        # 构建泡利算符
        # 参考： 8.Operators/index.html
        p = PauliOperator({"Z0":2})
        # 获得哈密顿量
        Hmt = p.to_hamiltonian(False)
        # 申请量子计算资源
        qvm= init_quantum_machine(QMachineType.CPU)
        # 申请量子比特，用于执行线路
        qvec = qvm.qAlloc_many(1)
        prog = QProg()
        prog << H(qvec[0])
        # 获取哈密顿期望
        expec =qvm.get_expectation(prog,Hmt,QVec(qvec))
        # 打印哈密顿期望
        print(expec)

    执行结果

    .. code-block:: bash

        0.0

.. function:: get_expectation(self: pyqpanda.pyQPanda.QuantumMachine, qprog: pyqpanda.pyQPanda.QProg, hamiltonian: List[Tuple[Dict[int, str], float]], qubit_list: pyqpanda.pyQPanda.QVec, shots: int) -> float

    此函数用于在虚拟机中获取哈密顿期望

    :param self: QuantumMachine，get_expectation是其成员函数
    :type self: pyqpanda.pyQPanda.QuantumMachine
    :param qprog: 要运行的量子程序。
    :type qprog: QProg
    :param hamiltonian: 选择的哈密顿。
    :type hamitonian: List[Tuple[Dict[int, str], float]]
    :param qubit_list: 要测量的qubit的列表。
    :type qubit_list: pyqpanda.pyQPanda.QVec
    :param shots: measure shots 
    :type shots: int
    :return: 哈密顿期望的值
    :rtype: float

     示例

     .. code-block:: python

        from pyqpanda import *

        # 构建泡利算符
        # 参考： 8.Operators/index.html
        p = PauliOperator({"Z0":2})
        # 获得哈密顿量
        Hmt = p.to_hamiltonian(False)
        # 申请量子计算资源
        qvm= init_quantum_machine(QMachineType.CPU)
        # 申请量子比特，用于执行线路
        qvec = qvm.qAlloc_many(1)
        prog = QProg()
        prog << H(qvec[0])
        # 获取哈密顿期望
        expec =qvm.get_expectation(prog,Hmt,QVec(qvec),100)
        # 打印哈密顿期望
        print(expec)

    执行结果

    .. code-block:: bash

        0.0

.. function:: get_expectation(self, prog: QProg, hamiltonian: List[Tuple[Dict[int,str],float]], qvec: QVec, task_name: str = 'QPanda Experiment')

    此函数用于在云平台中获取哈密顿期望

    :param self: QCloud，get_expectation是其成员函数
    :type self: QCloud
    :param qprog: 要运行的量子程序。
    :type qprog: QProg
    :param hamiltonian: 选择的哈密顿。
    :type hamitonian: List[Tuple[Dict[int, str], float]]
    :param qubit_list: 要测量的qubit的列表。
    :type qubit_list: pyqpanda.pyQPanda.QVec
    :param task_name: 提交至云平台的任务的名称
    :type task_name: str

    示例

     .. code-block:: python

        from pyqpanda import *

        from pyqpanda import *
        import numpy as np

        # 通过QCloud()创建量子云虚拟机
        QCM = QCloud()

        # 通过传入当前用户的token来初始化
        QCM.init_qvm("用户自己的token",True)

        # 构建泡利算符
        # 参考： 8.Operators/index.html

        # 2倍的"泡利Z0"张乘"泡利Z1" + 3倍的"泡利X1"张乘"泡利Y2"
        p = PauliOperator({"Z0":2})
        # 获得哈密顿量
        Hmt = p.to_hamiltonian(False)
        qvec = QCM.qAlloc_many(1)
        prog = QProg()
        prog << H(qvec[0])

        expec =QCM.get_expectation(prog,Hmt,[0])
        # 打印哈密顿期望
        print(expec)

    执行结果

    .. code-block:: bash

        0.0


    

