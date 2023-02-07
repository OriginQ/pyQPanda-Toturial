.. _QGateCounter:

逻辑门统计
===============

简介
--------------

逻辑门的统计是指统计量子程序、量子线路、量子循环控制或量子条件控制中所有的量子逻辑门个数方法。

接口介绍
--------------

我们先用pyqpanda构建一个量子程序：

    .. code-block:: python
          
        prog = QProg()
        prog << X(qubits[0]) << Y(qubits[1])\
             << H(qubits[0]) << RX(qubits[0], 3.14)\
             << Measure(qubits[0], cbits[0])

然后调用接口 ``get_qgate_num`` 统计量子逻辑门的个数，

    .. code-block:: python
          
        number = get_qgate_num(prog)

.. note::  统计 ``QCircuit`` 、 ``QWhileProg`` 、``QIfProg`` 中量子逻辑门的个数和 ``QProg`` 类似。

实例
-------------

    .. code-block:: python
    
        from pyqpanda import *

        if __name__ == "__main__":
            qvm = CPUQVM()
            qvm.init_qvm()
            qubits = qvm.qAlloc_many(2)
            cbits = qvm.cAlloc_many(2)

            prog = QProg()
            
            # 构建量子程序
            prog << X(qubits[0]) << Y(qubits[1])\
                << H(qubits[0]) << RX(qubits[0], 3.14)\
                << Measure(qubits[0], cbits[0])

            # 统计逻辑门个数
            number = get_qgate_num(prog)
            print("QGate number: " + str(number))



运行结果：

    .. code-block:: python

        QGate number: 4


此外在PyQPanda中还有一种统计某个线路中的某种逻辑门个数的接口。

接口介绍
--------------

我们先用pyqpanda构建一个量子程序：

    .. code-block:: python

        import pyqpanda.pyQPanda as pq

        class InitQMachine:
            def __init__(self, quBitCnt, cBitCnt, machineType=pq.QMachineType.CPU):
                self.m_machine = pq.init_quantum_machine(machineType)
                self.m_qlist = self.m_machine.qAlloc_many(quBitCnt)
                self.m_clist = self.m_machine.cAlloc_many(cBitCnt)


        if __name__ == "__main__":
            init_machine = InitQMachine(8, 8)
            qlist = init_machine.m_qlist
            clist = init_machine.m_clist
            prog = pq.QProg()

            cir = pq.QCircuit()
            cir.insert( pq.X(qlist[0])).insert( pq.X(qlist[1])).insert(
                pq.Y(qlist[1])).insert(pq.H(qlist[0])).insert(pq.Z(qlist[1])).insert( pq.RX(qlist[0], 3.14))

            prog.insert(cir).insert(pq.T(qlist[0])).insert(pq.CNOT(qlist[1], qlist[2])).insert(pq.H(qlist[3])).insert(
                pq.H(qlist[4])).insert(pq.X(qlist[4])).insert(pq.measure_all(qlist, clist))
        
            # 统计逻辑门个数
            total_num = pq.count_qgate_num(prog )

            # 统计X逻辑门个数
            Xnum = pq.count_qgate_num(prog, pq.PAULI_X_GATE);

            # 统计H逻辑门个数
            Hnum = pq.count_qgate_num(prog, pq.HADAMARD_GATE);

            # 统计ISWAP逻辑门个数
            ISWAPnum = pq.count_qgate_num(prog, pq.ISWAP_GATE);

            print("QGate number: " , total_num)
            print("XGate number: " , Xnum) 
            print("HGate number: " , Hnum) 
            print("ISWAPGate number: " , ISWAPnum)
        
运行结果：

    .. code-block:: python

        QGate number: 11
        XGate number:  3
        HGate number:  3
        ISWAPGate number:  0
    