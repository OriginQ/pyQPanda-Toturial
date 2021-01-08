QWhile
==============
----

量子程序循环控制操作，输入参数为条件判断表达式，功能是执行while循环操作。

.. _api_introduction:

接口介绍
>>>>>>>>>>>>>
----

在QPanda2中，QWhileProg类用于表示执行量子程序while循环操作，它也是QNode中的一种，初始化一个QWhileProg对象有以下两种

    .. code-block:: python

        qwile = QWhileProg(ClassicalCondition, QNode)

或

    .. code-block:: python

        qwile = create_while_prog(ClassicalCondition, QNode)

上述函数需要提供两个参数，即ClassicalCondition量子表达式与QNode节点
可以传入的QNode类型有： QProg、QCircuit、QGate、QWhileProg、QIfProg、QMeasure。

实例
>>>>>>>>>>
----

    .. code-block:: python

        from pyqpanda import *

        if __name__ == "__main__":

            init(QMachineType.CPU)
            qubits = qAlloc_many(3)
            cbits = cAlloc_many(3)
            cbits[0].set_val(0)
            cbits[1].set_val(1)

            prog = QProg()
            prog_while = QProg()

            # 构建QWhile的循环分支
            prog_while << H(qubits[0]) << H(qubits[1])<< H(qubits[2])\
                    << assign(cbits[0], cbits[0] + 1) << Measure(qubits[1], cbits[1])
            
            # 构建QWhile
            qwhile = create_while_prog(cbits[1], prog_while)
            
            # QWhile插入到量子程序中
            prog << qwhile

            # 运行，并打印测量结果
            result = directly_run(prog)
            print(result)
            print(cbits[0].get_val())
            finalize()


运行结果：

    .. code-block:: python

        2
        {'c1': False}