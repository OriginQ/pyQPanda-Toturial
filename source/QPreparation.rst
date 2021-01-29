试验态制备与量子纠缠
####
----

试验态制备
****

试验态制备，指的是量子计算中任意算法的初始量子态的构造，是量子计算的初始步骤。

以单比特的两态空间为例，在实际量子运算中，我们可以直接得到的默认量子态是基态 :math:`\left|0\right\rangle`，\
通过非门可以间接得到基态 :math:`\left|1\right\rangle`。

对于任给的目标叠加量子态，我们则需要构造相应的量子门组合来得到。从基态 :math:`\left|0\right\rangle` 出\
发制备任给目标叠加态的过程称为初态制备。

最大叠加态
++++

以二比特态空间为例，从 :math:`\left|0\right\rangle^{\otimes2}` 出发，对每个量子比特进行Hadamard门操作\
可以得到二比特空间中所有基态的均匀叠加。

类似地，在任意维态空间中，均可以借助Hadamard门从多维的 :math:`\left|0\right\rangle` 基态出发，得到所有基态均匀线性组合的量子态。

这种量子态称为最大叠加态，很多量子计算中量子比特的初始状态要求为最大叠加态，量子计算的并行性也有赖于此。


通过试验态制备，我们就可以得到任意的基础量子态，从而完成量子计算中运算对象的构造。\
但是在执行运算操作之前，我们需要对量子计算所使用的量子比特给出明确的约束——纠缠关联。

在介绍量子纠缠之前，我们需要介绍一下纯态和混态。

非基态的量子态都为叠加态。叠加态又可以分为相干叠加和非相干叠加，分别称为纯态和混态。

纯态与混态的区分方式有多种，典型的有布洛赫球（Bloch Sphere），将态空间与Bloch球关联，球面上量子态为纯态，球体内的量子态为混态。

另一种重要的区分方式为密度矩阵，混态的密度矩阵非对角元均为0。

量子纠缠
****

如果一个量子系统的量子态 :math:`\left|\psi\right\rangle` 可以表示成形如 :math:`\left|\psi\right\rangle=\left|\psi_0\
\right\rangle\otimes\left|\psi_1\right\rangle` 的两个量子系统的直积形式，我们就将此量子态称为直积态。

.. note:: 不能进行这种直积分解的量子态就是纠缠态。

例如对二比特的Bell态 :math:`\frac{1}{\sqrt2}\left|00\right\rangle+\frac{1}{\sqrt2}\left|11\right\rangle`，它不能写成\
两个单比特量子态的直积形式。

量子纠缠态有超越经典关联的量子关联。为了发挥量子计算的并行性和高效性，量子计算使用的量子比特之间应当有着纠缠关联。


最大叠加态制备
****

下面是基于QPanda-2.0的最大叠加态制备的代码实现，调用的量子比特之间有着纠缠关联。


.. code-block:: python

    #!/usr/bin/env python

    import pyqpanda as pq

    if __name__ == "__main__":

        machine = pq.init_quantum_machine(pq.QMachineType.CPU)
        qubits = machine.qAlloc_many(3)
        prog = pq.create_empty_qprog()

        # 构建量子程序
        prog.insert(pq.H(qubits[0])) \
            .insert(pq.H(qubits[1])) \
            .insert(pq.H(qubits[2]))

        # 对量子程序进行概率测量
        result = pq.prob_run_dict(prog, qubits, -1)
        pq.destroy_quantum_machine(machine)

        # 打印测量结果
        for key in result:
            print(key+":"+str(result[key]))

运行结果应当是以均匀概率1/8得到3比特空间中所有量子态：

.. code-block:: python

    000, 0.125
    001, 0.125
    010, 0.125
    011, 0.125
    100, 0.125
    101, 0.125
    110, 0.125
    111, 0.125
        