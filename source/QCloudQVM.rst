本源高性能计算集群云服务
=================================
----

本源量子的高性能计算集群提供多种功能强大的虚拟机计算后端，适用于不同情况下的量子线路模拟需求，完整示例程序介绍如下：

    .. code-block:: python

        from pyqpanda import *
        import numpy as np

        # 通过QCloud()创建量子云虚拟机
        QCM = QCloud()

        # 通过传入当前用户的token来初始化
        QCM.init_qvm("3B1AC640AAC248C6A7EE4E8D8537370D")

        qlist = QCM.qAlloc_many(6)
        clist = QCM.cAlloc_many(6)

        # 构建量子程序，可以手动输入，也可以来自OriginIR或QASM语法文件等
        measure_prog = QProg()
        measure_prog << hadamard_circuit(qlist)\
                     << CZ(qlist[1], qlist[5])\
                     << Measure(qlist[0], clist[0])\
                     << Measure(qlist[1], clist[1])

        pmeasure_prog = QProg()
        pmeasure_prog << hadamard_circuit(qlist)\
                      << CZ(qlist[1], qlist[5])\
                      << RX(qlist[2], np.pi / 4)\
                      << RX(qlist[1], np.pi / 4)\

        # 调用全振幅蒙特卡洛测量操作计算接口，需要量子程序和测量次数两个参数
        result = QCM.full_amplitude_measure(measure_prog, 1000)
        print(result)

全振幅模拟云计算
>>>>>>>>>>>>>>>>>>

    接口介绍如下：

    - ``full_amplitude_measure(全振幅蒙特卡洛测量操作)`` ：

        .. code-block:: python

            result0 = QCM.full_amplitude_measure(measure_prog, 100)
            print(result0)
        
        需要传入的第二个参数是测量次数，输出结果如下,左侧是量子态的二进制表示，右边表示测量次数对应的概率：
        
        .. code-block:: python

            {'00': 0.263, 
             '01': 0.255, 
             '10': 0.241, 
             '11': 0.241}

    - ``full_amplitude_pmeasure(全振幅概率测量操作)`` ：

        .. code-block:: python

            result1 = QCM.full_amplitude_pmeasure(pmeasure_prog, [0, 1, 2])
            print(result1)
        
        需要传入的第二个参数是测量的比特，输出结果如下,左侧是量子态的二进制表示，右边表示测量对应的概率：
        
        .. code-block:: python

            {'000': 0.12499999999999988, 
             '001': 0.12499999999999988, 
             '010': 0.12499999999999988, 
             '011': 0.12499999999999988, 
             '100': 0.12499999999999988, 
             '101': 0.12499999999999988, 
             '110': 0.12499999999999988, 
             '111': 0.12499999999999988}

部分振幅模拟云计算
>>>>>>>>>>>>>>>>>>

    - ``partial_amplitude_pmeasure(部分振幅概率测量操作)`` ：

        .. code-block:: python

            result2 = QCM.partial_amplitude_pmeasure(pmeasure_prog, ["0", "1", "2"])
            print(result2)
        
        需要传入的第二个参数是测量的量子态振幅的十进制表示，输出结果如下,左侧是量子态振幅的十进制表示，右边表示复数形式的振幅值：
        
        .. code-block:: python

            {'0': (0.08838832192122936-0.08838833495974541j), 
             '1': (0.08838832192122936-0.08838833495974541j), 
             '2': (0.08838832192122936-0.08838833495974541j)} 

单振幅云计算
>>>>>>>>>>>>>>>>>>

    - ``single_amplitude_pmeasure(单振幅概率测量操作)`` ：

        .. code-block:: python

            result3 = QCM.single_amplitude_pmeasure(pmeasure_prog, "0")
            print(result3)
        
        需要传入的第二个参数是测量的振幅（十进制表示），输出结果如下,只会输出一个量子态对应的复数形式的振幅值：
        
        .. code-block:: python

            (0.08838833056846361-0.08838833850593952j)

噪声模拟云计算
>>>>>>>>>>>>>>>>>>

    - ``noise_measure(噪声虚拟机测量操作)`` ：

        .. code-block:: python

            QCM.set_noise_model(NoiseModel.BIT_PHASE_FLIP_OPRATOR, [0.01], [0.02])
            result4 = QCM.noise_measure(measure_prog, 100)
            print(result4)
        
        通过 ``set_noise_model`` 设置噪声参数，第一个参数是噪声模型，后面分别是单门噪声参数和双门噪声参数，噪声模型的定义如下：

        .. code-block:: c

            enum NOISE_MODEL
            {
                DAMPING_KRAUS_OPERATOR,
                DEPHASING_KRAUS_OPERATOR,
                DECOHERENCE_KRAUS_OPERATOR_P1_P2,
                BITFLIP_KRAUS_OPERATOR,
                DEPOLARIZING_KRAUS_OPERATOR,
                BIT_PHASE_FLIP_OPRATOR,
                PHASE_DAMPING_OPRATOR,
                DECOHERENCE_KRAUS_OPERATOR,
                PAULI_KRAUS_MAP,
                KRAUS_MATRIX_OPRATOR,
                MIXED_UNITARY_OPRATOR,
            };

        可以通过pyqpanda的枚举类 ``NoiseModel`` 来获取，该接口输出结果如下,左侧是量子态的二进制表示，右边表示测量对应的概率：
        
        .. code-block:: python

            {'00': 0.27, 
             '01': 0.22, 
             '10': 0.21, 
             '11': 0.30}


