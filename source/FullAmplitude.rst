.. _QuantumMachine:

全振幅量子虚拟机
====================

全振幅量子虚拟机一次可以模拟计算出量子态的所有振幅，计算方式支持CPU、单线程计算和GPU，可以在初始化时配置，使用方式是完全一样的，只是其计算效率不同。

接口介绍
----------------

全振幅量子虚拟机类型：

.. code-block:: python

    class QMachineType(__pybind11_builtins.pybind11_object):
    """
        Members:
        
        CPU
        
        GPU
        
        CPU_SINGLE_THREAD
        
        NOISE
    """

QPanda2中在构造量子虚拟机时有以下几种方式：

    .. code-block:: python

        init(QMachineType.CPU)  # 使用init,不会返回qvm，会在代码中生成一个全局的qvm
        auto qvm = init_quantum_machine(QMachineType.CPU) # 通过接口得到quantum machine对象
        qvm = CPUQVM() # 新建一个quantum machine对象

.. note:: ``init`` 和 ``init_quantum_machine`` 这两个函数不是线程安全的，不适用于多线程编程，而且其最大的量子比特个数和经典寄存器个数均为默认值25。

设置好配置之后要初始化量子虚拟机：

    .. code-block:: python

        qvm.init_qvm()

.. note:: 调用 ``init`` 和 ``init_quantum_machine`` 接口， 就不需要初始化了。

下面我们就需要去申请量子比特和经典寄存器。

设置最大量子比特个数

.. code-block:: python

        # 设置最大量子比特个数和最大经典寄存器个数
        qvm.set_configure(30, 30)

.. note:: 若不设置则默认最大比特为29。

例如我们申请4个量子比特：

    .. code-block:: python

        qubits = qvm.qAlloc_many(4)

申请一个量子比特时也可以用这个接口：

    .. code-block:: python

        qubit = qvm.qAlloc()

申请经典寄存器也有类似于申请量子比特的接口，其使用方法和申请量子比特的方法一样，如申请4个经典寄存器的方法：

    .. code-block:: python

        cbits = qvm.cAlloc_many(4)

申请一个经典寄存器时也可以用这个接口：

    .. code-block:: python

        cbit = qvm.cAlloc()


在一个量子虚拟机中，申请了几次量子比特或经典寄存器，我们想知道一共申请了多少个量子比特或经典寄存器可以用下面的方法：

    .. code-block:: python

        num_qubit = qvm.get_allocate_qubit_num() # 申请量子比特的个数
        num_cbit = qvm.get_allocate_cmem_num() # 申请经典寄存器的个数

我们该如何使用量子虚拟机来执行量子程序呢？ 可以用下面的方法：

    .. code-block:: python

        prog = QProg()
        prog << H(qubits[0]) << CNOT(qubits[0], qubits[1]) << Measure(qubits[0], cbits[0])
        
        result = qvm.directly_run(prog) # 执行量子程序

如果想多次运行一个量子程序，并得到每次量子程序的结果，除了循环调用 ``directly_run`` 方法外， 我们还提供了一个接口 ``run_with_configuration`` ，该接口有两种重载方法，具体方法如下：

    .. code-block:: python

        result = qvm.run_with_configuration(prog, cbits, shots)

一种方法中中 ``prog`` 为量子程序， ``cbits`` 为 ClassicalCondition list，  ``shots`` 是一个整形数据，为量子程序运行次数。

    .. code-block:: python

        result = qvm.run_with_configuration(prog, cbits, config)

另一种方法中 ``prog`` 为量子程序， ``cbits`` 为 ClassicalCondition list, ``config`` 是一个字典类型的数据，内容如下：	

    .. code-block:: python	

        config = {'shots': 1000}	



如果想得到量子程序运行之后各个量子态的振幅值，可以调用 ``get_qstate`` 函数获得：

    .. code-block:: python

        stat = qvm.get_qstate()

量子虚拟机中测量和概率使用方法与 :ref:`Measure` 和 :ref:`PMeasure` 中介绍的相同，在这里就不多做赘述。

实例1
-----------------

    .. code-block:: python

        from pyqpanda import *

        if __name__ == "__main__":
            qvm = CPUQVM()
            qvm.init_qvm()

            qvm.set_configure(29, 29)
            qubits = qvm.qAlloc_many(4)
            cbits = qvm.cAlloc_many(4)

            # 构建量子程序
            prog = QProg()
            prog << H(qubits[0]) << CNOT(qubits[0], qubits[1]) << Measure(qubits[0], cbits[0])
            
            # 量子程序运行1000次，并返回测量结果
            result = qvm.run_with_configuration(prog, cbits, 1000)
            
            # 打印量子态在量子程序多次运行结果中出现的次数
            print(result)
            qvm.finalize()


运行结果：

    .. code-block:: python

        {'0000': 481, '1000': 519}

.. note:: 这个量子程序的运行结果是不确定的，但其 ``0000`` 和 ``1000`` 对应的值都应该在500左右。

为了方便使用，pyqpanda还封装了一些面向过程的接口，接口名称和使用方法与上述的基本相同。我们将上面的例子修改为面向过程的接口如下：

实例2
------------------

    .. code-block:: python

        from pyqpanda import *

        if __name__ == "__main__":
            init(QMachineType.CPU)
            qubits = qAlloc_many(4)
            cbits = cAlloc_many(4)

            # 构建量子程序
            prog = QProg()
            prog << H(qubits[0]) << CNOT(qubits[0], qubits[1]) << Measure(qubits[0], cbits[0])
            
            # 量子程序运行1000次，并返回测量结果
            result = run_with_configuration(prog, cbits, 1000)
            
            # 打印量子态在量子程序多次运行结果中出现的次数
            print(result)
            finalize()


运行结果：

    .. code-block:: python

        {'0000': 484, '1000': 516}
