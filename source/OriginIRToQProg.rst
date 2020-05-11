OriginIR转化为量子程序
=======================
----

通过该功能模块，你可以解析OriginIR文本文件，将其中的量子逻辑门操作信息提取出来，得到QPanda 2内部可操作的量子程序。

.. _OriginIR介绍: https://qpanda-toturial.readthedocs.io/zh/latest/QProgToOriginIR.html#id2

OriginIR
>>>>>>>
----

OriginIR的书写格式规范与例程可以参考量子程序转化OriginIR模块中的 `OriginIR介绍`_

QPanda 2提供了OriginIR文件转换工具接口 ``convert_originir_to_qprog`` 该接口使用非常简单，具体可参考下方示例程序。

实例
>>>>>>>
----

接下来通过简单的接口调用演示了OriginIR转化量子程序的过程

    .. code-block:: python
    
            from pyqpanda import *
            if __name__=="__main__":
                machine = init_quantum_machine(QMachineType.CPU)
                
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

                destroy_quantum_machine(machine)


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
        ENCONTROL
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

.. warning:: 
        新增接口 ``convert_originir_to_qprog()`` ，与老版本接口 ``transform_originir_to_qprog()`` 功能相同。