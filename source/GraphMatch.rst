.. _量子线路查询替换:

量子线路查询替换
=========================
----

在量子计算中，存在一些量子逻辑门或量子线路是可以相互替代的，比如如下替换过程：

H(0)->CNOT(1,0)->H(0)
可以替换为
CZ(1,0)

使用接口介绍
>>>>>>>>>>>>>>>>
----

在量子程序中，可能存在多个相同结构的子量子线路或多个相同的量子逻辑门，查询替换量子程序中指定结构的量子线路的功能就是找这些相同结构的子量子线路并把它们替换成目标量子线路。

在pyQPanda中，通过graph_query_replace接口实现该功能，输入参数一为待替换修改的量子程序节点，输入参数二为查询图量子线路节点，输入参数三为替换图量子线路节点，输入参数四为量子虚拟机。

示例
>>>>>>>>>>>>>>>>
----

     .. code-block:: python

        from pyqpanda import *

        machine = init_quantum_machine(QMachineType.CPU)
        q = machine.qAlloc_many(4)
        c = machine.cAlloc_many(4)
        
        # 构建量子程序
        prog = QProg()
        prog.insert(H(q[0]))\
            .insert(H(q[2]))\
            .insert(H(q[3]))\
            .insert(CNOT(q[1], q[0]))\
            .insert(H(q[0]))\
            .insert(CNOT(q[1], q[2]))\
            .insert(H(q[2]))\
            .insert(CNOT(q[2], q[3]))\
            .insert(H(q[3]))

        # 构建查询线路
        query_cir = QCircuit()
        query_cir.insert(H(q[0]))\
                .insert(CNOT(q[1], q[0]))\
                .insert(H(q[0]))
        
        # 构建替换线路
        replace_cir = QCircuit()
        replace_cir.insert(CZ(q[1], q[0]))

        print(convert_qprog_to_originir(prog,machine))

        # 搜索量子程序中的查询线路，并用替换线路替代
        update_prog = graph_query_replace(prog, query_cir, replace_cir, machine)
       
        print(convert_qprog_to_originir(update_prog,machine))

运行结果如下：

查询替换前：

    .. code-block:: c

        QINIT 4
        CREG 0
        H q[0]
        H q[2]
        H q[3]
        CNOT q[1],q[0]
        H q[0]
        CNOT q[1],q[2]
        H q[2]
        CNOT q[2],q[3]
        H q[3]

查询替换后： 

    .. code-block:: c

        QINIT 4
        CREG 0
        CZ q[0],q[1]
        CZ q[2],q[1]
        CZ q[3],q[2]

    .. warning::

        1. 查询量子线路和替代量子线路控制的量子比特必须一一对应。
        2. 查询量子线路和替代量子线路对应的有向无环图必须为连通图。