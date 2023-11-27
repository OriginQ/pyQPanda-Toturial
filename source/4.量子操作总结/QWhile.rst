QWhile
==============
----

无论是经典计算还是量子计算领域中，循环结构在许多算法和应用中扮演着重要角色。

量子QWhile循环节点是一种在量子程序中实现循环结构的机制，使得我们能够基于经典条件来重复执行一系列量子操作。这一概念类似于传统编程语言中的while循环，但在量子计算中涉及了量子比特和量子门操作。

实现量子While循环的常见方法是通过一个经典控制条件来判断循环是否继续，当然也可以是量子经典寄存器，一个典型的使用案例是利用量子QWhile循环节点来实现迭代优化算法，在这种情况下，经典条件可以是一组优化参数的变化是否达到收敛，而循环体中的量子操作可以是执行某种量子优化步骤。通过不断重复这个循环，我们可以逐步优化量子态或量子门操作，以实现更精确的结果。

.. _api_introduction:

接口介绍
>>>>>>>>>>>>>

在QPanda2中，QWhileProg类用于表示执行量子程序while循环操作，它也是QNode中的一种，QWhileProg的定义如下：

.. class:: QWhileProg

    量子 While 循环节点用于在量子程序中实现循环结构，允许基于经典条件重复执行量子操作。

    .. automethod:: __init__

    .. automethod:: get_classical_condition

    .. automethod:: get_true_branch

    .. method:: __init__(self, arg0: NodeIter) -> None

        创建一个 Quantum While 循环节点。

        :param arg0: 循环中的量子操作的迭代器。
        :type arg0: NodeIter
        :return: 无返回值
        :rtype: None

        该构造函数创建一个 Quantum While 循环节点，其中循环体是由迭代器中的量子操作构成。在每次循环迭代中，将执行迭代器中的量子操作。

    .. method:: __init__(self, arg0: ClassicalCondition, arg1: QProg) -> None

        创建一个 Quantum While 循环节点。

        :param arg0: 控制循环执行的经典条件。
        :type arg0: ClassicalCondition
        :param arg1: 循环体中的量子操作。
        :type arg1: QProg
        :return: 无返回值
        :rtype: None

        该构造函数创建一个 Quantum While 循环节点，其中循环体是由参数中的量子操作构成。循环将根据经典条件判断是否继续执行循环体中的操作。

    .. method:: get_classical_condition(self) -> ClassicalCondition

        获取循环的经典条件。

        :return: 循环的经典条件。
        :rtype: ClassicalCondition

        该方法返回用于控制循环执行的经典条件，该条件将在每次循环迭代前进行判断。

    .. method:: get_true_branch(self) -> QProg

        获取循环体中的量子操作。

        :return: 循环体中的量子操作。
        :rtype: QProg

        该方法返回在循环体中定义的量子操作，这些操作将在每次循环迭代中执行。

可以传入的QNode类型有： QProg、QCircuit、QGate、QWhileProg、QIfProg、QMeasure。

关于经典寄存器可以参考 :ref:`ClassicalCondition介绍` 。

实例
>>>>>>>>>>

    .. code-block:: python

        from pyqpanda import *

        if __name__ == "__main__":

            qvm = CPUQVM()
            qvm.init_qvm()
            qubits = qvm.qAlloc_many(3)
            cbits = qvm.cAlloc_many(3)
            cbits[0].set_val(0)
            cbits[1].set_val(1)

            prog = QProg()
            prog_while = QProg()

            # 构建QWhile的循环分支
            prog_while << H(qubits[0]) << H(qubits[1])<< H(qubits[2])\
                    << assign(cbits[0], cbits[0] + 1) << Measure(qubits[1], cbits[1])
            
            # 构建QWhile
            qwhile = QWhileProg(cbits[1], prog_while)
            
            # QWhile插入到量子程序中
            prog << qwhile

            # 运行，并打印测量结果
            result = qvm.directly_run(prog)
            print(result)
            print(cbits[0].get_val())


运行结果：

    .. code-block:: python

        {'c1': False}
        0