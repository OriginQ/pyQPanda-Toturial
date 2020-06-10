量子程序匹配拓扑结构
=====================

量子计算设备存在量子比特之间的有限连接，使得只能在有限的量子位对上应用两个量子位门。
量子程序应用到目标设备时，必须转换原始的量子程序以适应硬件限制，让双量子比特门中的两个量子比特能够满足物理拓扑结构，从而让双量子位门正常作用；
当前解决方案中多数需要在无法相互作用的两个量子比特间插入额外的SWAP操作，以便将逻辑量子位“移动”到它们可以相互作用的位置。
我们称这种解决方法为量子程序匹配拓扑结构。


接口说明
---------------

当前版本中存在两种思路的匹配拓扑方法：

- 接口  ``topology_match``
   通过采用线路分层以及A*搜索算法，在匹配过程中，让插入的SWAP操作个数近似达到最少，使得算法的整体近似消耗达到最少。
   该接口需要传入5个参数，其中分别为 构建的量子程序、使用的量子比特位集合、初始化的虚拟机指针、使用的SWAP操作的方式、拓扑结构的类型；
   并且返回映射后的量子程序

- 接口  ``qcodar_match``
   通过采用一种上下文敏感和持续时间感知的重映射算法，该算法能够感知门持续时间差和程序上下文，使得它能够从程序中提取更多的并行性，
   在不同体系结构的模拟中平均将量子程序的速度提高1.23。并在原始量子噪声模拟器上运行时保持电路的保真度。
   该接口需要传入7个参数，其中分别为 构建的量子程序、使用的量子比特位集合、初始化的虚拟机指针、拓扑结构的类型、拓扑结构的宽度、拓扑结构的长度、匹配拓扑运行的次数；
   并且返回映射后的量子程序

实例
---------------

``topology_match`` 实例
>>>>>>>>>>>>>>>>>>>>>>>>>

.. code-block:: python

    from pyqpanda import *

    if __name__=="__main__":
        qvm = CPUQVM()
        qvm.init_qvm()

        qv = qvm.qAlloc_many(16)
        c = qvm.cAlloc_many(16)
        src_prog = QProg()

        # 构建量子程序
        src_prog.insert(CNOT(qv[0], qv[3])) \
            .insert(CNOT(qv[0], qv[2])) \
            .insert(CNOT(qv[1], qv[3])) \
            .insert(CZ(qv[1], qv[2])) \
            .insert(CZ(qv[0], qv[2])) \
            .insert(T(qv[1])).insert(S(qv[2])).insert(H(qv[3]))

        # 对src_prog进行概率测量，得到结果results_1
        qvm.directly_run(src_prog)
        results_1 = qvm.pmeasure_no_index(qv)
        
        # 对src_prog进行拓扑匹配，得到匹配IBM_QX5_ARCH拓扑结构的量子程序out_prog
        out_prog, out_qv = topology_match(src_prog, qv, qvm, CNOT_GATE_METHOD, IBM_QX5_ARCH)

        # 对out_prog进行概率测量，得到结果results_2
        qvm.directly_run(out_prog)
        results_2 = qvm.pmeasure_no_index(out_qv)
        
        # 对比概率测量结果results_1和results_2, 打印相同结果
        len = min(len(results_1), len(results_2))
        for index in range(len):
            if abs(results_1[index] - results_2[index]) < 1.0e-6 :
                print(results_1[index])
            else:
                print("The results are different")

        destroy_quantum_machine(qvm)

具体步骤如下:

 - 首先创建量子虚拟机、量子寄存器、经典寄存器
 
 - 编写量子程序 ``src_prog`` ，对该量子程序进行概率测量得到结果 ``results_1``
 
 - 接着调用 ``topology_match()`` 对 ``src_prog`` 进行符合特定物理结构的线路映射，得到适配特定物理结构的量子程序 ``out_prog``

 - 对量子程序 ``out_prog`` 进行概率测量得到结果 ``results_2``
 
 - 由于量子程序映射只是对原线路增加额外的 ``SWAP`` 操作，以适配物理拓扑结构，并不影响线路的结构。所以对比结果 ``results_1`` 和 ``results_2`` ，如果结果一致，则线路映射正确。


运行结果如下:

.. code-block:: c

    0.4999999701976776
    0.0
    0.0
    0.0
    0.0
    0.0
    0.0
    0.0
    0.4999999701976776
    0.0
    0.0
    0.0
    0.0
    0.0
    0.0
    0.0

``qcodar_match`` 实例
>>>>>>>>>>>>>>>>>>>>>>>>>

.. code-block:: python

    from pyqpanda import *
    PI = 3.1415926

    if __name__=="__main__":
        qvm = CPUQVM()
        qvm.init_qvm()

        qv = qvm.qAlloc_many(4)
        cv = qvm.cAlloc_many(4)
        src_prog = QProg()

        # 构建量子程序
        src_prog.insert(CNOT(qv[1], qv[3])) \
            .insert(RX(qv[0], PI / 2)) \
            .insert(CNOT(qv[0], qv[2])) \
            .insert(RY(qv[1], -PI / 4)) \
            .insert(CNOT(qv[2], qv[0])) \
            .insert(CZ(qv[1], qv[2])) \
            .insert(CNOT(qv[1], qv[3])) \
            .insert(RZ(qv[2], PI / 6)) \
            .insert(CNOT(qv[2], qv[0])) \
            .insert(RZ(qv[0], -PI / 4)) \
            .insert(CNOT(qv[0], qv[2])) \
            .insert(H(qv[0]))\
            .insert(T(qv[1])) \
            .insert(RX(qv[1], -PI/4)) \
            .insert(Y(qv[2])) \
            .insert(Z(qv[1]))

        # 对src_prog进行概率测量，得到结果results_1
        qvm.directly_run(src_prog)
        results_1 = qvm.pmeasure_no_index(qv)
        
        # 对src_prog进行拓扑匹配，得到匹配IBM_QX5_ARCH拓扑结构的量子程序out_prog
        out_prog, out_qv = qcodar_match(src_prog, qv, qvm, SIMPLE_TYPE, 2, 3, 5 )

        # 对out_prog进行概率测量，得到结果results_2
        qvm.directly_run(out_prog)
        results_2 = qvm.pmeasure_no_index(out_qv)
        
        # 对比概率测量结果results_1和results_2, 打印相同结果
        len = min(len(results_1), len(results_2))
        for index in range(len):
            if abs(results_1[index] - results_2[index]) < 1.0e-6 :
                print(results_1[index])
            else:
                print("The results are different")

        destroy_quantum_machine(qvm)

具体步骤如下:

 - 首先创建量子虚拟机、量子寄存器、经典寄存器
 
 - 编写量子程序 ``src_prog`` ，对该量子程序进行概率测量得到结果 ``results_1``
 
 - 接着调用 ``qcodar_match()`` 对 ``src_prog`` 进行符合特定物理结构的线路映射，得到适配特定物理结构的量子程序 ``out_prog``

 - 对量子程序 ``out_prog`` 进行概率测量得到结果 ``results_2``
 
 - 由于量子程序映射只是对原线路增加额外的 ``SWAP`` 操作，以适配物理拓扑结构，并不影响线路的结构。所以对比结果 ``results_1`` 和 ``results_2`` ，如果结果一致，则线路映射正确。


运行结果如下：

.. code-block:: c

    0.0
    0.0
    0.0
    0.0
    0.2699950337409973
    0.4585585296154022
    0.04632381722331047
    0.07867620140314102
    0.0
    0.0
    0.0
    0.0
    0.013498696498572826
    0.007947907783091068
    0.07867618650197983
    0.046323806047439575