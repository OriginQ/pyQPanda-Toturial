
交叉熵基准
==========================

简介
--------------
交叉熵基准测试（xeb）[1]是一种通过应用随机电路并测量观察到的位串测量值与从模拟获得的这些位串的预期概率之间的交叉熵来评估门性能的方法。

原理
--------------
XEB 实验收集了执行随机电路时受到噪声影响的数据。应用带有单元 U 的随机电路的效果被模拟为去极化通道。其结果是，初始状态 :math:`\left|\psi\right\rangle` 映射到密度矩阵 :math:`\rho_U` 如下

.. math::
    \begin{aligned}
        \left|\psi\right\rangle \to \rho_U = f \left|\psi_U\right\rangle \left\langle\psi_U\right| + (1 - f) I / D
    \end{aligned}

其中， :math:`\left|\psi_U\right\rangle = U\left|\psi\right\rangle` ,  :math:`D` 是希尔伯特空间的维度， :math:`I/D` 是最大混合状态， :math:`f` 是电路应用的保真度。
要使这一模型准确无误，我们需要一个 :math:`U` 能扰乱错误的随机电路。在实践中，我们使用了一种特殊的电路范式，由随机单量子比特旋转与纠缠门交错组成。
这里引入能表示所有概率之和的观测值 :math:`O_U` ，例如: :math:`O_U|x\rangle = p(x)|s\rangle` ，对于任意的位字符串 :math:`x` ，我们可以根据如下公式及进行推导：

.. math::
    \begin{aligned}
        e_U &= \langle \psi_U|O_U|\psi_U\rangle \\
            &= \sum_{x} a^{*}_x \langle x |O_U|x\rangle a_x \\
            &= \sum_{x} a^{*}_x p(x) \langle x|O_U|x \rangle \\
            &= \sum_{x} a^{*}_x p(x)p(x)
    \end{aligned}

其中 :math:`e_U` 是理想概率的平方和。 :math:`u_U` 是一个只取决于算子的归一化因子。由于该算子的定义中包含了真实概率，因此在这里会显示出来。

.. math::
    \begin{aligned}
        u_U &= Tr[O_U / D ] \\
            &= 1/D \sum_{x}  \langle x |O_U|x\rangle \\
            &= 1/D \sum_{x}  p(x)
    \end{aligned}

假设观测值 :math:`O_U` 在计算基础中是对角线。则 :math:`O_U` 在 :math:`\rho_U` 上的期望值为

.. math::
    \begin{aligned}
        Tr(\rho_U O_U) = f\langle\psi_U|O_U|\psi_U\rangle + (1-f)Tr(O_U/D)
    \end{aligned}

这个等式说明了 :math:`f` 的估算方式，因为 :math:`Tr(\rho_U O_U)` 可以根据实验数据估算，并且 :math:`\langle\psi_U|O_U|\psi_U\rangle 和 Tr(O_U/D)` 可以通过计算求出。
让 :math:`e_U = \langle\psi_U|O_U|\psi_U\rangle, u_U = Tr(O_U/D)` , 定义 :math:`m_U为Tr(\rho_U O_U)` 的实验估计值。上述的表达式可以转化为以下的线性方程。

.. math::
    
    \begin{aligned}
        & m_U=f e_U+(1-f) u_U \\
        & m_U-u_U=f\left(e_U-u_U\right)
    \end{aligned}


核心思想
--------------
交叉熵基准测试的核心思想是比较量子计算机在理论预期和实际运行中的行为之间的差异。具体而言，通过在理论上准备一系列特定的量子态并在量子计算机上执行相应的门操作，然后测量产生的量子态与预期状态之间的交叉熵，可以得出量子计算机的性能评估结果。交叉熵是一种在信息论中常用的度量，用于衡量两个概率分布之间的差异。

接口说明
--------------

.. function:: double_gate_xeb(config: QCloudTaskConfig, qubit0: int, qubit1: int, clifford_range: List[int], num_circuits: int, gate_type: GateType = GateType.CZ_GATE) -> Dict[int,float]

    此函数用于执行双比特交叉熵基准（Double Gate XEB）实验。
    
    :param config: QCloudTaskConfig 对象，表示云量子任务的配置。
    :type config: QCloudTaskConfig
    :param qubit0: 双比特门的第一个量子比特索引。
    :type qubit0: int
    :param qubit1: 双比特门的第二个量子比特索引。
    :type qubit1: int
    :param clifford_range: 包含 Clifford 门的序列长度范围的列表，用于指定不同长度的 Clifford 门序列。
    :type clifford_range: List[int]
    :param num_circuits: 要执行的电路数量。
    :type num_circuits: int
    :param gate_type: 双比特门类型，默认为 CZ_GATE。
    :type gate_type: GateType, optional
    :return: 包含双比特门交叉熵基准实验结果的字典，其中键是 Clifford 门序列长度，值是误差概率。
    :rtype: Dict[int,float]
    :raises run_fail: 执行双比特门交叉熵基准实验失败。

实例
--------------
.. code-block:: python

    from pyqpanda import *

    if __name__=="__main__":

        # 设置不同层数组合
        range = [2,4,6,8,10]
        # 现在可测试双门类型主要为 CZ CNOT SWAP ISWAP SQISWAP

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

        res = double_gate_xeb(config, 0, 1, range, 20, GateType.CZ_GATE)
        # 对应的数值随噪声影响，噪声数值越大，所得结果越小，且层数增多，结果数值越小。

参考文献
----

::

    [1] Boixo, S., Isakov, S.V., Smelyanskiy, V.N. et al. Characterizing quantum supremacy in near-term devices. Nature Phys 14, 595–600 (2018). https://doi.org/10.1038/s41567-018-0124-x   