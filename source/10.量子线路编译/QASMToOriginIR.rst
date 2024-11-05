.. _`QASMToOriginIR`: 


QASMToOriginIR
=======================

简介
----

通过该功能模块，可以解析QASM文本文件（或者字符串），将其中的量子逻辑门操作信息提取出来，得到OriginIR的指令字符串。

接口介绍
---------

**QPanda 2提供了QASM字符串转换工具接口** ``convert_qasm_string_to_originir`` **。**

.. function:: convert_qasm_string_to_originir(qasm_str: str) -> str:

    该函数的作用是根据给定的QASM指令字符串生成对应的OriginIR指令字符串

    :param qasm_str: QASM指令字符串
    :type qasm_str: str
    :return: 转换得到的OriginIR指令字符串
    :rtype: str

    **示例用法:**

    .. code-block:: python
    
        from pyqpanda.pyQPanda import convert_qasm_string_to_originir

        #准备qasm指令字符串
        qasm_str = """OPENQASM 3.0;
            include "stdgates.inc";
            qubit[4] q;
            bit[2] c;
            rx(3.14) q[0];
            phase(3.18) q[0];
            c[0] = measure q[0];
            c[1] = measure q[1];
                    """
        #根据qasm指令字符串生成OriginIR指令字符串
        originir_str = convert_qasm_string_to_originir(qasm_str=qasm_str)
        #打印生成的OriginIR指令字符串
        print(originir_str)

    **示例代码输出结果:**

    .. code-block:: bash
        
        QINIT 4
        CREG 2
        RX q[0],(3.14)
        P q[0],(3.18)
        MEASURE q[0],c[0]
        MEASURE q[1],c[1]
        

**QPanda 2提供了QASM文件转换工具接口** ``convert_qasm_to_originir`` **。**

.. function:: convert_qasm_to_originir(file_path: str) -> str:

    该函数的作用是根据给定的QASM指令字符串生成对应的OriginIR指令字符串

    :param file_path: 存储QASM指令字符串的文件
    :type file_path: str
    :return: 转换得到的OriginIR指令字符串
    :rtype: str

    **示例用法:**

    .. code-block:: python
        
        from pyqpanda.pyQPanda import QMachineType, convert_qasm_to_originir, init_quantum_machine

        #########################准备包含QASM指令字符串的文件
        qasm_file = "test.qasm"
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
        #######################根据包含QASM指令字符串的文件生成OriginIR指令字符串
        originir_str = convert_qasm_to_originir(qasm_file)
        #######################打印结果
        print( originir_str)

    **示例代码输出结果:**

    .. code-block:: bash

        ### opened qasm file:test.qasm
        QINIT 4
        CREG 2
        RX q[0],(3.14)
        P q[0],(3.18)
        MEASURE q[0],c[0]
        MEASURE q[1],c[1]
