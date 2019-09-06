QNode迭代器
量子程序由一个个的量子逻辑门组成，组成量子程序的每个量子逻辑门称作一个节点，记为QNode。我们的量子程序结构和链表结构非常相似。
NodeIter，是PyPanda对外提供的一个功能组件，我们可以通过NodeIter的迭代器操作方法很方便的管理我们的量子程序。

接口介绍
目前NodeIter主要提供以下几种操作：
get_next 获取下一个节点
get_pre 获取前项节点
get_node_type 获取节点类型


实例
以下实例展示NodeIter 各种接口的使用方式：

::

    import pyqpanda.pyQPanda as pq
    import math
    
    machine = pq.init_quantum_machine(pq.QMachineType.CPU)
    q = machine.qAlloc_many(8)
    c = machine.cAlloc_many(8)
    prog = pq.QProg()
    
    prog.insert(pq.H(q[0])).insert(pq.S(q[2])).insert(pq.CNOT(q[0], q[1]))\
        .insert(pq.CZ(q[1], q[2])).insert(pq.CR(q[1], q[2], math.pi/2))
    iter_start = prog.begin()
    iter_end = iter_start.get_next()
    iter_end = iter_end.get_next()
    result_mat = pq.get_matrix(prog, iter_start, iter_end)
    pq.print_mat(result_mat)
