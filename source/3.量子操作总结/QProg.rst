量子程序
==============
----

量子程序是一种描述量子计算任务的指令序列，类似于经典计算中的计算机程序。然而，与经典计算不同的是，量子程序在量子比特上执行操作，利用量子力学的奇特性质来进行信息处理。

在传统计算中，经典比特（0和1）是计算的基本单位，而在量子计算中，量子比特（或称为量子位）可以同时处于0和1的叠加态，还可以通过纠缠现象与其他量子比特相互关联。这些量子特性赋予了量子程序强大的计算能力，使其能够解决一些经典计算难题，如因子分解和优化问题。

量子程序的核心是量子门操作，它们是对量子比特进行操作的基本构建块。通过使用不同的量子门操作，可以在量子比特之间创建复杂的量子态和量子纠缠，实现量子计算中的各种算法和任务。量子程序还包括测量操作，将量子信息转化为经典信息以便进一步分析和处理。

编写和优化量子程序是量子计算研究和应用的关键一步。设计合理的量子门序列、选择适当的量子比特布局以及优化操作顺序等都会影响量子程序的执行效率和准确性。随着量子计算技术的不断发展，量子程序成为了探索量子算法、量子模拟、量子优化等领域的重要工具。

.. _api_introduction:

接口介绍
>>>>>>>>>>>>>>>>

在QPanda2中，QProg是量子编程的一个容器类，是一个量子程序的最高单位。

.. class:: QProg

    该类实现了量子程序的构建，使用链表数据结构存储量子电路。可用于构建量子电路，执行量子操作以及进行分析。

    .. method:: __init__()

        初始化一个空的量子程序。

    .. method:: __init__(prog: QProg)

        使用另一个量子程序构造新的量子程序节点。

        :param prog: 要复制的量子程序。
        :type prog: QProg
        :return: 一个新的量子程序节点。

    .. method:: __init__(qcircuit: QCircuit)

        使用一个量子线路构造新的量子程序节点。

        :param qcircuit: 要转换为量子程序的量子线路。
        :type qcircuit: QCircuit
        :return: 一个新的量子程序节点。

    .. method:: __init__(qif_prog: QIfProg)

        使用一个 QIfProg 节点构造新的量子程序节点。

        :param qif_prog: 要转换为量子程序的 QIfProg 节点。
        :type qif_prog: QIfProg
        :return: 一个新的量子程序节点。

    .. method:: __init__(qwhile_prog: QWhileProg)

        使用一个 QWhileProg 节点构造新的量子程序节点。

        :param qwhile_prog: 要转换为量子程序的 QWhileProg 节点。
        :type qwhile_prog: QWhileProg
        :return: 一个新的量子程序节点。

    .. method:: __init__(qgate: QGate)

        使用一个 QGate 节点构造新的量子程序节点。

        :param qgate: 要转换为量子程序的 QGate 节点。
        :type qgate: QGate
        :return: 一个新的量子程序节点。

    .. method:: __init__(qmeasure: QMeasure)

        使用一个 QMeasure 节点构造新的量子程序节点。

        :param qmeasure: 要转换为量子程序的 QMeasure 节点。
        :type qmeasure: QMeasure
        :return: 一个新的量子程序节点。

    .. method:: __init__(qreset: QReset)

        使用一个 QReset 节点构造新的量子程序节点。

        :param qreset: 要转换为量子程序的 QReset 节点。
        :type qreset: QReset
        :return: 一个新的量子程序节点。

    .. method:: __init__(cc: ClassicalCondition)

        使用一个 ClassicalCondition 节点构造新的量子程序节点。

        :param cc: 要转换为量子程序的 ClassicalCondition 节点。
        :type cc: ClassicalCondition
        :return: 一个新的量子程序节点。

    .. method:: __init__(node_iter: NodeIter)

        使用一个 NodeIter 节点构造新的量子程序节点。

        :param node_iter: 要转换为量子程序的 NodeIter 节点。
        :type node_iter: NodeIter
        :return: 一个新的量子程序节点。

    .. method:: get_max_qubit_addr()

        获取量子程序中最大的量子比特地址，下标从0开始

    .. method:: get_qgate_num()

        获取量子程序中的量子门数量。

    .. method:: get_used_cbits(cbit_vector: List[ClassicalCondition]) -> List[ClassicalCondition]

        获取量子程序中使用的经典比特列表。

        :param cbit_vector: 用于存储使用的经典比特的列表。
        :type cbit_vector: List[ClassicalCondition]
        :return: 使用的经典比特列表。
        :rtype: List[ClassicalCondition]

    .. method:: get_used_qubits(qubit_vector: QVec) -> QVec

        获取量子程序中使用的量子比特列表。

        :param qubit_vector: 用于存储使用的量子比特的列表。
        :type qubit_vector: QVec
        :return: 使用的量子比特列表。
        :rtype: QVec

    .. method:: insert(node: Union[QProg, QGate, QCircuit, QIfProg, QWhileProg, QMeasure, QReset, ClassicalCondition]) -> QProg

        在量子程序中插入一个节点。

        :param node: 要插入的节点。
        :type node: Union[QProg, QGate, QCircuit, QIfProg, QWhileProg, QMeasure, QReset, ClassicalCondition]
        :return: 修改后的量子程序。
        :rtype: QProg

    .. method:: is_empty()

        判断量子程序是否为空。

    .. method:: is_measure_last_pos()

        判断量子程序最后一个节点是否为测量操作。

    .. method:: last()

        获取量子程序的最后一个节点。

    .. method:: __lshift__(node: Union[QProg, QGate, QCircuit, QIfProg, QWhileProg, QMeasure, QReset, ClassicalCondition]) -> QProg

        通过左移操作符在量子程序中插入一个节点。

        :param node: 要插入的节点。
        :type node: Union[QProg, QGate, QCircuit, QIfProg, QWhileProg, QMeasure, QReset, ClassicalCondition]
        :return: 修改后的量子程序。
        :rtype: QProg

它也是QNode中的一种，初始化一个QProg对象也可以使用下面的方式

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

QProg还支持 ``cast_qprog_qcircuit`` 接口，可以将QProg转换成QCircuit类型：

    .. code-block:: python

        cir = cast_qprog_qcircuit(prog)  
        print(cir)


QProg还支持 ``cast_qprog_qgate`` 接口，可以将QProg转换成QGate类型：

    .. code-block:: python

        gate = cast_qprog_qgate(prog) 

QProg还支持 ``cast_qprog_qmeasure`` 接口，可以将QProg转换成QMeasure类型：

    .. code-block:: python

        qmeas = cast_qprog_qmeasure(prog)

实例
>>>>>>>>>>
----

    .. code-block:: python

        from pyqpanda import *

        if __name__ == "__main__":

            qvm = CPUQVM()
            qvm.init_qvm()
            qubits = qvm.qAlloc_many(4)
            cbits = qvm.cAlloc_many(4)
            prog = QProg()

            # 构建量子程序
            prog << H(qubits[0]) \
                 << X(qubits[1]) \
                 << iSWAP(qubits[0], qubits[1]) \
                 << CNOT(qubits[1], qubits[2]) \
                 << H(qubits[3]) \
                 << measure_all(qubits, cbits)

            # 量子程序运行1000次，并返回测量结果
            result = qvm.run_with_configuration(prog, cbits, 1000)
            
            # 打印量子态在量子程序多次运行结果中出现的次数
            print(result)



运行结果：

    .. code-block:: c

        {'0001': 232, '0111': 263, '1001': 243, '1111': 262}


QProg支持 ``get_all_used_qubits`` 接口，可以获取到QProg中所有已使用到的比特信息：

.. code-block:: python

        used_qv = get_all_used_qubits(prog)

