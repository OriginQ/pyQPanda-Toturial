量子云虚拟机
=====================

在复杂的量子线路模拟中有必要借助于高性能计算机集群或真实的量子计算机，用云计算的方式替代本地计算，在一定程度上减轻用户的计算成本，获得更好的计算体验。

量子云虚拟机基于量子云平台，用户通过量子云平台经由调度服务器向部署在远程的量子计算机或计算集群提交任务，并接收返回的结果，流程如下图所示。

.. image:: images/qcloud.gif
   :align: center  

pyqpanda封装了量子云虚拟机，可以向本源量子的计算服务器集群或量子真实芯片发送计算指令，并获取计算结果。
 
首先通过 ``QCloud()`` 构建量子云虚拟机对象，然后用 ``init_qvm`` 初始化系统资源
 
        .. code-block:: python
 
            from pyqpanda import *
            PI = 3.141593
            
            QCM = QCloud()
            QCM.init_qvm("3B1AC640AAC248C6A7EE4E8D8537370D")

        ``init_qvm`` 需要用户传入量子云平台用户验证标识token，可以从本源量子云平台个人信息下获取。接着构建量子程序，可以手动输入，也可以来自OriginIR或QASM语法文件等

        .. code-block:: python

            qlist = QCM.qAlloc_many(6)
            clist = QCM.cAlloc_many(6)

            measure_prog = QProg()
            measure_prog.insert(hadamard_circuit(qlist))\
                        .insert(CZ(qlist[1], qlist[5]))\
                        .insert(CZ(qlist[0], qlist[4]))\
                        .insert(RX(qlist[2], PI / 4))\
                        .insert(RX(qlist[1], PI / 4))\
                        .insert(CZ(qlist[2], qlist[3]))\
                        .insert(Measure(qlist[0], clist[0]))\
                        .insert(Measure(qlist[1], clist[1]))\
                        .insert(Measure(qlist[2], clist[2]))

            pmeasure_prog = QProg()
            pmeasure_prog.insert(hadamard_circuit(qlist))\
                         .insert(CZ(qlist[1], qlist[5]))\
                         .insert(RX(qlist[2], PI / 4))\
                         .insert(RX(qlist[1], PI / 4))\

            result = QCM.full_amplitude_measure(measure_prog, 100)
            QCM.finalize()

        核心过程是提交计算接口，量子云虚拟机有多种计算后端，目前支持以下6种方式：

        - ``1.full_amplitude_measure(全振幅蒙特卡洛测量操作)`` ：

                .. code-block:: python

                    result0 = QCM.full_amplitude_measure(measure_prog, 100)
                    print(result0)
                
                需要传入的第二个参数是测量次数，输出结果如下,左侧是量子态的二进制表示，右边表示测量次数对应的概率：
                
                .. code-block:: python

                    {'000': 0.15, 
                     '001': 0.08, 
                     '010': 0.13, 
                     '011': 0.11, 
                     '100': 0.11, 
                     '101': 0.18, 
                     '110': 0.13, 
                     '111': 0.11}

        - ``2.full_amplitude_pmeasure(全振幅概率测量操作)`` ：

                .. code-block:: python

                    result1 = QCM.full_amplitude_pmeasure(pmeasure_prog, [0, 1, 2])
                    print(result1)
                
                需要传入的第二个参数是测量的比特，输出结果如下,左侧是量子态的二进制表示，右边表示测量对应的概率：
                
                .. code-block:: python

                    {'000': 0.125, 
                     '001': 0.125, 
                     '010': 0.125, 
                     '011': 0.125, 
                     '100': 0.125,
                     '110': 0.125, 
                     '111': 0.125}

        - ``3.partial_amplitude_pmeasure(部分振幅概率测量操作)`` ：

                .. code-block:: python

                    result2 = QCM.partial_amplitude_pmeasure(pmeasure_prog, ["0", "1", "2"])
                    print(result2)
                
                需要传入的第二个参数是测量的量子态振幅的十进制表示，输出结果如下,左侧是量子态振幅的十进制表示，右边表示复数形式的振幅值：
                
                .. code-block:: python

                    {'0': (0.08838832192122936-0.08838833495974541j), 
                     '1': (0.08838832192122936-0.08838833495974541j), 
                     '2': (0.08838832192122936-0.08838833495974541j } 

        - ``4.single_amplitude_pmeasure(单振幅概率测量操作)`` ：

                .. code-block:: python

                    result3 = QCM.single_amplitude_pmeasure(pmeasure_prog, "0")
                    print(result3)
                
                需要传入的第二个参数是测量的振幅（十进制表示），输出结果如下,只会输出一个量子态对应的复数形式的振幅值：
                
                .. code-block:: python

                    (0.08838833056846361-0.08838833850593952j)

        - ``5.noise_measure(噪声虚拟机测量操作)`` ：

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

                    {'000': 0.12, 
                     '001': 0.20, 
                     '010': 0.06, 
                     '011': 0.12, 
                     '100': 0.13, 
                     '101': 0.10, 
                     '110': 0.12, 
                     '111': 0.15}

        - ``6.full_amplitude_measure(本源悟源真实芯片测量操作)`` ：

                .. code-block:: python

                    result5 = QCM.real_chip_measure(measure_prog, 100)
                    print(result5)
                
                输出结果如下,左侧是量子态的二进制表示，右边表示测量次数对应的概率：
                
                .. code-block:: python

                    {'000': 0.125690974898748, 
                     '001': 0.1376474724775309, 
                     '010': 0.08622495923853496, 
                     '011': 0.21313000364370588, 
                     '100': 0.11617781984817964, 
                     '101': 0.14758585390966736, 
                     '110': 0.11815719064612076, 
                     '111': 0.055385725337512515}

        .. note:: 
            - 使用对应的计算接口时，需要确认当前用户已经开通了该产品，否则可能会导致提交计算任务失败。
            - 在噪声模拟时，退相干的单门噪声和双门参数参数分别有3个，不同于其他噪声
            - 量子云虚拟机目前使用的真实芯片是本源悟源，仅支持6比特量子线路模拟，未来会加入其他的量子芯片，敬请期待。
