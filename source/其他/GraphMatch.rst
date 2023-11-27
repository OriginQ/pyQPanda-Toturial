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

提供了统一的量子线路优化接口： ``circuit_optimizer`` ，该接口可实现多种量子线路的查询替换，对应的接口参数：
参数1：QProg 待优化的原始量子程序
参数2：vector 子线路查询替换队列，每个队列元素包含目标搜索线路和对应的替换线路


示例
>>>>>>>>>>>>>>>>
----

     .. code-block:: python

        from pyqpanda import *
        if __name__=="__main__":
            machine = CPUQVM()
            machine.init_qvm()
            q = machine.qAlloc_many(4)
            c = machine.cAlloc_many(4)
            # 构建量子程序
            prog = QProg()
            prog << H(q[0])\
                << H(q[2])\
                << H(q[3])\
                << CNOT(q[1], q[0])\
                << H(q[0])\
                << CNOT(q[1], q[2])\
                << H(q[2])\
                << CNOT(q[2], q[3])\
                << H(q[3])
            # 构建查询线路
            query_cir = QCircuit()
            query_cir << H(q[0])\
                    << CNOT(q[1], q[0])\
                    << H(q[0])
            # 构建替换线路
            replace_cir = QCircuit()
            replace_cir << CZ(q[1], q[0])
            print("查询替换前：")
            print(convert_qprog_to_originir(prog,machine))
            # 搜索量子程序中的查询线路，并用替换线路替代
            update_prog = circuit_optimizer(prog, [[query_cir, replace_cir]])
            print("查询替换后：")
            print(convert_qprog_to_originir(update_prog,machine))

运行结果如下：

查询替换前：

    .. code-block:: c

        QINIT 4
        CREG 4
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
        CREG 4
        CZ q[1],q[0]
        CZ q[1],q[2]
        CZ q[2],q[3]
        
.. warning::

        1. 查询量子线路和替代量子线路控制的量子比特必须一一对应。
        2. 查询量子线路和替代量子线路对应的有向无环图必须为连通图。