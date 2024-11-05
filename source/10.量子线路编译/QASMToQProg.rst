.. _`QASMToQProg`:

QASMToQProg
=======================

简介
----

通过该功能模块，可以解析QASM文本文件（或者字符串），将其中的量子逻辑门操作信息提取出来，得到QPanda 2内部可操作的量子程序。

接口介绍
---------

**QPanda 2提供了QASM文件转换工具接口** ``convert_qasm_to_qprog`` **。**

.. function:: convert_qasm_to_qprog(file_path: str, machine: QuantumMachine) -> list:

    该函数的作用是从给定的 QASM 文件中读取指令集并将其转换为量子程序，同时需要提供一个已初始化的量子机器实例。

    :param file_path: QASM 文件路径。
    :type file_path: str
    :param machine: 已初始化的量子机器实例。
    :type machine: QuantumMachine
    :return: 包含转换后的 QProg、量子比特列表和经典比特列表的列表。
    :rtype: list
    :raises run_fail: QASM 转换为 QProg 失败。

    返回的列表包含了转换后的 QProg 以及与之关联的量子比特列表和经典比特列表。您可以根据需要进一步操作这些信息，例如执行量子程序、获取测量结果等。

    **示例用法:**

    .. code-block:: python
    
        from pyqpanda.pyQPanda import QMachineType,destroy_quantum_machine, init_quantum_machine
        from pyqpanda.pyQPanda import convert_qasm_to_qprog

        #########################准备包含QASM指令字符串的文件
        qasm_file = "testfile.txt"
        f = open(qasm_file, mode='w', encoding='utf-8')
        f.write("""OPENQASM 3.0;
                         include "stdgates.inc";
                         qubit[4] q;
                         bit[2] c;
                         rx(3.14) q[0];
                         phase(3.18) q[0];
                         c[0] = measure q[0];
                         c[1] = measure q[1];
                """)
        f.close()
        #######################准备计算资源
        machine = init_quantum_machine(QMachineType.CPU)
        #######################根据包含QASM指令字符串的文件生成QProg实例
        qprog, qbits, cbits = convert_qasm_to_qprog(qasm_file,machine)
        # 打印转换结果
        print("qprog:",end='\n')
        print(qprog,end='\n')
        print("qbits:",end='\n')
        print(qbits)
        print("cbits:",end='\n')
        print(cbits)
        #######################释放计算资源
        destroy_quantum_machine(machine)


    **示例代码输出结果:**

    .. code-block:: bash

        ### opened qasm file:testfile.txt
        qprog:

                  ┌────────────┐ ┌───────────┐  ┌─┐ 
        q_0:  |0>─┤RX(3.140000)├ ┤P(3.180000)├ ─┤M├ 
                  └┬─┬─────────┘ └───────────┘  └╥┘ 
        q_1:  |0>──┤M├────────── ───────────── ──╫─ 
                   └╥┘                           ║  
         c :   / ═══╩════════════════════════════╩═
                     1                            0


        qbits:
        [<pyqpanda.pyQPanda.Qubit object at 0x000001553FF218B0>, <pyqpanda.pyQPanda.Qubit object at 0x000001553FF21870>, <pyqpanda.pyQPanda.Qubit object at 0x000001553FF21D30>, <pyqpanda.pyQPanda.Qubit object at 0x000001553FF4FAB0>]
        cbits:
        [<pyqpanda.pyQPanda.ClassicalCondition object at 0x0000015571C8E4B0>, <pyqpanda.pyQPanda.ClassicalCondition object at 0x0000015571C5BCB0>]


**QPanda 2提供了QASM指令字符串转换工具接口** ``convert_qasm_string_to_qprog`` **。**

.. function:: convert_qasm_string_to_qprog(qasm_str: str, machine: QuantumMachine) -> list:

    该函数的作用是从给定的 QASM 文件中读取指令集并将其转换为量子程序，同时需要提供一个已初始化的量子机器实例。

    :param qasm_str: QASM指令字符串
    :type qasm_str: str
    :param machine: 已初始化的量子机器实例。
    :type machine: QuantumMachine
    :return: 包含转换后的 QProg、量子比特列表和经典比特列表的列表。
    :rtype: list
    :raises run_fail: QASM 转换为 QProg 失败。

    返回的列表包含了转换后的 QProg 以及与之关联的量子比特列表和经典比特列表。您可以根据需要进一步操作这些信息，例如执行量子程序、获取测量结果等。

    **示例用法:**

    .. code-block:: python

        from pyqpanda.pyQPanda import QMachineType,destroy_quantum_machine, init_quantum_machine
        from pyqpanda.pyQPanda import convert_qasm_string_to_qprog

        #########################准备包含QASM指令字符串
        qasm_str = """OPENQASM 3.0;
                            include "stdgates.inc";
                            qubit[4] q;
                            bit[2] c;
                            rx(3.14) q[0];
                            phase(3.18) q[0];
                            c[0] = measure q[0];
                            c[1] = measure q[1];
        """

        #######################准备计算资源
        machine = init_quantum_machine(QMachineType.CPU)
        #######################根据包含QASM指令字符串的文件生成QProg实例
        qprog, qbits, cbits = convert_qasm_string_to_qprog(qasm_str,machine)
        # 打印转换结果
        print("qprog:",end='\n')
        print(qprog,end='\n')
        print("qbits:",end='\n')
        print(qbits)
        print("cbits:",end='\n')
        print(cbits) 
        #######################释放计算资源
        destroy_quantum_machine(machine)

    **示例代码输出结果:**

    .. code-block:: bash
        
        qprog:

                    ┌────────────┐ ┌───────────┐  ┌─┐ 
        q_0:  |0>─┤RX(3.140000)├ ┤P(3.180000)├ ─┤M├ 
                    └┬─┬─────────┘ └───────────┘  └╥┘ 
        q_1:  |0>──┤M├────────── ───────────── ──╫─ 
                    └╥┘                           ║  
            c :   / ═══╩════════════════════════════╩═
                        1                            0


        qbits:
        [<pyqpanda.pyQPanda.Qubit object at 0x000001A3AF6614B0>, <pyqpanda.pyQPanda.Qubit object at 0x000001A3AF661570>, <pyqpanda.pyQPanda.Qubit object at 0x000001A3AF6615F0>, <pyqpanda.pyQPanda.Qubit object at 0x000001A3AF6615B0>]
        cbits:
        [<pyqpanda.pyQPanda.ClassicalCondition object at 0x000001A3E0F068B0>, <pyqpanda.pyQPanda.ClassicalCondition object at 0x000001A3C8E72D70>]

