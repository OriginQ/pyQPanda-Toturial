NodeIter
==============
----

NodeIter，是PyPanda对外提供的QProg程序遍历迭代器，我们可以通过NodeIter很方便的管理我们的量子程序。

接口介绍
>>>>>>>>>>>>>>>>
----

目前NodeIter主要提供以下几种操作：
获取下一个节点

::

    iter = iter.get_next()
    
获取前项节点

::

    iter = iter.get_next()
    

获取节点类型

::

    type = iter.get_node_type()
    
实例
>>>>>>>>>>
----

以下实例程序是通过 NodeIter 实现遍历一个QProg，并输出各个节点逻辑门类型的功能：

::

    import pyqpanda.pyQPanda as pq
    import math
    
    machine = pq.init_quantum_machine(pq.QMachineType.CPU)
    q = machine.qAlloc_many(8)
    c = machine.cAlloc_many(8)
    prog = pq.QProg()
    
    prog.insert(pq.H(q[0])).insert(pq.S(q[2])).insert(pq.CNOT(q[0], q[1])).insert(pq.CZ(q[1], q[2])).insert(pq.CR(q[1], q[2], math.pi/2))
    iter = prog.begin()
    iter_end = prog.end()
    while  iter != iter_end:
        if pq.NodeType.GATE_NODE == iter.get_node_type():
            gate = pq.QGate(iter)
            print(gate.gate_type())
        iter = iter.get_next()
    else:
        print('Traversal End.\n')
    
    pq.destroy_quantum_machine(m_machine)

反向遍历：

::

    import pyqpanda.pyQPanda as pq
    import math
    
    machine = pq.init_quantum_machine(pq.QMachineType.CPU)
    q = machine.qAlloc_many(8)
    c = machine.cAlloc_many(8)
    prog = pq.QProg()
    
    prog.insert(pq.H(q[0])).insert(pq.S(q[2])).insert(pq.CNOT(q[0], q[1])).insert(pq.CZ(q[1], q[2])).insert(pq.CR(q[1], q[2], math.pi/2))
    iter_head = prog.head()
    iter = prog.last()
    while  iter != iter_head:
        if pq.NodeType.GATE_NODE == iter.get_node_type():
            gate = pq.QGate(iter)
            print(gate.gate_type())
        iter = iter.get_pre()
    else:
        print('Traversal End.\n')
