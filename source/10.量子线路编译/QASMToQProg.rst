QASM
=======================
----

通过该功能模块，你可以解析QASM文本文件，将其中的量子逻辑门操作信息提取出来，得到QPanda 2内部可操作的量子程序。

QASM介绍
---------

QPanda 2提供了QASM文件转换工具接口 ``convert_qasm_to_qprog`` 该接口使用非常简单。

.. function:: convert_qasm_to_qprog(file_path: str, machine: QuantumMachine) -> list

    该函数的作用是从给定的 QASM 文件中读取指令集并将其转换为量子程序，同时需要提供一个已初始化的量子机器实例。

    :param file_path: QASM 文件路径。
    :type file_path: str
    :param machine: 已初始化的量子机器实例。
    :type machine: QuantumMachine
    :return: 包含转换后的 QProg、量子比特列表和经典比特列表的列表。
    :rtype: list
    :raises run_fail: QASM 转换为 QProg 失败。

    返回的列表包含了转换后的 QProg 以及与之关联的量子比特列表和经典比特列表。您可以根据需要进一步操作这些信息，例如执行量子程序、获取测量结果等。

    示例用法::

        # 初始化 QuantumMachine 实例
        machine = CPUQVM()
        machine.init_qvm()
        
        # 将 QASM 文件转换为 QProg
        result = convert_qasm_to_qprog("my_circuit.qasm", machine)
        qprog, qubit_list, cbit_list = result
        
        # 执行量子程序并获取测量结果
        machine.run(qprog, qubit_list)
        measurement_results = machine.get_prob_dict(qubit_list)

接下来通过简单的接口调用演示了QASM转化量子程序的过程

    .. code-block:: python
    
        from pyqpanda import *

        if __name__=="__main__":
        
            machine = CPUQVM()
            machine.init_qvm()

            # 编写QASM文件
            f = open('testfile.txt', mode='w',encoding='utf-8')
            f.write("""// test QASM file
                OPENQASM 2.0;
                include "qelib1.inc";
                qreg q[3];
                creg c[3];
                x q[0];
                x q[1];
                z q[2];
                h q[0];
                tdg q[1];
                measure q[0] -> c[0];
                """)
            f.close()

            # QASM转换量子程序， 并返回量子程序、量子比特以及经典寄存器
            prog_trans, qv, cv = convert_qasm_to_qprog("testfile.txt", machine)

            # 量子程序转换QASM
            qasm = convert_qprog_to_qasm(prog_trans,machine)
            
            # 打印并对比转换结果
            print(qasm)


具体步骤如下:

 - 首先编写QASM，并将其保存到指定文件中。
 
 - 接着在主程序中用 ``init_quantum_machine`` 初始化一个量子虚拟机对象，用于管理后续一系列行为。

 - 然后调用 ``convert_qasm_to_qprog`` 接口将QASM转换为量子程序。

 - 最后调用 ``convert_qprog_to_qasm`` 接口，把量子程序转为QASM，通过比较量子程序执行结果，判断QASM是否正确转换成量子程序，并且用 ``destroy_quantum_machine`` 释放系统资源。

运行结果如下：

    .. code-block:: c

        OPENQASM 2.0;
        include "qelib1.inc";
        qreg q[3];
        creg c[3];
        u3(1.5707963267949037,3.1415926535897931,3.1415926535897931) q[0];
        u3(3.1415926535897931,2.3561944901923386,0) q[1];
        u3(0,3.1415926535897931,0) q[2];
        measure q[0] -> c[0];
        
.. note:: 上述示例中，由于QASM支持U3门，所以在QProg转QASM时，对量子线路做了优化，输出的QASM中只有U3门，这样可以有效降低量子线路深度。对于暂不支持的操作类型，可能会在QASM转化成量子程序的过程中发生错误。
