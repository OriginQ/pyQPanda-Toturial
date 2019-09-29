.. _QGateCompare:

不支持的量子逻辑门统计
======================

简介
--------------

统计量子程序、量子线路、量子循环控制、量子条件控制中不支持的量子逻辑门个数，也可以判断一个量子逻辑门是否支持。

接口介绍
--------------

我们先用pyqpanda构建一个量子程序：

    .. code-block:: python
          
        prog = QProg()
        prog.insert(X(qubits[0])).insert(Y(qubits[1]))\
            .insert(H(qubits[0])).insert(RX(qubits[0], 3.14))\
            .insert(measure(qubits[0], cbits[0]))

然后调用 ``get_unsupport_qgate_num`` 统计不支持量子逻辑门的个数

    .. code-block:: python
          
        single_gates = ["H"]        #支持的单量子逻辑门类型
        double_gates = ["CNOT"]     #支持的双量子逻辑门类型
        gates = [single_gates, double_gates]
        num = size_t num = get_unsupport_qgate_num(prog, gates)

.. note:: 统计 ``QCircuit`` 、 ``QWhileProg`` 、``QIfProg`` 、 ``QGate`` 中不支持的量子逻辑门的个数和 ``QProg`` 类似。

实例
-------------

    .. code-block:: python
    
        from pyqpanda import *

        if __name__ == "__main__":
            machine = init_quantum_machine(QMachineType.CPU)
            qubits = machine.qAlloc_many(4)
            cbits = machine.cAlloc_many(4)
            prog = QProg()
            prog.insert(X(qubits[0])).insert(Y(qubits[1]))\
            .insert(H(qubits[0])).insert(RX(qubits[0], 3.14))\
            .insert(measure(qubits[0], cbits[0]))

            single_gates = ["H"]        #支持的单量子逻辑门类型
            double_gates = ["CNOT"]     #支持的双量子逻辑门类型
            gates = [single_gates, double_gates]
            num = get_unsupport_qgate_num(prog, gates)
            print("unsupport QGate num: " + str(num))
            destroy_quantum_machine(machine)

运行结果：

    .. code-block:: python

        unsupport QGate num: 4

    
