量子程序
==============
----

量子程序设计用于量子程序的编写与构造，一般地， 可以理解为一个操作序列。由于量子算法中也会包含经典计算，因而业界设想，最近将来出现的量子计算机是混合结构的，它包含两大部分一部分是经典计算机，负责执行经典计算与控制；另一部分是量子设备，负责执行量子计算。QPanda-2将量子程序的编程过程视作经典程序运行的一部分，在整个外围的宿主机程序中，一定包含创建量子程序的部分。

.. _api_introduction:

接口介绍
>>>>>>>>>>>>>>>>
----

在QPanda2中，QProg是量子编程的一个容器类，是一个量子程序的最高单位。它也是QNode中的一种，初始化一个QProg对象有以下两种

    .. code-block:: python

        prog = QProg()

或

    .. code-block:: python

        prog = create_empty_qprog()

还可以由已有的QNode节点来构建量子程序，如：

    .. code-block:: python

        qubit = qAlloc()
        gate = H(qubit)
        prog = QProg(gate)

可以用类似的方式构建量子程序的有QCircuit、QGate、QWhileProg、QIfProg、ClassicalCondition、QMeasure。

你可以通过如下方式向QProg尾部填充节点, 在这里pyqpanda重载了 ``<<`` 运算符作为插入量子线路的方法

    .. code-block:: python

        prog << node

QNode的类型有QGate，QPorg，QIf，Measure等等，QProg支持插入所有类型的QNode

实例
>>>>>>>>>>
----

    .. code-block:: python

        from pyqpanda import *

        if __name__ == "__main__":

            init(QMachineType.CPU)
            qubits = qAlloc_many(4)
            cbits = cAlloc_many(4)
            prog = QProg()

            # 构建量子程序
            prog << H(qubits[0]) \
                 << X(qubits[1]) \
                 << iSWAP(qubits[0], qubits[1]) \
                 << CNOT(qubits[1], qubits[2]) \
                 << H(qubits[3]) \
                 << measure_all(qubits, cbits)

            # 量子程序运行1000次，并返回测量结果
            result = run_with_configuration(prog, cbits, 1000)
            
            # 打印量子态在量子程序多次运行结果中出现的次数
            print(result)
            finalize()



运行结果：

    .. code-block:: c

        {'1000': 272, '1001': 261, '1110': 220, '1111': 247}
