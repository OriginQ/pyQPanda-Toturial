.. _Measure:

量子测量
================

量子测量是指通过外界对量子系统进行干扰来获取需要的信息，测量门使用的是蒙特卡洛方法的测量。在量子线路中用如下图标表示：

.. image:: images/QGate_measure.png
    :width: 65

.. _api_introduction:

接口介绍
----------------

本章主要介绍获得量子测量对象、根据配置运行含有量子测量的量子程序、快速测量。

在量子程序中我们需要对某个量子比特做测量操作，并把测量结果存储到经典寄存器上，可以通过下面的方式获得一个测量对象：

    .. code-block:: python

        measure = Measure(qubit, cbit); 

可以看到Measure接两个参数， 第一个是测量比特，第二个是经典寄存器。

如果想测量所有的量子比特并将其存储到对应的经典寄存器上， 可以如下操作：

    .. code-block:: python

        measureprog = measure_all(qubits， cbits);

其中qubits的类型是 ``QVec`` ， cbits的类型是 ``ClassicalCondition list``。

.. note:: ``measure_all`` 的返回值类型是 ``QProg``。

在得到含有量子测量的程序后，我们可以调用 ``directly_run`` 或 ``run_with_configuration`` 来得到量子程序的测量结果。

``directly_run`` 的功能是运行量子程序并返回运行的结果， 使用方法如下：

    .. code-block:: python

        prog = QProg()
        prog << H(qubits[0])\
             << CNOT(qubits[0], qubits[1])\
             << CNOT(qubits[1], qubits[2])\
             << CNOT(qubits[2], qubits[3])\
             << Measure(qubits[0], cbits[0])

        result = directly_run(prog)

``run_with_configuration`` 的功能是统计量子程序多次运行的测量结果， 使用方法如下：

    .. code-block:: python

        prog = QProg()
        prog << H(qubits[0])\
             << H(qubits[0])\
             << H(qubits[1])\
             << H(qubits[2])\
             << measure_all(qubits, cbits)

        result = run_with_configuration(prog, cbits, 1000)

其中第一个参数是量子程序，第二个参数是ClassicalCondition list， 第三个参数是运行的次数。

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


