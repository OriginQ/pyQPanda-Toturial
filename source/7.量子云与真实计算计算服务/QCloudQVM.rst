高性能计算集群云服务
=================================

当涉及到处理复杂的量子计算和模拟任务时，高性能计算集群成为了不可或缺的工具。

与个人电脑的单进程计算方式不同，高性能计算集群采用分布式计算算法，意味着计算任务可以被分解成多个子任务，并在集群中的多个计算节点上并行执行，从而大大提升了计算效率和速度。这对于处理复杂的量子计算任务尤为重要，因为量子线路模拟往往涉及大量的计算和存储需求。通过分布式计算，我们能够将这些庞大的计算任务分解成更小的部分，在多个节点上同时进行处理，从而显著缩短了计算时间。

本源量子的高性能计算集群提供多种功能强大的虚拟机计算后端，针对不同的量子计算模型和算法进行了优化，适用于不同情况下的量子线路模拟需求，我们引入 ``QCloud`` 来提交任务和查询计算计算结果。

.. class:: QCloud(QuantumMachine)

    量子云计算集群任务管理类，用于管理集群计算，提交任务并获取结果。

    :param None: 无参数。
    :type None: None

    .. method:: __init__()

        创建一个 Quantum Cloud 虚拟机实例。

        :return: 无返回值。
        :rtype: None

    .. method:: full_amplitude_measure(prog, shot, task_name='QPanda Experiment')

        对给定量子线路执行全振幅采样测量，返回测量结果的概率分布。

        :param prog: 要执行的量子线路。
        :type prog: QProg
        :param shot: 测量的次数。
        :type shot: int
        :param task_name: 任务名称，默认为 'QPanda Experiment'。
        :type task_name: str, optional
        :return: 各测量结果的概率分布。
        :rtype: Dict[str, float]

    .. method:: full_amplitude_pmeasure(prog, qvec, task_name='QPanda Experiment')

        对给定量子线路执行全振幅概率测量，测量结果只考虑指定的测量比特，返回测量结果的概率分布。

        :param prog: 要执行的量子线路。
        :type prog: QProg
        :param qvec: 指定的测量比特列表。
        :type qvec: List[int]
        :param task_name: 任务名称，默认为 'QPanda Experiment'。
        :type task_name: str, optional
        :return: 各测量结果的概率分布。
        :rtype: Dict[str, float]

    .. method:: get_expectation(prog, hamiltonian, qvec, task_name='QPanda Experiment')

        该方法在给定的量子线路下，根据指定的哈密顿量，计算量子态的期望值。

        :param prog: 要执行的量子线路。
        :type prog: QProg
        :param hamiltonian: 哈密顿量的项和系数组成的列表。
        :type hamiltonian: List[Tuple[Dict[int, str], float]]
        :param qvec: 用于计算期望值的量子比特列表。
        :type qvec: QVec
        :param task_name: 任务名称，默认为 'QPanda Experiment'。
        :type task_name: str, optional
        :return: 计算得到的期望值。
        :rtype: float

    .. method:: init_qvm(token: str, is_logged: bool = False, use_bin_or_hex: bool = True, enable_pqc_encryption = False, request_time_out: int = 100)

        该方法用于初始化 QVM 服务，提供必要的用户身份验证令牌和其他参数。可选参数用于配置 QVM 的行为，例如是否记录操作，以及在处理二进制和十六进制字符串时是否使用默认设置。

        :param token: 用户身份验证令牌。
        :type token: str
        :param is_logged: 是否在控制台上记录 QVM 操作（默认为 False）。
        :type is_logged: bool, optional
        :param use_bin_or_hex: 是否在处理二进制和十六进制字符串时使用默认设置（默认为 True）。
        :type use_bin_or_hex: bool, optional
        :param enable_pqc_encryption: 是否启用混合加密算法对数据传输进行加密（默认为 False）
        :type use_bin_or_hex: bool, optional
        :param request_time_out: 请求超时时间，以秒为单位（默认为 100）。
        :type request_time_out: int, optional

    .. method:: noise_measure(prog, shot, task_name='QPanda Experiment')

        对给定量子线路执行带噪声的测量，返回测量结果的概率分布，需要提前设置噪声模型和参数

        :param prog: 要执行的量子线路。
        :type prog: QProg
        :param shot: 测量的次数。
        :type shot: int
        :param task_name: 任务名称，默认为 'QPanda Experiment'。
        :type task_name: str, optional
        :return: 各测量结果的概率分布。
        :rtype: Dict[str, float]

    .. method:: partial_amplitude_pmeasure(prog, amp_vec, task_name='QPanda Experiment')

        对给定量子线路执行部分振幅测量，返回测量结果的概率幅值分布。

        :param prog: 要执行的量子线路。
        :type prog: QProg
        :param amp_vec: 部分振幅测量的振幅向量。
        :type amp_vec: List[str]
        :param task_name: 任务名称，默认为 'QPanda Experiment'。
        :type task_name: str, optional
        :return: 各测量结果的概率幅值分布。
        :rtype: Dict[str, complex]

    .. method:: set_noise_model(arg0, arg1, arg2)

        该方法用于设置量子虚拟机的噪声模型，包括噪声模型本身和相关的噪声参数。

        :param arg0: 噪声模型。
        :type arg0: NoiseModel
        :param arg1: 噪声参数列表。
        :type arg1: List[float]
        :param arg2: 噪声参数列表。
        :type arg2: List[float]
        :return: 无返回值。
        :rtype: None

    .. method:: single_amplitude_pmeasure(prog, amplitude, task_name='QPanda Experiment')

        对给定量子线路执行单振幅测量，返回测量结果的概率幅值。

        :param prog: 要执行的量子线路。
        :type prog: QProg
        :param amplitude: 单振幅测量的振幅。
        :type amplitude: str
        :param task_name: 任务名称，默认为 'QPanda Experiment'。
        :type task_name: str, optional
        :return: 测量结果的概率幅值。
        :rtype: complex

    我们以简单的量子线路为例，导入必要的库，然后是初始化和设置用户信息过程，用户可以在本源量子云官网 QCloud_免费注册获取用户标识符,参考 :ref:`真实芯片计算服务` 章节内容

    .. code-block:: python

        from pyqpanda import *
        import numpy as np

        # 通过QCloud()创建量子云虚拟机
        QCM = QCloud()

        # 通过传入当前用户的token来初始化
        QCM.init_qvm("608e020100301006072a8648ce3d020106052b8104001c041730150201010410634a5b6d0a2a9a2b03b9d7c17c57405f/13082")

    然后是构建量子线路，对于需要采样测量的量子线路需要插入测量节点

    .. code-block:: python

        qlist = QCM.qAlloc_many(6)
        clist = QCM.cAlloc_many(6)

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

    接下来就是提交计算任务和获取结果：

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

    - ``partial_amplitude_pmeasure(部分振幅概率测量操作)`` ：

        .. code-block:: python

            result2 = QCM.partial_amplitude_pmeasure(pmeasure_prog, ["0", "1", "2"])
            print(result2)
        
        需要传入的第二个参数是测量的量子态振幅的十进制表示，输出结果如下,左侧是量子态振幅的十进制表示，右边表示复数形式的振幅值：
        
        .. code-block:: python

            {'0': (0.08838832192122936-0.08838833495974541j), 
             '1': (0.08838832192122936-0.08838833495974541j), 
             '2': (0.08838832192122936-0.08838833495974541j)} 

    - ``single_amplitude_pmeasure(单振幅概率测量操作)`` ：

        .. code-block:: python

            result3 = QCM.single_amplitude_pmeasure(pmeasure_prog, "0")
            print(result3)
        
        需要传入的第二个参数是测量的振幅（十进制表示），输出结果如下,只会输出一个量子态对应的复数形式的振幅值：
        
        .. code-block:: python

            (0.08838833056846361-0.08838833850593952j)

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


