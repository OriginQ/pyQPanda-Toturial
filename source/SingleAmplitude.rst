.. _单振幅量子虚拟机:

单振幅量子虚拟机
======================
----

目前我们可以通过量子计算的相关理论，用经典计算机实现模拟量子虚拟机。
量子虚拟机的模拟主要有全振幅与单振幅两种解决方案，其主要区别在于，全振幅一次模拟计算就能算出量子态的所有振幅，单振幅一次模拟计算只能计算出 :math:`2^{N}` 个振幅中的一个。

然而全振幅模拟量子计算时间较长，计算量随量子比特数指数增长，
在现有硬件下，无法模拟超过49量子比特。通过单振幅量子虚拟机技术可以模拟超过49量子比特，同时模拟速度有较大提升，且算法的计算量不随量子比特数指数提升。

使用介绍
>>>>>>>>>>>>>>>>
----

其使用方式与前面介绍的量子虚拟机模块非常类似，首先通过 ``SingleAmpQVM`` 初始化一个单振幅量子虚拟机对象用于管理后续一系列行为

    .. code-block:: python

        from pyqpanda import *
        from numpy import pi
        
        machine = SingleAmpQVM()

然后是量子程序的初始化、构建与装载过程：

    .. code-block:: python

        machine.init_qvm()

        q = machine.qAlloc_many(10)
        c = machine.cAlloc_many(10)

        prog = QProg()

        # 构建量子程序
        prog << hadamard_circuit(q)\
             << CZ(q[1], q[5])\
             << CZ(q[3], q[5])\
             << CZ(q[2], q[4])\
             << CZ(q[3], q[7])\
             << CZ(q[0], q[4])\
             << RY(q[7], pi / 2)\
             << RX(q[8], pi / 2)\
             << RX(q[9], pi / 2)\
             << CR(q[0], q[1], pi)\
             << CR(q[2], q[3], pi)\
             << RY(q[4], pi / 2)\
             << RZ(q[5], pi / 4)\
             << RX(q[6], pi / 2)\
             << RZ(q[7], pi / 4)\
             << CR(q[8], q[9], pi)\
             << CR(q[1], q[2], pi)\
             << RY(q[3], pi / 2)\
             << RX(q[4], pi / 2)\
             << RX(q[5], pi / 2)\
             << CR(q[9], q[1], pi)\
             << RY(q[1], pi / 2)\
             << RY(q[2], pi / 2)\
             << RZ(q[3], pi / 4)\
             << CR(q[7], q[8], pi)

        machine.run(prog)

接口使用如下：

- ``pmeasure_bin_index(string)`` ,使用示例

    .. code-block:: python

        result = machine.pmeasure_bin_index(prog,"0000000000")
        print(result)

    结果输出如下：

    .. code-block:: python

        0.0016670938348397613

- ``pmeasure_dec_index(string)`` ,使用示例

    .. code-block:: python

        result = machine.pmeasure_dec_index(prog,"1")
        print(result)

    结果输出如下：

    .. code-block:: python

        0.0016670938348397613
