
量子体积
==========================

简介
--------------
量子体积（\ **Quantum
Volume**\ ）[1]，是一个用于评估量子计算系统性能的协议。它表示可以在系统上执行的最大等宽度深度的随机线路。量子计算系统的操作保真度越高，关联性越高，有越大的校准过的门操作集合便会有越高的量子体积。量子体积与系统的整体性能相关联，即与系统的整体错误率，潜在的物理比特关联和门操作并行度相联系。总的来说，量子体积是一个用于近期整体评估量子计算系统的一个实用方法，数值越高，系统整体错误率就越低，性能就越好。

测量量子体积的标准做法就是对系统使用规定的量子线路模型执行随机的线路操作，尽可能地将比特纠缠在一起，然后再将实验得到的结果与模拟的结果进行比较。按要求分析统计结果。

量子体积被定义为指数形式：

.. math::


   V_Q=2^n

其中n表示在给定比特数目m（m大于n）和完成计算任务的条件下，系统操作的最大逻辑深度，如果芯片能执行的最大逻辑深度n大于比特数m，那么系统的量子体积就是

.. math::


   2^m


接口说明
--------------

.. function:: calculate_quantum_volume(QuantumMachine: QVM, qubit_list: List[List[int]], ntrials: int, shots: int = 1000) -> int

    此函数用于对噪声量子机器或云量子计算机进行量子体积的计算。

    :param QuantumMachine: 噪声量子机器或云量子计算机。
    :type noise_qvm: NoiseQVM or QCloud
    :param qubit_list: 量子比特列表。
    :type qubit_list: List[List[int]]
    :param ntrials: 实验次数。
    :type ntrials: int
    :param shots: 测量次数。默认为 1000。
    :type shots: int, optional
    :return: 计算得到的量子体积。
    :rtype: int
    :raises run_fail: 计算量子体积失败。

实例
--------------

.. code-block:: python

    from pyqpanda import *

    if __name__=="__main__":
        #构建噪声虚拟机，设置噪声参数
        qvm = NoiseQVM()
        qvm.init_qvm()
        qvm.set_noise_model(NoiseModel.DEPOLARIZING_KRAUS_OPERATOR, GateType.CZ_GATE, 0.005)

        #同样可以申请云计算机器（采用真实芯片），采用真实芯片要考虑芯片构造
        #qvm = QCloud()
        #qvm.init_qvm("898D47CF515A48CEAA9F2326394B85C6")
        
        #构建待测量的量子比特组合， 这里比特组合为2组，其中 量子比特3、4为一组；量子比特2，3，5为一组
        qubit_lists = [[3,4], [2,3,5]] 

        #设置随机迭代次数
        ntrials = 100
        
        #设置测量次数,即真实芯片或者噪声虚拟机shots数值
        shots = 2000
        qv_result = calculate_quantum_volume(qvm, qubit_lists, ntrials, shots)
        print("Quantum Volume : ", qv_result)
        qvm.finalize()


运行结果：

::

    Quantum Volume ： 8


参考文献
----

::

    [1] Andrew W. Cross, Lev S. Bishop, Sarah Sheldon, Paul D. Nation, and Jay M. Gambetta, Validating quantum computers using randomized model circuits, Phys. Rev. A 100, 032328 (2019). https://arxiv.org/pdf/1811.12926
