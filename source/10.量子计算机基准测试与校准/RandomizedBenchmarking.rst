
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

.. function:: single_qubit_rb(qvm: QuantumMachine, qubit: Qubit, clifford_range: List[int], num_circuits: int, shots: int, chip_id: int = 2, interleaved_gates: List[QGate] = []) -> Dict[int, float]

    该函数用于在量子芯片上进行单比特随机基准测试。通过对指定的单比特量子线路进行随机化的 Clifford 门序列操作，以评估量子设备的性能。

    :param qvm: 量子机器对象，可以是芯片实际或模拟量子机器。
    :type qvm: QuantumMachine
    :param qubit: 待测试的单比特量子比特。
    :type qubit: Qubit
    :param clifford_range: Clifford 门序列的范围列表，用于构建随机序列。
    :type clifford_range: List[int]
    :param num_circuits: 随机序列的数量，用于统计结果。
    :type num_circuits: int
    :param shots: 每个序列的测量次数，用于获取统计概率。
    :type shots: int
    :param chip_id: 芯片标识，默认为 2（本源悟源5号）。
    :type chip_id: int, optional
    :param interleaved_gates: 用于插入随机序列的门操作列表，默认为空列表。
    :type interleaved_gates: List[QGate], optional
    :return: 包含测试结果数据的字典，键为 Clifford 门序列长度，值为对应的指数衰减指数。
    :rtype: Dict[int, float]
    :raises run_fail: 单比特随机基准测试运行失败。

    示例用法::

        # 在量子芯片上对单比特进行随机基准测试
        result_dict = single_qubit_rb(my_qvm, qubit=qubit_0, clifford_range=[1, 10, 20], num_circuits=100, shots=1024)

        # 在量子芯片上对单比特进行随机基准测试，插入额外的门操作
        result_dict = single_qubit_rb(my_qvm, qubit=qubit_1, clifford_range=[1, 5, 10], num_circuits=50, shots=512, interleaved_gates=[H(qubit_1)])

2.双门随机基准测试： ``double_qubit_rb`` 。

.. function:: double_qubit_rb(qvm: QuantumMachine, qubit0: Qubit, qubit1: Qubit, clifford_range: List[int], num_circuits: int, shots: int, chip_id: int = 2, interleaved_gates: List[QGate] = []) -> Dict[int, float]

    该函数用于在给定的双量子比特上进行随机基准测试，测试芯片或量子模拟器的噪声水平。
    
    :param qvm: 量子机器。
    :type qvm: QuantumMachine
    :param qubit0: 第一个双量子比特。
    :type qubit0: Qubit
    :param qubit1: 第二个双量子比特。
    :type qubit1: Qubit
    :param clifford_range: Clifford序列的长度范围列表。
    :type clifford_range: List[int]
    :param num_circuits: 测试电路数量。
    :type num_circuits: int
    :param shots: 测量的次数。
    :type shots: int
    :param chip_id: 芯片标识，默认为2（本源悟源5号）。
    :type chip_id: int, optional
    :param interleaved_gates: 交错门列表，默认为空列表。
    :type interleaved_gates: List[QGate], optional
    :return: 包含测试结果的字典，键为Clifford序列的长度，值为对应的测试结果（成功概率）。
    :rtype: Dict[int, float]
    :raises run_fail: 双量子比特随机基准测试失败。

    示例用法（不插入门操作）::

        # 在量子芯片上对双量子比特进行随机基准测试
        result_dict = double_qubit_rb(my_qvm, qubit0, qubit1, clifford_range=[1, 10, 20], num_circuits=100, shots=1024)

        # 在量子芯片上对双量子比特进行随机基准测试，并插入额外的CZ门操作
        result_dict = double_qubit_rb(my_qvm, qubit0, qubit1, clifford_range=[1, 10, 20], num_circuits=100, shots=1024, interleaved_gates=[CZ(qubit0, qubit1)])

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


参考文献
----

::

    [1] Easwar Magesan, J. M. Gambetta, and Joseph Emerson, Robust randomized benchmarking of quantum processes, https://arxiv.org/abs/1009.3639.
    [2] Easwar Magesan, Jay M. Gambetta, and Joseph Emerson, Characterizing Quantum Gates via Randomized Benchmarking, https://arxiv.org/abs/1109.6887.