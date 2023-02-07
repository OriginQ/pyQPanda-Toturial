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

其使用方式与前面介绍的量子虚拟机模块非常类似。主要接口有以下几种：

``run``  ：输入参数为执行的量子程序，申请的量子比特，最大RANK，quickBB优化的最大运行时间。

``pmeasure_bin_index``  ：输入参数为二进制索引字符串，输出为该索引下的量子态概率。使用前需要调用run接口如 pmeasure_bin_index("0000000000") ，同时保证字符串长度与测量的比特数相同。

``pmeasure_dec_index``  ：输入参数为十进制索引字符串，输出为该索引下的量子态概率。使用前需要调用run接口。如 pmeasure_dec_index("1")，同时保证索引大小不超过2的n次方(n为比特数)。

``pmeasure_bin_amplitude``  ：输入参数为二进制索引字符串，输出为该索引下的量子态振幅。使用前需要调用run接口如 pmeasure_bin_amplitude("0000000000") ，同时保证字符串长度与测量的比特数相同。

``pmeasure_dec_amplitude``  ：输入参数为十进制索引字符串，输出为该索引下的量子态振幅。使用前需要调用run接口。如 pmeasure_dec_amplitude("1")，同时保证索引大小不超过2的n次方(n为比特数)。

``get_prob_dict``  ：输入参数为要执行的量子程序，以及要测量的量子比特。输出为对应量子比特的所有态结果。使用前需要调用run接口。需要注意的是该接口要求量子比特数为30个以内时使用。

``prob_run_dict``  ：输入参数为要执行的量子程序，以及要测量的量子比特。输出为对应量子比特的所有态结果。需要注意的是该接口要求量子比特数为30个以内时使用。

首先通过 ``SingleAmpQVM`` 初始化一个单振幅量子虚拟机对象用于管理后续一系列行为。

    .. code-block:: python

        from pyqpanda import *
        from numpy import pi
        
        qvm = SingleAmpQVM()

然后是量子程序的初始化、构建与装载过程：

    .. code-block:: python

        qvm.init_qvm()

        qv = qvm.qAlloc_many(10)
        cv = qvm.cAlloc_many(10)

        prog = QProg()

        # 构建量子程序
        prog << CZ(qv[1], qv[5])\
            << CZ(qv[3], qv[5])\
            << CZ(qv[2], qv[4])\
            << CZ(qv[3], qv[7])\
            << CZ(qv[0], qv[4])\
            << RY(qv[7], pi / 2)\
            << RX(qv[8], pi / 2)\
            << RX(qv[9], pi / 2)\
            << CR(qv[0], qv[1], pi)\
            << CR(qv[2], qv[3], pi)\
            << RY(qv[4], pi / 2)\
            << RZ(qv[5], pi / 4)\
            << RX(qv[6], pi / 2)\
            << RZ(qv[7], pi / 4)\
            << CR(qv[8], qv[9], pi)\
            << CR(qv[1], qv[2], pi)\
            << RY(qv[3], pi / 2)\
            << RX(qv[4], pi / 2)\
            << RX(qv[5], pi / 2)\
            << CR(qv[9], qv[1], pi)\
            << RY(qv[1], pi / 2)\
            << RY(qv[2], pi / 2)\
            << RZ(qv[3], pi / 4)\
            << CR(qv[7], qv[8], pi)

接口使用如下：

``pmeasure_bin_index`` ,使用时需要结合 ``run`` 方法。用法示例：

    .. code-block:: python

        # run 有三个参数，默认2个，
        #  第一个执行的量子程序
        #  第二个为申请的量子比特
        # 第三个为最大RANK，这里根据内存设置，默认30
        # 第四个就是quickBB优化的最大运行时间，默认5s

        qvm.run(prog, qv)
        bin_result = qvm.pmeasure_bin_index("0001000000") 
        print("0001000000 : ", bin_result)

结果输出如下：

    .. code-block:: python

        0001000000 :  0.001953123603016138

``pmeasure_dec_index`` ,使用时需要结合 ``run`` 方法。用法示例：

    .. code-block:: python

        qvm.run(prog, qv)
        dec_result = qvm.pmeasure_dec_index("2")
        print("2 : ",dec_result)

结果输出如下：

    .. code-block:: python

        2 :  0.001953123603016138

``get_prob_dict``,使用时需要结合 ``run`` 方法。用法示例：

    .. code-block:: python

        qvm.run(prog, qv)
        res = qvm.get_prob_dict(qv)  


``prob_run_dict`` 接口是 ``get_prob_dict`` 和 ``run`` 的封装，用法示例：

    .. code-block:: python

        res_1 = qvm.prob_run_dict(prog, qv)
  