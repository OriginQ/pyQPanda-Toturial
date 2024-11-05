.. _`PyquilToQProg`:

PyquilToQProg
=======================

简介
----

通过该功能模块，可以解析Pyquil文本文件（或者字符串），将其中的量子逻辑门操作信息提取出来，得到QPanda 2内部可操作的量子程序。

接口介绍
---------

**QPanda 2提供了Pyquil文件转换工具接口** ``convert_pyquil_file_to_qprog`` **。**

.. function:: convert_pyquil_file_to_qprog(file_path: str, machine: QuantumMachine) -> list:

    该函数的作用是从给定的 Pyquil 文件中读取指令集并将其转换为量子程序，同时需要提供一个已初始化的量子机器实例。

    :param file_path: Pyquil 文件路径。
    :type file_path: str
    :param machine: 已初始化的量子机器实例。
    :type machine: QuantumMachine
    :return: 包含转换后的 QProg、量子比特列表和经典比特列表的列表。
    :rtype: list
    :raises run_fail: Pyquil转换为 QProg 失败。

    返回的列表包含了转换后的 QProg 以及与之关联的量子比特列表和经典比特列表。您可以根据需要进一步操作这些信息，例如执行量子程序、获取测量结果等。

    **示例用法:**

    .. code-block:: python

        from pyqpanda.pyQPanda import init_quantum_machine,QMachineType,destroy_quantum_machine,convert_pyquil_file_to_qprog
        #########################准备包含Pyquil指令字符串的文件
        # 定义Pyquil指令字符串
        pyquil_str = """DECLARE ro BIT[1]
        DECLARE theta REAL[2]
        SWAP 0 1
        H 0
        """
        # 创建包含Pyquil指令字符串的文件
        pyquil_file = "example.pyquil"
        with open(pyquil_file, "w") as file:
            # 将字符串写入文件
            file.write(pyquil_str)

        #########################将包含Pyquil指令字符串的文件转换为QProg
        # 初始化 QuantumMachine 实例

        machine = init_quantum_machine(QMachineType.CPU)

        # 将 Pyquil 文件转换为 QProg
        qprog, qbits, cbits = convert_pyquil_file_to_qprog(pyquil_file,machine)

        # 打印转换结果
        print("qprog:",end='\n')
        print(qprog,end='\n')
        print("qbits:",end='\n')
        print(qbits)
        print("cbits:",end='\n')
        print(cbits)

        # 销毁 QuantumMachine 实例
        destroy_quantum_machine(machine)

    **示例代码运行结果:**

    .. code-block:: bash
        
        qprog:

                    ┌─┐ 
        q_0:  |0>─X ┤H├ 
                  │ └─┘ 
        q_1:  |0>─X ─── 
                
         c :   / ═
          


        qbits:
        [<pyqpanda.pyQPanda.Qubit object at 0x00000229BB8915B0>, <pyqpanda.pyQPanda.Qubit object at 0x00000229BB891570>]
        cbits:
        [<pyqpanda.pyQPanda.ClassicalCondition object at 0x00000229ED0E42F0>, <pyqpanda.pyQPanda.ClassicalCondition object at 0x00000229ED1BE270>, <pyqpanda.pyQPanda.ClassicalCondition object at 0x00000229ED1DA230>, <pyqpanda.pyQPanda.ClassicalCondition object at 0x00000229ED0D32F0>]




**QPanda 2提供了Pyquil字符串转换工具接口** ``convert_pyquil_string_to_qprog`` **。**

.. function:: convert_pyquil_string_to_qprog(pyquil_str: str, machine: QuantumMachine) -> list:

    该函数的作用是从给定的 Pyquil 文件中读取指令集并将其转换为量子程序，同时需要提供一个已初始化的量子机器实例。

    :param pyquil_str: Pyquil 文件路径。
    :type pyquil_str: str
    :param machine: 已初始化的量子机器实例。
    :type machine: QuantumMachine
    :return: 包含转换后的 QProg、量子比特列表和经典比特列表的列表。
    :rtype: list
    :raises run_fail: Pyquil转换为 QProg 失败。

    返回的列表包含了转换后的 QProg 以及与之关联的量子比特列表和经典比特列表。您可以根据需要进一步操作这些信息，例如执行量子程序、获取测量结果等。

    **示例用法:**

    .. code-block:: python

        from pyqpanda.pyQPanda import init_quantum_machine,convert_pyquil_string_to_qprog,QMachineType,destroy_quantum_machine

        # 定义pyquil指令字符串
        pyquil_str = """DECLARE ro BIT[1]
        DECLARE theta REAL[2]
        SWAP 0 1
        H 0
        """
        # 初始化 QuantumMachine 实例
        machine = init_quantum_machine(QMachineType.CPU)

        # 将 Pyquil 文件转换为 QProg
        qprog, qbits, cbits = convert_pyquil_string_to_qprog(pyquil_str,machine)

        # 打印转换结果
        print("qprog:",end='\n')
        print(qprog,end='\n')
        print("qbits:",end='\n')
        print(qbits)
        print("cbits:",end='\n')
        print(cbits)

        # 销毁 QuantumMachine 实例
        destroy_quantum_machine(machine)

    **示例代码运行结果:**

    .. code-block:: bash
        
        qprog:

                    ┌─┐ 
        q_0:  |0>─X ┤H├ 
                  │ └─┘ 
        q_1:  |0>─X ─── 
                
         c :   / ═
          


        qbits:
        [<pyqpanda.pyQPanda.Qubit object at 0x0000025B871313F0>, <pyqpanda.pyQPanda.Qubit object at 0x0000025B871314B0>]
        cbits:
        [<pyqpanda.pyQPanda.ClassicalCondition object at 0x0000025B87131830>, <pyqpanda.pyQPanda.ClassicalCondition object at 0x0000025BB8C89EF0>, <pyqpanda.pyQPanda.ClassicalCondition object at 0x0000025BB898BFB0>, <pyqpanda.pyQPanda.ClassicalCondition object at 0x0000025BB897EBF0>]

