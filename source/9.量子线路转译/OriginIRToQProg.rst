

通过该功能模块，你可以解析OriginIR文本文件，将其中的量子逻辑门操作信息提取出来，得到QPanda 2内部可操作的量子程序。

QPanda 2提供了OriginIR文件转换工具接口 ``convert_originir_to_qprog`` 该接口使用非常简单

.. function:: convert_originir_to_qprog(file_path: str, machine: QuantumMachine) -> list

    将 OriginIR 指令集转换为量子程序的函数
    ==========================================

    该函数将 OriginIR 指令集文件转换为量子程序。

    :param file_path: OriginIR 文件的文件路径。
    :type file_path: str
    :param machine: 初始化的量子机器。
    :type machine: QuantumMachine
    :return: 包含转换后的 QProg、量子比特列表和经典比特列表的列表。
    :rtype: list
    :raises run_fail: 转换 OriginIR 到 QProg 失败。

    该函数的主要目的是读取给定的 OriginIR 指令集文件，并将其转换为一个 QProg 量子程序。要进行转换的 OriginIR 文件路径需要提供，同时需要提供一个初始化的量子机器。返回的结果列表包含了转换后的 QProg，以及用于 QProg 的量子比特列表和经典比特列表。

    示例用法::

        # 初始化量子机器
        qvm = CPUQVM()
        qvm.init_qvm()

        # 转换 OriginIR 文件为 QProg

        result = convert_originir_to_qprog("path/to/originir/file.ir", qvm)
        qprog, qubit_list, cbit_list = result

接下来通过简单的接口调用演示了OriginIR转化量子程序的过程

    .. code-block:: python
    
            from pyqpanda import *
            if __name__=="__main__":

                machine = CPUQVM()
                machine.init_qvm()
                # 编写OriginIR文件
                f = open('testfile.txt', mode='w',encoding='utf-8')
                f.write("""QINIT 4
                    CREG 4
                    DAGGER
                    X q[1]
                    X q[2]
                    CONTROL q[1], q[2]
                    RY q[0], (1.047198)
                    ENDCONTROL
                    ENDDAGGER
                    MEASURE q[0], c[0]
                    QIF c[0]
                    H q[1]
                    H q[2]
                    RZ q[2], (2.356194)
                    CU q[2], q[3], (3.141593, 4.712389, 1.570796, -1.570796)
                    CNOT q[2], q[1]
                    ENDQIF
                    """)

                f.close()

                # OriginIR转换量子程序, 返回转换后的量子程序、量子程序使用的量子比特以及经典寄存器
                prog, qv, cv = convert_originir_to_qprog("testfile.txt", machine)
                
                # 量子程序转换OriginIR，打印并对比转换结果
                print(convert_qprog_to_originir(prog,machine))

具体步骤如下:

 - 首先编写OriginIR，并将其保存到指定文件中
 
 - 接着在主程序中用 ``init_quantum_machine`` 初始化一个量子虚拟机对象，用于管理后续一系列行为

 - 然后调用 ``convert_originir_to_qprog`` 接口将OriginIR转换为量子程序

 - 最后调用 ``convert_qprog_to_originir`` 接口，把量子程序转为OriginIR，通过比较输入和生成的OriginIR是否相同，判断OriginIR是否正确转换成量子程序，并且用 ``destroy_quantum_machine`` 释放系统资源

运行结果如下：

    .. code-block:: c

        QINIT 4
        CREG 4
        DAGGER
        X q[1]
        X q[2]
        CONTROL q[1],q[2]
        RY q[0],(1.047198)
        ENDCONTROL
        ENDDAGGER
        MEASURE q[0],c[0]
        QIF c[0]
        H q[1]
        ELSE
        H q[2]
        RZ q[2],(2.356194)
        CU q[2],q[3],(3.141593,4.712389,1.570796,-1.570796)
        CNOT q[2],q[1]
        ENDQIF
        
.. note:: 对于暂不支持的操作类型，可能会在OriginIR转化成量子程序的过程中发生错误。

