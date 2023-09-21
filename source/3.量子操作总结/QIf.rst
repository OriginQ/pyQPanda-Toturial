QIf
==========

QIf表示量子程序条件判断操作，输入参数为条件判断表达式，功能是执行条件判断。

在量子计算中，除了对量子比特进行操作外，还可以根据经典寄存器的状态来执行条件操作。这意味着我们可以根据经典寄存器中存储的经典信息来决定是否执行特定的量子操作。

这种条件操作使得量子计算能够根据经典信息灵活地调整量子门的应用，从而实现更加复杂和多样化的计算过程。

例如，假设我们有一个经典寄存器中存储了一个位的值，可以是0或1。我们可以根据这个位的值来决定是否对量子比特应用某个特定的量子门操作。如果经典寄存器中的位是0，我们执行一系列操作；如果位是1，我们执行另一系列操作。通过这种方式，我们可以在量子计算中引入经典信息，从而实现更加智能和可控的计算过程。

.. _ClassicalCondition介绍:

经典寄存器
>>>>>>>>>>>>>>

在量子计算中，经典寄存器是与量子比特（qubit）相对应的一个概念。

由于量子计算和经典计算是不同的计算模型，它们之间需要有适当的接口来实现数据的传递和交互。经典寄存器就是这种接口之一，用于在量子计算和经典计算之间传递信息。

经典寄存器是一个类似于经典计算机中的比特（bit）的概念，它代表了一个经典的二进制值（0或1）。

在量子计算中，经典寄存器用于记录量子计算的结果。当量子计算完成后，量子比特的测量结果将被存储在经典寄存器中，以供后续的经典计算和分析使用。

在一些量子计算算法和量子门操作中，可能需要基于经典信息来控制量子操作，即 **QIf、QWhile** 操作等，经典寄存器可以用于记录这些控制信息，从而实现更复杂的量子计算任务。

.. class:: ClassicalCondition

    经典寄存器类

    .. method:: __init__(*args, **kwargs)

        初始化 ClassicalCondition 类实例。

    .. method:: get_val() -> int

        获取经典条件的值。

        :return: 经典条件的值。
        :rtype: int

    .. method:: set_val(value: int) -> None

        设置经典条件的值。

        :param value: 要设置的经典条件的值。
        :type value: int
        :return: 无返回值。

    .. method:: __add__(other: Union[ClassicalCondition, int]) -> ClassicalCondition

        重载操作符 `+`，用于经典条件的加法运算。

        :param other: 要进行加法运算的另一个经典条件或整数。
        :type other: Union[ClassicalCondition, int]
        :return: 计算结果作为新的经典条件。
        :rtype: ClassicalCondition

    .. method:: __eq__(other: Union[ClassicalCondition, int]) -> ClassicalCondition

        重载操作符 `==`，用于经典条件的等于比较。

        :param other: 要进行等于比较的另一个经典条件或整数。
        :type other: Union[ClassicalCondition, int]
        :return: 计算结果作为新的经典条件。
        :rtype: ClassicalCondition

    .. method:: __ge__(other: Union[ClassicalCondition, int]) -> ClassicalCondition

        重载操作符 `>=`，用于经典条件的大于等于比较。

        :param other: 要进行大于等于比较的另一个经典条件或整数。
        :type other: Union[ClassicalCondition, int]
        :return: 计算结果作为新的经典条件。
        :rtype: ClassicalCondition

    .. method:: __gt__(other: Union[ClassicalCondition, int]) -> ClassicalCondition

        重载操作符 `>`，用于经典条件的大于比较。

        :param other: 要进行大于比较的另一个经典条件或整数。
        :type other: Union[ClassicalCondition, int]
        :return: 计算结果作为新的经典条件。
        :rtype: ClassicalCondition

    .. method:: __le__(other: Union[ClassicalCondition, int]) -> ClassicalCondition

        重载操作符 `<=`，用于经典条件的小于等于比较。

        :param other: 要进行小于等于比较的另一个经典条件或整数。
        :type other: Union[ClassicalCondition, int]
        :return: 计算结果作为新的经典条件。
        :rtype: ClassicalCondition

    .. method:: __lt__(other: Union[ClassicalCondition, int]) -> ClassicalCondition

        重载操作符 `<`，用于经典条件的小于比较。

        :param other: 要进行小于比较的另一个经典条件或整数。
        :type other: Union[ClassicalCondition, int]
        :return: 计算结果作为新的经典条件。
        :rtype: ClassicalCondition

    .. method:: __mul__(other: Union[ClassicalCondition, int]) -> ClassicalCondition

        重载操作符 `*`，用于经典条件的乘法运算。

        :param other: 要进行乘法运算的另一个经典条件或整数。
        :type other: Union[ClassicalCondition, int]
        :return: 计算结果作为新的经典条件。
        :rtype: ClassicalCondition

    .. method:: __radd__(other: int) -> ClassicalCondition

        重载操作符 `+`，用于右侧加法运算。

        :param other: 要进行加法运算的整数。
        :type other: int
        :return: 计算结果作为新的经典条件。
        :rtype: ClassicalCondition

    .. method:: __rmul__(other: int) -> ClassicalCondition

        重载操作符 `*`，用于右侧乘法运算。

        :param other: 要进行乘法运算的整数。
        :type other: int
        :return: 计算结果作为新的经典条件。
        :rtype: ClassicalCondition

    .. method:: __rsub__(other: int) -> ClassicalCondition

        重载操作符 `-`，用于右侧减法运算。

        :param other: 要进行减法运算的整数。
        :type other: int
        :return: 计算结果作为新的经典条件。
        :rtype: ClassicalCondition

    .. method:: __rtruediv__(other: int) -> ClassicalCondition

        重载操作符 `/`，用于右侧除法运算。

        :param other: 要进行除法运算的整数。
        :type other: int
        :return: 计算结果作为新的经典条件。
        :rtype: ClassicalCondition

    .. method:: __sub__(other: Union[ClassicalCondition, int]) -> ClassicalCondition

        重载操作符 `-`，用于经典条件的减法运算。

        :param other: 要进行减法运算的另一个经典条件或整数。
        :type other: Union[ClassicalCondition, int]
        :return: 计算结果作为新的经典条件。
        :rtype: ClassicalCondition

    .. method:: __truediv__(other: Union[ClassicalCondition, int]) -> ClassicalCondition

        重载操作符 `/`，用于经典条件的除法运算。

        :param other: 要进行除法运算的另一个经典条件或整数。
        :type other: Union[ClassicalCondition, int]
        :return: 计算结果作为新的经典条件

.. _api_introduction:

接口介绍
>>>>>>>>>>>

在QPanda2中，QIfProg类用于表示执行量子程序条件判断操作，它也是QNode中的一种，QIf的定义如下：

.. class:: QIfProg

    表示量子条件分支的类，有两种初始化方式。

    .. method:: __init__(self, arg0: NodeIter) -> None

        创建一个量子条件分支节点。

        :param arg0: 分支节点的迭代器。
        :type arg0: NodeIter
        :return: 无返回值
        :rtype: None

        创建一个具有指定迭代器的量子条件分支节点。

    .. method:: __init__(self, classical_cond: ClassicalCondition, true_branch_qprog: QProg) -> None

        创建一个量子条件分支节点，具有一个正确分支的情况。

        :param classical_cond: 用于判断是否执行正确分支的经典条件。
        :type classical_cond: ClassicalCondition
        :param true_branch_qprog: 正确分支的量子线路。
        :type true_branch_qprog: QProg
        :return: 无返回值
        :rtype: None

        创建一个具有给定经典条件和正确分支量子线路的量子条件分支节点。

    .. method:: __init__(self, classical_cond: ClassicalCondition, true_branch_qprog: QProg, false_branch_qprog: QProg) -> None

        创建一个量子条件分支节点，具有正确分支和错误分支的情况。

        :param classical_cond: 用于判断是否执行正确分支的经典条件。
        :type classical_cond: ClassicalCondition
        :param true_branch_qprog: 正确分支的量子线路。
        :type true_branch_qprog: QProg
        :param false_branch_qprog: 错误分支的量子线路。
        :type false_branch_qprog: QProg
        :return: 无返回值
        :rtype: None

        创建一个具有给定经典条件、正确分支量子线路和错误分支量子线路的量子QIf节点。

    .. method:: get_classical_condition(self) -> ClassicalCondition

        获取该量子条件分支节点的经典条件。

        :return: 经典条件
        :rtype: ClassicalCondition

    .. method:: get_false_branch(self) -> QProg

        获取该量子条件分支节点的错误分支量子线路。

        :return: 错误分支量子线路
        :rtype: QProg

    .. method:: get_true_branch(self) -> QProg

        获取该量子条件分支节点的正确分支量子线路。

        :return: 正确分支量子线路
        :rtype: QProg

可以传入的QNode类型有： QProg、QCircuit、QGate、QWhileProg、QIfProg、QMeasure。

实例
>>>>>>>>>

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

