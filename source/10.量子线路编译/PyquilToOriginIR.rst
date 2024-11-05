.. _`PyquilToOriginIR`:

PyquilToOriginIR
=======================

简介
----

通过该功能模块，可以解析Pyquil文本文件（或者字符串），将其中的量子逻辑门操作信息提取出来，得到OriginIR的指令字符串。

接口介绍
---------

**QPanda 2提供了Pyquil字符串转换工具接口** ``convert_pyquil_string_to_originir`` **。**

.. function:: convert_pyquil_string_to_originir(pyquil_str: str) -> str:

    该函数的作用是根据给定的pyquil指令字符串生成对应的OriginIR指令字符串

    :param pyquil_str: pyquil指令字符串
    :type pyquil_str: str
    :return: 转换得到的OriginIR指令字符串
    :rtype: str

    **示例用法:**

    .. code-block:: python

        from pyqpanda.pyQPanda import init_quantum_machine,QMachineType,destroy_quantum_machine,convert_pyquil_string_to_originir
        # 定义Pyquil指令字符串
        pyquil_str = """DECLARE ro BIT[2]
        SWAP 0 1
        H 0
        """

        #########################将包含Pyquil指令字符串的文件转换为OriginIR指令字符串

        # 将 Pyquil 文件转换为 OriginIR指令字符串
        originir_str =convert_pyquil_string_to_originir(pyquil_str)

        # 打印转换结果
        print(originir_str)

    **示例代码运行结果:**

    .. code-block:: bash

        
        QINIT 2
        CREG 3
        SWAP q[0],q[1]
        H q[0]

    



**QPanda 2提供了pyquil文件转换工具接口** ``convert_pyquil_file_to_originir`` **。**

.. function:: convert_pyquil_file_to_originir(file_path: str) -> str:

    该函数的作用是根据给定的Pyquil指令字符串生成对应的OriginIR指令字符串

    :param file_path: 存储Pyquil指令字符串的文件
    :type file_path: str
    :return: 转换得到的OriginIR指令字符串
    :rtype: str

    **示例用法:**

    .. code-block:: python

        from pyqpanda.pyQPanda import init_quantum_machine,QMachineType,destroy_quantum_machine,convert_pyquil_file_to_originir
        #########################准备包含Pyquil指令字符串的文件
        # 定义Pyquil指令字符串
        pyquil_str = """DECLARE ro BIT[2]
        SWAP 0 1
        H 0
        """
        # 创建包含Pyquil指令字符串的文件
        pyquil_file = "example.pyquil"
        with open(pyquil_file, "w") as file:
            # 将字符串写入文件
            file.write(pyquil_str)

        #########################将包含Pyquil指令字符串的文件转换为OriginIR指令字符串

        # 将 Pyquil 文件转换为 OriginIR指令字符串
        originir_str = convert_pyquil_file_to_originir(pyquil_file)

        # 打印转换结果
        print(originir_str)

    **示例代码运行结果:**

    .. code-block:: bash
        
        QINIT 2
        CREG 3
        SWAP q[0],q[1]
        H q[0]