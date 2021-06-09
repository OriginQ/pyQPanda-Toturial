
随机基准
==========================

简介
--------------
随机基准测试（RB）是使用随机化方法对量子门进行基准测试。由于完整的过程层析成像对于大型系统是不可行的，因此越来越关注可扩展方法，
以部分表征影响量子系统的噪声。在\ `[1] <https://arxiv.org/pdf/1009.3639>`__\ 中提出了一种可扩展的、鲁棒的算法（n个量子位组成的系统），
使用随机技术通过单个参数对整个Clifford门进行基准测试的鲁棒算法。

接口说明
--------------
``single_qubit_rb`` 的输入参数分别噪声虚拟机或者量子云机器，待测量的量子比特，随机线路clifford门集的不同数量组合、随机线路的数量、测量次数、验证基本逻辑门（默认无），输出为\ ``std::map``
数据， 关键值为clifford门集数量，数值对应符合期望概率的大小。

``double_qubit_rb`` 的输入参数分别噪声虚拟机或者量子云机器，待测量的量子比特0，待测量的量子比特1，随机线路clifford门集的不同数量组合、随机线路的数量、测量次数、验证基本逻辑门（默认无）输出为\ ``std::map``
数据， 关键值为clifford门集数量，数值对应符合期望概率的大小。

实例
--------------
.. code-block:: python

    from pyqpanda import *

    if __name__=="__main__":  
        # 构建噪声虚拟机，调整噪声模拟真实芯片
        qvm = NoiseQVM()
        qvm.init_qvm()
        qvm.set_noise_model(NoiseModel.DEPOLARIZING_KRAUS_OPERATOR, GateType.CZ_GATE, 0.005)
        qvm.set_noise_model(NoiseModel.DEPOLARIZING_KRAUS_OPERATOR, GateType.PAULI_Y_GATE, 0.005)
        qv = qvm.qAlloc_many(4)

        # 同样可以申请云计算机器（采用真实芯片）
        # qvm =  QCloud()
        # qvm.init_qvm("898D47CF515A48CEAA9F2326394B85C6")

        # 设置随机线路中clifford门集数量
        range = [ 5,10,15 ]

        # 测量单比特随机基准
        res = single_qubit_rb(qvm, qv[0], range, 10, 1000)

        # 同样可以测量两比特随机基准
        #res = double_qubit_rb(qvm, qv[0], qv[1], range, 10, 1000)
       
        # 对应的数值随噪声影响，噪声数值越大，所得结果越小，且随clifford门集数量增多，结果数值越小。
        print(res)

        qvm.finalize()

运行结果：

::
    
    {5: 0.9996, 10: 0.9999, 15: 0.9993000000000001}