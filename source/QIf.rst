QIf
==========
----

QIf表示量子程序条件判断操作，输入参数为条件判断表达式，功能是执行条件判断。

.. _api_introduction:

接口介绍
>>>>>>>>>>>
----

在QPanda2中，QIfProg类用于表示执行量子程序条件判断操作，它也是QNode中的一种，初始化一个QIfProg对象有以下两种：

    .. code-block:: python

        qif = QIfProg(ClassicalCondition, QNode)
        qif = QIfProg(ClassicalCondition, QNode, QNode)


上述函数需要提供两种类型参数，即ClassicalCondition量子表达式与QNode节点，
当传入1个QNode参数时，QNode表示正确分支节点，当传入2个QNode参数时，第一个表示正确分支节点，第二个表示错误分支节点。
可以传入的QNode类型有： QProg、QCircuit、QGate、QWhileProg、QIfProg、QMeasure。

实例
>>>>>>>>>
----

    .. code-block:: python

        from pyqpanda import *

        if __name__ == "__main__":

            qvm = CPUQVM()
            qvm.init_qvm()
            qubits = qvm.qAlloc_many(3)
            cbits = qvm.cAlloc_many(3)
            cbits[0].set_val(0)
            cbits[1].set_val(3)

            prog = QProg()
            branch_true = QProg()
            branch_false = QProg()

            # 构建QIf正确分支以及错误分支
            branch_true << H(qubits[0])<< H(qubits[1]) << H(qubits[2])
            branch_false << H(qubits[0]) << CNOT(qubits[0], qubits[1]) << CNOT(qubits[1], qubits[2])

            # 构建QIf
            qif = QIfProg(cbits[0] > cbits[1], branch_true, branch_false)
            
            # QIf插入到量子程序中
            prog << qif

            # 概率测量，并返回目标量子比特的概率测量结果，下标为十进制
            result = qvm.prob_run_tuple_list(prog, qubits, -1)

            # 打印概率测量结果
            print(result)


运行结果：

    .. code-block:: python

        [(0, 0.4999999999999999), (7, 0.4999999999999999), (1, 0.0), (2, 0.0), (3, 0.0), (4, 0.0), (5, 0.0), (6, 0.0)]

