量子线路字符画
============

接口draw_qprog()可以将输入的量子程序转换为字符画并输出到控制台同时保存字符画信息到文件（QCircuitTextPic.txt，该接口会在当前程序运行目录下创建该txt文件，文件用utf8编码，并覆盖之前数据）。
    
量子线路字符画时序表示
====================

接口draw_qprog_with_clock()可以将输入的量子程序转换为字符画并根据各种逻辑门的时序配置信息分层显示到控制台并保存信息到文件（QCircuitTextPic.txt，该接口会在当前程序运行目录下创建该txt文件，文件用utf8编码，并覆盖之前数据），接口功能和draw_qprog()接口功能类似，只是会在构建字符画的同时，根据逻辑门的时序信息进行分层显示。
默认的各种逻辑门时序配置如下：
::
    <QGateTimeSequence>
      <QMeasureTimeSequence>2</QMeasureTimeSequence>
      <QSwapTimeSequence>2</QSwapTimeSequence>
      <QGateControlTimeSequence>2</QGateControlTimeSequence>
      <QGateSingleTimeSequence>1</QGateSingleTimeSequence>
    </QGateTimeSequence>

可以看到目前逻辑门总共分成4种类型，除了单门占1个时序外，其他类型分别各自占用2个时序，用户可以根据实际情况自行在配置文件中配置各种逻辑门的时序信息。

.. note:: 用户可通过如下链接地址获取默认配置文件 `QPandaConfig.xml <https://github.com/OriginQ/QPanda-2/blob/master/QPandaConfig.xml>`_ , 将该默认配置文件放在执行程序同级目录下，可执行程序会自动解析该文件。

实例
---------------

::

    import pyqpanda.pyQPanda as pq
    import math
    class InitQMachine:
        def __init__(self, quBitCnt, cBitCnt, machineType = pq.QMachineType.CPU):
            self.m_machine = pq.init_quantum_machine(machineType)
            self.m_qlist = self.m_machine.qAlloc_many(quBitCnt)
            self.m_clist = self.m_machine.cAlloc_many(cBitCnt)

        def __del__(self):
            pq.destroy_quantum_machine(self.m_machine)
    
    def test_print_qcircuit(q, c):
        prog = pq.QCircuit()
        prog.insert(pq.CU(1, 2, 3, 4, q[0], q[5])).insert(pq.H(q[0])).insert(pq.S(q[2])).insert(pq.CNOT(q[0], q[1])).insert(pq.CZ(q[1], q[2])).insert(pq.CR(q[2], q[1], math.pi/2))
        prog.set_dagger(True)
        print('draw_qprog:')
        pq.draw_qprog(prog )
        print('draw_qprog_with_clock:')
        pq.draw_qprog_with_clock(prog)
    
    if __name__=="__main__":
        init_machine = InitQMachine(16, 16)
        qlist = init_machine.m_qlist
        clist = init_machine.m_clist
        machine = init_machine.m_machine

        test_print_qcircuit(qlist, clist)
        
以上示例分别演示了draw_qprog和draw_qprog_with_clock这两个接口的使用方法，上述代码的输出结果如下：

.. figure:: ./images/py_draw_prog.png
   :alt:
   
图中，第二个量子线路图是字符画时序展示效果，每个执行时序间用虚竖线表示。

其他使用
--------

接口draw_qprog()和draw_qprog_with_clock()的详细参数说明如下：
::
    def draw_qprog(prog: pyqpanda.pyQPanda.QProg, itr_start: pyqpanda.pyQPanda.NodeIter = <pyqpanda.pyQPanda.NodeIter>, itr_end: pyqpanda.pyQPanda.NodeIter = <pyqpanda.pyQPanda.NodeIter>)
    def draw_qprog_with_clock(prog: pyqpanda.pyQPanda.QProg, itr_start: pyqpanda.pyQPanda.NodeIter = <pyqpanda.pyQPanda.NodeIter>, itr_end: pyqpanda.pyQPanda.NodeIter = <pyqpanda.pyQPanda.NodeIter>)

可以看出这两个接口的参数类型一样，都有3个参数，并且后两个参数都为默认参数。这两个参数提供用户可根据实际需要，只打印某个量子程序中，某一区间段的量子线路信息，可以在某些场景下给用户以更灵活的使用方式。这里作为演示，我们将上述示例代码中的test_print_qcircuit()接口实现改成如下代码：
::

    prog = pq.QCircuit()
    prog.insert(pq.CU(1, 2, 3, 4, q[0], q[5])).insert(pq.H(q[0])).insert(pq.S(q[2])).insert(pq.CNOT(q[0], q[1])).insert(pq.CZ(q[1], q[2])).insert(pq.CR(q[2], q[1], math.pi/2))
    iter_start = prog.begin()
    iter_end = iter_start.get_next()
    iter_end = iter_end.get_next()
    iter_end = iter_end.get_next()
    prog.set_dagger(True)
    print('draw_qprog:')
    pq.draw_qprog(prog, iter_start, iter_end)
    print('draw_qprog_with_clock:')
    pq.draw_qprog_with_clock(prog, iter_start, iter_end)
    
上面这段示例代码只会输出prog的前4个逻辑门节点，用户可自行替换上述代码段到前面的示例程序中，运行查看结果，这里不再赘述。





