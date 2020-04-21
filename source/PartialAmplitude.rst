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
        PI = 3.141593
        machine = PartialAmpQVM()

然后是量子程序的初始化、构建与装载过程，以QPanda2的 :ref:`部分振幅示例程序`来演示：

    .. code-block:: python

        machine.init_qvm()

        q = machine.qAlloc_many(10)
        c = machine.cAlloc_many(10)

        prog = QProg()

        prog.insert(hadamard_circuit(q))\
            .insert(CZ(q[1], q[5]))\
            .insert(CZ(q[3], q[7]))\
            .insert(CZ(q[0], q[4]))\
            .insert(RZ(q[7], PI / 4))\
            .insert(RX(q[5], PI / 4))\
            .insert(RX(q[4], PI / 4))\
            .insert(RY(q[3], PI / 4))\
            .insert(CZ(q[2], q[6]))\
            .insert(RZ(q[3], PI / 4))\
            .insert(RZ(q[8], PI / 4))\
            .insert(CZ(q[9], q[5]))\
            .insert(RY(q[2], PI / 4))\
            .insert(RZ(q[9], PI / 4))\
            .insert(CZ(q[2], q[3]))

        machine.run(prog)

部分接口使用如下：

    - ``pmeasure_bin_index(string)`` ,使用示例

        .. code-block:: python

            result = machine.pmeasure_bin_index("0000000000")
            print(result)

        结果输出如下：

        .. code-block:: python

            (-0.00647208746522665-0.006472080945968628j)

    - ``pmeasure_dec_index(string)`` ,使用示例

        .. code-block:: python

            result = machine.pmeasure_dec_index("1")
            print(result)

        结果输出如下：

        .. code-block:: python

            (-6.068964220062867e-10-0.009152906015515327j)

    - ``pmeasure_subset(state_index)`` ,使用示例

        .. code-block:: python

            state_index = ["0", "1", "2"]
            result = machine.pmeasure_subset(state_index)
            print(result)

        结果输出如下：

        .. code-block:: python

             {'0': (-0.00647208746522665-0.006472080945968628j), 
              '1': (-6.068964220062867e-10-0.009152906015515327j), 
              '2': (-6.984919309616089e-10-0.009152908809483051j)}

        .. warning::

            部分旧的接口，比如 ``get_qstate()`` 、 ``pmeasure(string)`` 、 ``pmeasure(string)`` 以及 ``get_prob_dict(qvec,string)`` 等已经被弃用了。
        
