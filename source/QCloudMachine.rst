量子云虚拟机
=====================
量子计算的模拟方法受限于机器的硬件水平，因此对于复杂的量子线路模拟有必要借助于高性能计算机集群，用云计算的方式替代本地计算，
从而一定程度上减轻了用户的计算成本，并帮助用户获得更好的计算体验。

pyQPanda封装了量子云虚拟机，可以向本源量子的计算服务器集群发送计算指令，同时根据生成的唯一任务标识进行计算结果的查询等操作。

首先通过 ``QCloud()`` 构建量子云虚拟机对象，然后用 ``init_qvm`` 初始化系统资源

        .. code-block:: python

            from pyqpanda import *
            import time

            PI = 3.141593
            
            QCM = QCloud()
            QCM.init_qvm("4B7AFE1E196A4197B7C6845C4E73EF2E")

 ``init_qvm`` 需要用户传入量子云平台用户验证标识token，可以从本源量子云平台个人信息下获取。接着构建量子程序

        .. code-block:: python

            qlist = QCM.qAlloc_many(10)
            clist = QCM.qAlloc_many(10)
            prog = QProg()
            for i in qlist:
            
            prog.insert(hadamard_circuit(qlist))\
                .insert(CZ(qlist[1], qlist[5]))\
                .insert(CZ(qlist[3], qlist[7]))\
                .insert(CZ(qlist[0], qlist[4]))\
                .insert(RZ(qlist[7], PI / 4))\
                .insert(RX(qlist[5], PI / 4))\
                .insert(RX(qlist[4], PI / 4))\
                .insert(RY(qlist[3], PI / 4))\
                .insert(CZ(qlist[2], qlist[6]))\
                .insert(RZ(qlist[3], PI / 4))\
                .insert(RZ(qlist[8], PI / 4))\
                .insert(CZ(qlist[9], qlist[5]))\
                .insert(RY(qlist[2], PI / 4))\
                .insert(RZ(qlist[9], PI / 4))\
                .insert(CZ(qlist[2], qlist[3]))\
                .insert(Measure(qlist[0], clist[0]))\
                .insert(Measure(qlist[1], clist[1]))\
                .insert(Measure(qlist[2], clist[2]))

量子云虚拟机有多种计算后端，主流的计算方法是 ``full_amplitude_measure(全振幅蒙特卡洛测量操作)`` 。

- ``full_amplitude_measure(QProg,shot)`` ：

        .. code-block:: python

            taskid = QCM.full_amplitude_measure(prog, 100)
        
        根据输出结果可以看到当前任务标识(TaskId)
        
        .. code-block:: python

            submit task 1337101012920d7beeeb122f2444c8537c97e28f64053 success

        利用 ``get_result`` 接口,通过传入TaskId和对应的虚拟机类型参数就可以对计算结果进行查询
        
        .. code-block:: python

                time.sleep(8)
                QCM.get_result(taskid,,ClusterMachineType.Full_AMPLITUDE)

        结果会在当前目录下生成结果文件，以taskid命名。内容如下：
        
        .. code-block:: python

                0 : 0.13
                1 : 0.15
                2 : 0.12
                3 : 0.14
                4 : 0.1
                5 : 0.11
                6 : 0.11
                7 : 0.14

        结果左侧是量子态的十进制表示，右边表示测量对应的概率

    .. note:: 
        - 量子云计算平台还支持 ``full_amplitude_pmeasure(全振幅概率测量操作)`` 丶 ``partial_amplitude_pmeasure(部分振幅概率测量操作)`` 和 ``single_amplitude_pmeasure(单振幅概率测量操作)`` ，它们的使用方法大同小异。
        - 量子云虚拟机未来会加入含噪声量子算法模拟以及量子化学模拟，敬请期待。
