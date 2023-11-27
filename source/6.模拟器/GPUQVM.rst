.. _QuantumMachine:

GPU量子虚拟机
====================

背景介绍
---------

GPU量子模拟器提供了另一种全振幅模拟方案，当涉及到计算密集型任务，如复杂的数学计算、图像处理和机器学习等，GPU的并行处理能力使其比CPU更高效，在量子计算的模拟中的优势体现在以下几点：

    1. **并行计算架构** ：GPU并行处理能力源于其设计理念，将多个简单的处理器组合在一起，形成大规模的计算能力。这些处理器可以同时执行多个计算任务，从而在处理大规模数据实现高效的并行计算。而量子态的向量计算中，可以分成不同区块，这些区块之间可以并行。

    2. **任务分割和调度** ：GPU在执行任务时，任务调度由GPU驱动程序负责，可以根据任务的需求动态分配处理单元和内存资源，当对大型量子线路模拟时，CPU通常需要预设计算资源分配和调度算法，而GPU可以直接交给GPU驱动程序自动调度。

    3. **高效的数据缓存和内存管理** ：GPU具有高速的显存和缓存系统，有助于减少数据访问延迟，提高计算效率。此外，GPU还支持对内存进行多层次管理，以优化数据访问和存储。

    4. **高性能编程模型和算法** ：为了方便开发者利用GPU的并行处理能力，GPU厂商提供了多种并行编程模型和工具，如CUDA、OpenCL等，量子计算模拟中的矩阵和线性计算任务能充分发挥性能优势。


接口介绍
----------------

.. class:: GPUQVM(QuantumMachine)

    GPU模拟器类,该类实现了基于GPU计算平台的量子线路模拟。

    .. method:: __init__()

        初始化 GPUQVM 类实例。

    .. method:: init_qvm() -> None

        初始化量子虚拟机。

        :return: 无返回值。

    .. method:: run_with_configuration(prog: QVec, shots : int, const NoiseModel& = NoiseModel()) -> Dict[str, int]

        获取采样测量结果的字典形式。

        :param qprog: 要运行的量子程序。
        :type qprog: QProg
        :param shots: 要采样测量的次数。
        :type shots: int
        :param noise_model: 噪声模型。默认为空的噪声模型。
        :type noise_model: Noise, optional
        :return: 包含测量结果的字典，键为测量结果的二进制字符串，值为对应的次数。
        :rtype: Dict[str, int]
        :raises run_fail: 获取测量结果失败。

    .. method:: prob_run_dict(program: QProg, qubit_list: QVec, select_max: int = -1) -> Dict[str, float]

        运行量子程序并获取测量概率结果的字典形式。

        :param program: 要运行的量子程序。
        :type program: QProg
        :param qubit_list: 用于测量的量子比特列表。
        :type qubit_list: QVec
        :param select_max: 返回的元素数量上限。默认为 -1，表示无限制。
        :type select_max: int, optional
        :return: 包含测量概率的字典，键为测量结果的二进制字符串，值为对应的测量概率。
        :rtype: Dict[str, float]
        :raises run_fail: 运行量子程序失败。

    .. method:: prob_run_list(program: QProg, qubit_list: QVec, select_max: int = -1) -> List[float]

        运行量子程序并获取测量概率结果的列表形式。

        :param program: 要运行的量子程序。
        :type program: QProg
        :param qubit_list: 用于测量的量子比特列表。
        :type qubit_list: QVec
        :param select_max: 返回的元素数量上限。默认为 -1，表示无限制。
        :type select_max: int, optional
        :return: 包含测量概率的列表。
        :rtype: List[float]
        :raises run_fail: 运行量子程序失败。

    .. method:: prob_run_tuple_list(program: QProg, qubit_list: QVec, select_max: int = -1) -> List[Tuple[int, float]]

        运行量子程序并获取测量概率结果的元组列表形式。

        :param program: 要运行的量子程序。
        :type program: QProg
        :param qubit_list: 用于测量的量子比特列表。
        :type qubit_list: QVec
        :param select_max: 返回的元素数量上限。默认为 -1，表示无限制。
        :type select_max: int, optional
        :return: 包含测量概率的元组列表，每个元组包含测量结果的索引和对应的概率。
        :rtype: List[Tuple[int, float]]
        :raises run_fail: 运行量子程序失败。

GPU模拟器的使用方法和CPUQVM类似，代码示例如下：

代码示例
---------------------------------------------------

    .. code-block:: python

        from pyqpanda import *
        from numpy import pi

        if __name__ == "__main__":

            qvm = GPUQVM()
            qvm.init_qvm()

            qvm.set_configure(29, 29)
            q = qvm.qAlloc_many(4)
            c = qvm.cAlloc_many(4)

            # 构建量子程序
            prog = QProg()
            prog << H(q[0])\
                    << CNOT(q[0], q[1])\
                    << RZ(q[0], pi / 4)\
                    << RX(q[2], pi / 4)\
                    << CZ(q[0], q[1])\
                    << CZ(q[2], q[3])

            measure_prog = QProg()
            measure_prog << prog\
                        << Measure(q[0], c[0])\
                        << Measure(q[1], c[1])
            
            # 量子程序运行1000次，并返回测量结果
            measure_result = qvm.run_with_configuration(measure_prog, 1000)

            prob_result = qvm.prob_run_dict(prog, [q[0],q[1]])
            
            # 打印量子态在量子程序多次运行结果中出现的次数
            print(measure_result)
            print(prob_result)
            qvm.finalize()

运行结果：

    .. code-block:: python

        {'00': 497, '11': 503}
        {'00': 0.5, '01': 0.0, '10': 0.0, '11': 0.5}

.. note:: 使用GPU虚拟机需要本地运行环境有cuda环境
