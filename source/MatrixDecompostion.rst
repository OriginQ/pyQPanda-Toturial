酉矩阵分解
=====================
目前，量子计算的算法通常用量子线路表示，量子线路包括量子逻辑门操作。
通常，连续的一段量子线路通常包含几十上百个甚至成千上万个量子逻辑门操作，而量子逻辑门数量或单个量子逻辑门操作的量子比特数越多，计算过程越为复杂，导致量子线路的模拟效率较低，且对硬件资源的占用较多。

算法目标
>>>>>>>>>>
----

对于上述问题，有必要对量子线路进行一种等价转换，需要减少量子线路中逻辑门的数量，
同时在此基础上，需要确保转换前后整个量子线路对应的酉矩阵完全相同.

算法概述
>>>>>>>>>>
----

本文介绍的算法是将一个N阶酉矩阵，分解成不超过r = N(N−1)/2个带有少量控制的单量子逻辑门序列，其中N=2^n，分解的产物满足如下等式关系

.. centered:: :math:`U_rU_{r-1}···U_3U_2U_1U=I_N`

从而可以得到原矩阵U的分解结果表示

.. centered:: :math:`U=U_1^{\dagger}U_2^{\dagger}U_3^{\dagger}···U_{r-1}^{\dagger}U_r^{\dagger}`

使用介绍
>>>>>>>>>>>>>>>>
----

pyqpanda中设计了 ``matrix_decompose`` 接口用于进行酉矩阵分解，该接口需要两个参数，
第一个是使用到的所有量子比特，第二个是待分解的酉矩阵，该函数的输出是转换后的量子线路。

实例
>>>>>>>>>>
----

.. _酉矩阵分解示例程序:
以下示例展示了部分振幅量子虚拟机接口的使用方式

    .. code-block:: python
  
        import pyqpanda as pq
        import numpy as np

        if __name__=="__main__":

            machine = pq.init_quantum_machine(pq.QMachineType.CPU)
            q = machine.qAlloc_many(2)
            c = machine.cAlloc_many(2)

            source_matrix = [(0.974545+0.002125j),  (-0.012681-0.128788j), (-0.015742-0.128335j), (-0.020006-0.128030j),
                            (-0.012681-0.128788j), (0.980870-0.129132j),  (-0.012099+0.001730j), (-0.016949-0.063521j),
                            (-0.015742-0.128335j), (-0.012099+0.001730j), (0.976706-0.128312j),  (-0.023108-0.110363j),
                            (-0.020006-0.128030j), (-0.016949-0.063521j), (-0.023108-0.110363j), (0.974615-0.127660j)]

            print("source matrix : ")
            print(source_matrix)

            out_cir = pq.matrix_decompose(q, source_matrix)
            circuit_matrix = pq.get_matrix(out_cir)

            print("the decomposed matrix : ")
            print(circuit_matrix)

            source_matrix = np.round(np.array(source_matrix),3)
            circuit_matrix = np.round(np.array(circuit_matrix),3)

            if np.all(source_matrix == circuit_matrix):
                print('matrix decompose ok !')
            else:
                print('matrix decompose false !')


上述实例运行的结果如下：

    .. code-block:: python

        source matrix :
        [(0.974545+0.002125j),  (-0.012681-0.128788j), (-0.015742-0.128335j), (-0.020006-0.12803j), 
         (-0.012681-0.128788j), (0.98087-0.129132j),   (-0.012099+0.00173j),  (-0.016949-0.063521j), 
         (-0.015742-0.128335j), (-0.012099+0.00173j),  (0.976706-0.128312j),  (-0.023108-0.110363j), 
         (-0.020006-0.12803j),  (-0.016949-0.063521j), (-0.023108-0.110363j), (0.974615-0.12766j)]

        the decomposed matrix :
        [(0.974545419216156+0.00212500081397593j),    (-0.012681466527283192-0.12878791987895966j), (-0.015742329880595207-0.12833496928215027j),   (-0.020006246864795685-0.12803010642528534j),   
         (-0.012681004591286182-0.1287880390882492j), (0.9808700680732727-0.12913194298744202j),    (-0.012098574079573154+0.0017299940809607506j), (-0.01694825477898121-0.06352110952138901j), 
         (-0.01574200578033924-0.12833505868911743j), (-0.01209898293018341+0.0017300674226135015j),(0.9767062664031982-0.12831196188926697j),      (-0.02310757525265217-0.11036307364702225j), 
         (-0.020006004720926285-0.12803006172180176j),(-0.01694897934794426-0.06352093815803528j),  (-0.02310837060213089-0.11036311835050583j),    (0.9746155142784119-0.1276601254940033j)]
        
        matrix decompose ok !

从输出的结果可以看出，分解前后的矩阵完全相同，对于一个量子比特数目确定的量子系统，
即使分解前的量子线路含有成千上万个量子逻辑门，该接口可以将分解后的量子线路复杂度控制在合理范围之内，
完全不受到分解前量子线路复杂度的影响，

    .. note::

        1. 该接口的输入参数必须为酉矩阵。
        2. 通过将分解的结果数量约束在一个限定范围内，有效减少了量子线路中的量子逻辑门数量，极大地提升了量子算法的模拟效率
        3. 示例程序中， ``get_matrix`` 接口用于获取一个量子线路对应的矩阵