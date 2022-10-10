.. _部分振幅量子虚拟机:

部分振幅量子虚拟机
=========================
----

目前用经典计算机模拟量子虚拟机的主流解决方案有全振幅与单振幅两种。除此之外，还有部分振幅量子虚拟机，该方案能在更低的硬件条件下，实现更高的模拟效率。

使用介绍
>>>>>>>>>>>>>>>>
----

其使用方式与前面介绍的量子虚拟机模块非常类似，首先通过 ``PartialAmpQVM`` 初始化一个部分振幅量子虚拟机对象用于管理后续一系列行为

    .. code-block:: python

        from pyqpanda import *
        from numpy import pi
        machine = PartialAmpQVM()

然后是量子程序的初始化、构建与装载过程，以QPanda2的 `部分振幅示例程序` 来演示：

    .. code-block:: python

        machine.init_qvm()

        q = machine.qAlloc_many(10)
        c = machine.cAlloc_many(10)

        # 构建量子程序
        prog = QProg()
        prog << hadamard_circuit(q)\
             << CZ(q[1], q[5])\
             << CZ(q[3], q[7])\
             << CZ(q[0], q[4])\
             << RZ(q[7], pi / 4)\
             << RX(q[5], pi / 4)\
             << RX(q[4], pi / 4)\
             << RY(q[3], pi / 4)\
             << CZ(q[2], q[6])\
             << RZ(q[3], pi / 4)\
             << RZ(q[8], pi / 4)\
             << CZ(q[9], q[5])\
             << RY(q[2], pi / 4)\
             << RZ(q[9], pi / 4)\
             << CZ(q[2], q[3])

        machine.run(prog)

部分接口使用如下：

    - ``pmeasure_bin_index(string)`` ,使用示例

        .. code-block:: python

            result = machine.pmeasure_bin_index("0000000000")
            print(result)

        结果输出如下：

        .. code-block:: python

            (-0.00647208746522665, -0.006472080945968628j)

    - ``pmeasure_dec_index(string)`` ,使用示例

        .. code-block:: python

            result = machine.pmeasure_dec_index("1")
            print(result)

        结果输出如下：

        .. code-block:: python

            (-4.413170804465268e, -19-0.009152913087920392j)

    - ``pmeasure_subset(state_index)`` ,使用示例

        .. code-block:: python

            state_index = ["0", "1", "2"]
            result = machine.pmeasure_subset(state_index)
            print(result)

        结果输出如下：

        .. code-block:: python

             {'0': (-0.006472086912079613, -0.00647208691207961j), 
              '1': (-4.413170804465268e-19, -0.009152913087920392j), 
              '2': (-3.0357660829594124e-18, -0.009152913087920392j)}

        .. warning::

            部分旧的接口，比如  ``pmeasure(string)`` 、 ``pmeasure(string)`` 以及 ``get_prob_dict(qvec,string)`` 等已经被弃用了。
        
