
随机基准
==========================

简介
--------------

随机基准测试（Randomized Benchmarking，RB）是量子计算中一种用于量子门性能评估的实验技术。它用于测量量子门的错误率，提供了关于量子计算系统的噪声水平和稳定性的信息。RB 是一种广泛使用的方法，用于评估量子设备的可靠性和错误率。


算法流程
--------------

在随机基准测试中，主要思想是通过对随机序列的一系列量子门操作进行测量，来评估量子门的错误率。这些随机序列的特点是它们会趋向于互相抵消，从而减少系统噪声的影响。通过比较实际测量结果和理论预期，可以估计出量子门的错误率。

实验过程如下：

1. 生成随机序列：生成一系列随机的量子门序列，这些序列涵盖了不同的量子门操作和顺序。

2. 实验操作：在量子设备上依次执行生成的随机序列。

3. 测量结果：对每个随机序列，测量量子比特的状态，并记录测量结果。

1，2，3步的具体操作如下：

.. admonition:: 1,2,3步的具体操作
   :class: tip

    在Clifford群中随机需求m个门，构成一个序列；
    计算该序列的等效 :math:`U` 操作，该操作的逆 :math:`\mathrm{U}^{-1}` 一定也在Clifford群中，将 :math:`\mathrm{U}^{-1}` 添加到序列中作为第m+1个元素，构成一个完整的序列;
    测量量子比特在该序列操作之后的0态（初态在0态）保真度 :math:`y_{mk}` 。

4. 分析：通过比较预期测量结果和实际测量结果，可以得出量子门的错误率。通常使用指数递减模型来分析错误率。

5. 错误率估计：通过分析获得的数据，可以估计出不同量子门的平均错误率。



.. admonition:: 4,5步的具体操作
   :class: tip


    计算序列长度为m时的平均保真度 :math:`y_m=\frac{1}{K} \sum_1^K y_{m k}` , 得到序列平均保真度y和序列长度m的关系，并用公式下面拟合：

    .. math::

        \begin{aligned}
        y=A * p^m+B
        \end{aligned}

    门操作平均错误率 :math:`r_c` 与拟合参数𝑝的关系：

    .. math::

        \begin{aligned}
        r_c=(1-p) *\left(2^n-1\right) / 2^n
        \end{aligned}




随着Clifford门数量的增加，门序列的平均成功概率会下降，因为当重复应用包含错误的量子门时，整个门序列的错误概率会单调增加,在 RB 中，通常假设不同Clifford的噪声超算子相等，在此假设下，门序列的平均成功概率已被证明随Clifford门的数量呈指数衰减。

接口说明
--------------

1.单门随机基准测试： ``single_qubit_rb`` 。

.. function:: single_qubit_rb(config: QCloudTaskConfig, qubit: int, clifford_range: List[int], num_circuits: int, interleaved_gates: List[QGate] = []) -> Dict[int,float]

    此函数用于执行单比特随机电路基准（Single Qubit Randomized Benchmarking）实验。
    
    :param config: QCloudTaskConfig 对象，表示云量子任务的配置。
    :type config: QCloudTaskConfig
    :param qubit: 单比特量子比特索引。
    :type qubit: int
    :param clifford_range: 包含 Clifford 门的序列长度范围的列表，用于指定不同长度的 Clifford 门序列。
    :type clifford_range: List[int]
    :param num_circuits: 要执行的电路数量。
    :type num_circuits: int
    :param interleaved_gates: 包含插入在 Clifford 门序列中的额外门的列表，默认为空列表。
    :type interleaved_gates: List[QGate], optional
    :return: 包含单比特随机电路基准实验结果的字典，其中键是 Clifford 门序列长度，值是误差概率。
    :rtype: Dict[int,float]
    :raises run_fail: 执行单比特随机电路基准实验失败。

2.双门随机基准测试： ``double_qubit_rb`` 。

.. function:: double_qubit_rb(config: QCloudTaskConfig, qubit0: int, qubit1: int, clifford_range: List[int], num_circuits: int, interleaved_gates: List[QGate] = []) -> Dict[int,float]

    此函数用于执行双比特随机电路基准（Double Qubit Randomized Benchmarking）实验。
    
    :param config: QCloudTaskConfig 对象，表示云量子任务的配置。
    :type config: QCloudTaskConfig
    :param qubit0: 双比特第一个量子比特索引。
    :type qubit0: int
    :param qubit1: 双比特第二个量子比特索引。
    :type qubit1: int
    :param clifford_range: 包含 Clifford 门的序列长度范围的列表，用于指定不同长度的 Clifford 门序列。
    :type clifford_range: List[int]
    :param num_circuits: 要执行的电路数量。
    :type num_circuits: int
    :param interleaved_gates: 包含插入在 Clifford 门序列中的额外门的列表，默认为空列表。
    :type interleaved_gates: List[QGate], optional
    :return: 包含双比特随机电路基准实验结果的字典，其中键是 Clifford 门序列长度，值是误差概率。
    :rtype: Dict[int,float]
    :raises run_fail: 执行双比特随机电路基准实验失败。

实例
--------------

.. code-block:: python

    from pyqpanda import *

    if __name__=="__main__":  

        # 设置随机线路中clifford门集数量
        range = [ 5,10,15 ]

        #设置用户真实apikey，需要确保有足够算力资源
        online_api_key = "XXX"

        #配置量子计算任务参数
        config = QCloudTaskConfig()
        config.cloud_token = online_api_key
        config.chip_id = origin_72
        config.open_amend = False
        config.open_mapping = False
        config.open_optimization = False
        config.shots = 1000

        #测量单比特随机基准
        single_rb_result = single_qubit_rb(config, 0, range, 20)

        #同样可以测量两比特随机基准
        double_rb_result = double_qubit_rb(config, 0, 1, range, 20)
        
        #对应的数值随设备噪声影响，噪声数值越大，所得结果越小，且随clifford门集数量增多，结果数值越小。
        print(single_rb_result)
        print(double_rb_result)

        #运行结果：
        # {5: 0.464, 10: 0.4535, 15: 0.437}
        # {5: 0.1675, 10: 0.20750000000000002, 15: 0.198}

参考文献
----

::

    [1] Easwar Magesan, J. M. Gambetta, and Joseph Emerson, Robust randomized benchmarking of quantum processes, https://arxiv.org/abs/1009.3639.
    [2] Easwar Magesan, Jay M. Gambetta, and Joseph Emerson, Characterizing Quantum Gates via Randomized Benchmarking, https://arxiv.org/abs/1109.6887.