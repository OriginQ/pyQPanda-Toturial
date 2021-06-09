
交叉熵基准
==========================

简介
--------------
交叉熵基准测试（xeb）是一种通过应用随机电路并测量观察到的位串测量值与从模拟获得的这些位串的预期概率之间的交叉熵来评估门性能的方法。

接口说明
--------------
``double_gate_xeb`` 输入参数分别噪声虚拟机或者量子云机器、待测量的量子比特0、待测量的量子比特1、线路不同层数、随机线路的数量、测量次数、验证双门类型（默认CZ门）。
输出为字典数据，key为线路层数，value对应符合期望概率的大小。

实例
--------------
.. code-block:: python

    from pyqpanda import *

    if __name__=="__main__":

        # 构建噪声虚拟机，调整噪声模拟真实芯片
        qvm = NoiseQVM()
        qvm.init_qvm()
        qv = qvm.qAlloc_many(4)

        # 设置噪声参数
        qvm.set_noise_model(NoiseModel.DEPOLARIZING_KRAUS_OPERATOR, GateType.CZ_GATE, 0.1)
        
        # 同样可以申请云计算机器（采用真实芯片）
        # qvm =  QCloud()
        # qvm.init_qvm("898D47CF515A48CEAA9F2326394B85C6")

        # 设置不同层数组合
        range = [2,4,6,8,10]
        # 现在可测试双门类型主要为CZ CNOT SWAP ISWAP SQISWAP
        res = double_gate_xeb(qvm, qv[0], qv[1], range, 10, 1000, GateType.CZ_GATE)
        # 对应的数值随噪声影响，噪声数值越大，所得结果越小，且层数增多，结果数值越小。

        print(res)

        qvm.finalize()

运行结果：
::

   {2: 0.9922736287117004, 4: 0.9303175806999207, 6: 0.7203856110572815, 8: 0.7342230677604675, 10: 0.7967881560325623}