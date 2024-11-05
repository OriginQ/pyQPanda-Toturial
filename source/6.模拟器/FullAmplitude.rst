.. _全振幅量子虚拟机:

全振幅量子虚拟机
====================

背景介绍
---------

量子电路的经典模拟对于更好地理解量子计算的操作和行为是至关重要的。这样的模拟使研究人员和开发人员能够评估新量子算法的复杂性，并验证量子设备的有效性。

全振幅模拟是量子计算领域中最经典的模拟方案之一，用于模拟较小规模的量子系统。在这个模拟方案中，可以实现对整个量子系统的状态进行精确模拟，从而获得系统在不同时间点上的演化情况。这个方法的核心思想是表示和跟踪量子态的完整振幅信息，通过密度矩阵或纯态向量来描述量子系统的状态。

对于一个量子比特来说，可以看作是一个两能级系统，量子态 :math:`|\psi\rangle` 可以表示为：

.. math:: 

    |\psi\rangle=a_0|0\rangle+a_1|1\rangle

其中 :math:`a_0` 和 :math:`a_1` 是复振幅，并且:

.. math:: 

    \left|a_0\right|^2+\left|a_1\right|^2=1

式子中 :math:`|0\rangle` 和 :math:`|1\rangle` 是两个计算标准正交基态，量子态也可以用如下方法表示

.. math:: 

    |\psi\rangle=a_0\left[\begin{array}{l}
    1 \\
    0
    \end{array}\right]+a_1\left[\begin{array}{l}
    0 \\
    1
    \end{array}\right]=\left[\begin{array}{l}
    a_0 \\
    a_1
    \end{array}\right]

对于一个 n-比特量子系统来说，可以通过 :math:`2^n` 个振幅来表示

.. math:: 

    |\psi\rangle=a_{0 . \ldots 00}|0 \ldots 00\rangle+a_{0 . \ldots 01}|0 \ldots 01\rangle+\ldots+a_{1 . \ldots 11}|1 \ldots 11\rangle

所有振幅满足概率归一化条件，即

.. math:: 

    \sum_i\left|a_i\right|^2=1

在量子计算过程中，所有的量子逻辑门可以通过矩阵形式施加到系统中。将单门U施加到第K个量子比特上的过程可以表述为：

.. math:: 

    A=I^{\otimes n-k-1} \otimes U \otimes I^{\otimes k},

其中I是 :math:`2 \times 2` 的单位矩阵， U是 :math:`2 \times 2` 酉矩阵，对于双门操作来说，这个过程是类似的。

可以看出，随着量子比特增加，需要表征的量子态振幅数量随指数增加，具体可以参考如下表，这一问题称为量子霸权。

.. list-table::

    * - **模拟的量子比特数** 
      - **全部量子态存储所需的最低内存/GB** 
    * - 26 
      - 1
    * - 27
      - 2
    * - 28 
      - 4
    * - 29 
      - 8
    * - 30 
      - 16
    * - ... 
      - ...
    * - 48
      -  :math:`2^{22}` 
    * - 49 
      -  :math:`2^{23}` 
    * - 50
      -  :math:`2^{24}` 


当达到50比特及以上时，需要的内存数是一个天文数字，这个问题即所谓的 **量子霸权（Quantum Supremacy）** ，指量子计算机在某些特定任务上展现出超越经典计算机的能力，即在这些任务上实现了经典计算机无法模拟的优越性能。

这种现象突显了量子计算机在某些领域具有巨大的潜力，因为它们能够在短时间内解决一些经典计算机需要花费数年、数百年甚至更多时间才能解决的问题。

接口介绍
----------------

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
全振幅虚拟机支持计算float与double精度的数据，设置方式如下：
    
    .. code-block:: python

        qvm = CPUQVM()
        #True: double精度， False: float精度
        qvm.init_qvm(True)


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

一种方法中 ``prog`` 为量子程序， ``cbits`` 为 ClassicalCondition list，  ``shots`` 是一个整型数据，为量子程序运行次数。

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

        {'0000': 481, '0001': 519}

.. note:: 这个量子程序的运行结果是不确定的，但其 ``0000`` 和 ``0001`` 对应的值都应该在500左右。

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

        {'0000': 484, '0001': 516}

.. _`FullAmplitued(CPU/GPU)`:

通过函数参数选择不同的硬件资源（CPU/GPU）
-----------------------------------------

    示例代码：

    .. code-block:: python

        from pyqpanda import *

        def test_gpu():
            print("test_gpu")
            machine = FullAmplitudeQVM()
            machine.set_configure(72, 72)
            machine.init_qvm("GPU")

            q = machine.qAlloc_many(2)
            c = machine.cAlloc_many(2)

            prog = QProg()
            prog << RX(q[0], 1)
            prog << U1(q[1], 2)

            opt = PauliOperator({"Z0 Z1": 2, "X0 Y1": 3})
            hamiltonian = opt.to_hamiltonian(False)
            exp = machine.get_expectation(prog, hamiltonian,q)
            print(exp)

        def test_cpu():
            print("test_cpu")
            machine = FullAmplitudeQVM()
            machine.set_configure(72, 72)
            machine.init_qvm("CPU")

            q = machine.qAlloc_many(2)
            c = machine.cAlloc_many(2)

            prog = QProg()
            prog << RX(q[0], 1)
            prog << U1(q[1], 2)

            opt = PauliOperator({"Z0 Z1": 2, "X0 Y1": 3})
            hamiltonian = opt.to_hamiltonian(False)
            exp = machine.get_expectation(prog, hamiltonian,q)
            print(exp)

        if __name__ == "__main__":
            test_gpu()
            test_cpu()
    
    示例代码的运行结果：

    .. code-block:: bash

        test_gpu
        1.0806046117362795
        test_cpu
        1.0806046117362795
