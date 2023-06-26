NodeIter
==============

NodeIter，是pyQPanda对外提供的 QProg 或者 QCircuit 遍历迭代器，我们可以通过NodeIter很方便的管理我们的量子程序。

接口介绍
>>>>>>>>>>>>>>>>

目前NodeIter主要提供以下几种操作：
获取下一个节点

::

    iter = iter.get_next()
    
获取前项节点

::

    iter = iter.get_pre()
    

获取节点类型

::

    type = iter.get_node_type()
    
通过迭代器构造QProg

::

    type = iter.get_node_type()
    if pq.NodeType.PROG_NODE == type:
        prog = pq.QProg(iter)

通过迭代器构造量子线路QCircuit

::

    type = iter.get_node_type()
    if pq.NodeType.CIRCUIT_NODE == type:
        cir = pq.QCircuit(iter)
        
通过迭代器构造QGate

::

    type = iter.get_node_type()
    if pq.NodeType.GATE_NODE == type:
        gate = pq.QGate(iter)
        
通过迭代器构造QIfProg

::

    type = iter.get_node_type()
    if pq.NodeType.QIF_START_NODE == type:
        if_prog = pq.QIfProg(iter)
        
通过迭代器构造QWhileProg

::

    type = iter.get_node_type()
    if pq.NodeType.WHILE_START_NODE == type:
        while_prog = pq.QWhileProg(iter)
        
通过迭代器构造QMeasure

::

    type = iter.get_node_type()
    if pq.NodeType.MEASURE_GATE == type:
        measure_gate = pq.QMeasure(iter)
        
实例
>>>>>>>>>>

以下实例程序是通过 NodeIter 实现遍历一个QProg，并输出各个节点逻辑门类型的功能：

::

    import pyqpanda.pyQPanda as pq
    import math
        
    machine = pq.init_quantum_machine(pq.QMachineType.CPU)
    q = machine.qAlloc_many(8)
    c = machine.cAlloc_many(8)
    prog = pq.QProg()

    prog << pq.H(q[0]) << pq.S(q[2]) << pq.CNOT(q[0], q[1]) << pq.CZ(q[1], q[2]) << pq.CR(q[1], q[2], math.pi/2)
    iter = prog.begin()
    iter_end = prog.end()
    while  iter != iter_end:
        if pq.NodeType.GATE_NODE == iter.get_node_type():
            gate = pq.QGate(iter)
            print(gate.gate_type())
        iter = iter.get_next()
    else:
        print('Traversal End.\n')

    pq.destroy_quantum_machine(machine)

运行结果：

::

    9
    11
    21
    22
    28
    Traversal End.

反向遍历：

::

    import pyqpanda.pyQPanda as pq
    import math

    machine = pq.init_quantum_machine(pq.QMachineType.CPU)
    q = machine.qAlloc_many(8)
    c = machine.cAlloc_many(8)
    prog = pq.QProg()

    prog << pq.H(q[0]) << pq.S(q[2]) << pq.CNOT(q[0], q[1]) << pq.CZ(q[1], q[2]) << pq.CR(q[1], q[2], math.pi/2)
    iter_head = prog.head()
    iter = prog.last()
    while  iter != iter_head:
        if pq.NodeType.GATE_NODE == iter.get_node_type():
            gate = pq.QGate(iter)
            print(gate.gate_type())
        iter = iter.get_pre()
    else:
        print('Traversal End.\n')

运行结果：

::

    28
    22
    21
    11
    9
    Traversal End.
