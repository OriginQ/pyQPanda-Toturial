量子程序转化OriginIR
=======================
----

通过该功能模块，你可以解析通过QPanda2构建的量子程序，将其中包含的量子比特信息以及量子逻辑门操作信息提取出来，得到按固定格式存储的OriginIR。

.. _OriginIR介绍: https://qpanda-toturial.readthedocs.io/zh/latest/QProgToOriginIR.html#id2

OriginIR
>>>>>>>>>>>>>>>>>
----

OriginIR的书写格式规范与例程可以参考量子程序转化OriginIR模块中的 `OriginIR介绍`_


QPanda2提供了OriginIR转换工具接口 ``transform_qprog_to_originir`` 该接口使用非常简单，具体可参考下方示例程序。

实例
>>>>>>>>>>>>>>
----

下面的例程通过简单的接口调用演示了量子程序转化OriginIR的过程

    .. code-block:: python

        from pyqpanda import *

        if __name__ == "__main__":
            machine = init_quantum_machine(QMachineType.CPU)
            qlist = machine.qAlloc_many(4)
            clist = machine.cAlloc_many(4)
            
            prog = CreateEmptyQProg()
            prog_cir = CreateEmptyCircuit()
            prog_cir.insert(Y(qlist[2])).insert(H(qlist[2])).insert(CNOT(qlist[0],qlist[1]))
            qwhile = CreateWhileProg(clist[1], prog_cir)
            
            prog.insert(H(qlist[2])).insert(measure(qlist[1],clist[1])).insert(qwhile)
            
            print(transform_qprog_to_originir(prog,machine))
            
            destroy_quantum_machine(machine)


具体步骤如下:

 - 首先在主程序中用 ``init_quantum_machine`` 初始化一个量子虚拟机对象，用于管理后续一系列行为

 - 接着用 ``qAlloc_many`` 和 ``cAlloc_many`` 初始化量子比特与经典寄存器数目

 - 然后调用 ``CreateEmptyQProg`` 构建量子程序

 - 最后调用接口 ``transform_qprog_to_originir`` 输出OriginIR字符串，并用 ``destroy_quantum_machine`` 释放系统资源

运行结果如下：

    .. code-block:: python

        QINIT 4
        CREG 4
        H q[2]
        MEASURE q[1],c[1]
        QWHILE c[1]
        Y q[2]
        H q[2]
        CNOT q[0],q[1]
        ENDQWHILE


   .. note:: 对于暂不支持的操作类型，OriginIR会显示UnSupported XXXNode，其中XXX为具体的节点类型。


.. warning:: 
        新版本中接口名有所调整，旧接口 ``to_originir`` 将由 ``transform_qprog_to_originir`` 替代。\
      
        ``to_originir`` 将于下版本去除，请读者知悉。