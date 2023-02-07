密度矩阵、Bloch球与量子态分布展示
====================

对于一些低量子比特系统而言，能够展示整个系统的量子态分布、密度矩阵分布或者Bloch轨迹，对于算法研究有很大帮助。
pyqpanda提供了类似的功能接口。

对于量子态，可以通过 ``state_to_density_matrix`` 转化为密度矩阵，参数是 **量子态数组** ，可以参考如下示例。

    .. code-block:: python

        from pyqpanda import *
        import numpy as np

        machine = CPUQVM()
        machine.init_qvm()
        qubits = machine.qAlloc_many(3)

        prog = QProg()
        prog << X(qubits[0:2])\
            << Z(qubits[:2])\
            << H(qubits[:])

        machine.directly_run(prog)
        state = machine.get_qstate()
        density_matrix = state_to_density_matrix(state)
        print(density_matrix)

输出结果如下：

    .. code-block:: python


        [[ 0.125+0.j -0.125-0.j -0.125-0.j  0.125+0.j  0.125+0.j -0.125-0.j
        -0.125-0.j  0.125+0.j]
        [-0.125+0.j  0.125+0.j  0.125+0.j -0.125+0.j -0.125+0.j  0.125+0.j
        0.125+0.j -0.125+0.j]
        [-0.125+0.j  0.125+0.j  0.125+0.j -0.125+0.j -0.125+0.j  0.125+0.j
        0.125+0.j -0.125+0.j]
        [ 0.125+0.j -0.125-0.j -0.125-0.j  0.125+0.j  0.125+0.j -0.125-0.j
        -0.125-0.j  0.125+0.j]
        [ 0.125+0.j -0.125-0.j -0.125-0.j  0.125+0.j  0.125+0.j -0.125-0.j
        -0.125-0.j  0.125+0.j]
        [-0.125+0.j  0.125+0.j  0.125+0.j -0.125+0.j -0.125+0.j  0.125+0.j
        0.125+0.j -0.125+0.j]
        [-0.125+0.j  0.125+0.j  0.125+0.j -0.125+0.j -0.125+0.j  0.125+0.j
        0.125+0.j -0.125+0.j]
        [ 0.125+0.j -0.125-0.j -0.125-0.j  0.125+0.j  0.125+0.j -0.125-0.j
        -0.125-0.j  0.125+0.j]]

如果需要打印量子态的分布，可以使用 ``plot_state_city`` 接口，函数定义如下

    .. code-block:: python

        def plot_state_city(state_vector, title="", figsize=None, color=None, ax_real=None, ax_imag=None)

使用示例：

    .. code-block:: python

        from pyqpanda import *
        import numpy as np

        machine = CPUQVM()
        machine.set_configure(50, 50)
        machine.init_qvm()
        q = machine.qAlloc_many(4)
        c = machine.cAlloc_many(4)
        prog = QProg()
        prog.insert(X(q[1]))\
            .insert(T(q[0]))\
            .insert(RX(q[1], np.pi/2))\
            .insert(RZ(q[0], np.pi/4))
        machine.directly_run(prog)
        result = machine.get_qstate()
        plot_state_city(result)
        machine.finalize()

终端会通过matplot绘制具体的量子态分布如下

    .. image:: images/plot_state_city.png
        :align: center

对于密度矩阵，我们可以通过 ``plot_density_matrix`` 来打印密度矩阵，函数定义如下：

    .. code-block:: python

        def plot_density_matrix(density_matrix, xlabels=None, ylabels=None,
                                title=None, limits=None, phase_limits=None, fig=None, axis_vals=None,
                                threshold=None)

使用示例：

    .. code-block:: python

        from pyqpanda import *
        import numpy as np

        machine = CPUQVM()
        machine.set_configure(50, 50)
        machine.init_qvm()
        q = machine.qAlloc_many(4)
        c = machine.cAlloc_many(4)
        prog = QProg()
        prog.insert(X(q[1]))\
            .insert(H(q[0]))\
            .insert(H(q[1]))\
            .insert(T(q[2]))\
            .insert(RX(q[1], np.pi/2))\
            .insert(RY(q[3], np.pi/3))\
            .insert(RZ(q[0], np.pi/4))\
            .insert(RZ(q[1], np.pi))\
            .insert(RZ(q[2], np.pi))\
            .insert(RZ(q[3], np.pi))
        machine.directly_run(prog)
        result = machine.get_qstate()
        rho = state_to_density_matrix(result)
        plot_density_matrix(rho)
        machine.finalize()

终端会通过matplot绘制具体的密度矩阵分布如下：

    .. image:: images/state_to_density_matrix.png
        :width: 400
        :align: center

对于单个比特而言，有些情况下我们需要研究它的Bloch球运动轨迹，这个功能可以通过 ``plot_bloch_circuit`` 接口，函数定义如下：
 
    .. code-block:: python

        def plot_bloch_circuit(circuit,trace=True,saveas=None,fps=20,secs_per_gate=1)

使用代码示例：

    .. code-block:: python

        from pyqpanda import *
        import numpy as np

        machine = CPUQVM()
        machine.set_configure(50, 50)
        machine.init_qvm()
        q = machine.qAlloc_many(2)
        c = machine.cAlloc_many(2)
        cir = QCircuit()
        cir.insert(RX(q[0], np.pi/2)) \
            .insert(RZ(q[0], np.pi / 2)) \
            .insert(RZ(q[0], np.pi/6))\
            .insert(RY(q[0], np.pi/3))\
            .insert(RX(q[0], np.pi/9))
        plot_bloch_circuit(cir)
        machine.finalize()

终端会动态展示单个量子比特线路的Bloch轨迹如下：

    .. image:: images/bolch_cir.jpg
        :width: 300
        :align: center

在运行一个量子线路得到概率分布后，可以通过 ``draw_probaility`` 或 ``draw_probaility_dict`` 绘制具体的概率分布，
他们的区别是第一个函数参数是dict类型，包含量子态二进制表示与对应的概率，另一个函数参数是list，表示量子态概率数组，运行示例如下：

    .. code-block:: python

        from pyqpanda import *
        import numpy as np

        machine = CPUQVM()
        machine.init_qvm()
        qubits = machine.qAlloc_many(3)

        prog = QProg()
        prog << Z(qubits[0])\
            << X1(qubits[1])\
            << H(qubits[:2])

        machine.directly_run(prog)
        result_dict = machine.prob_run_dict(prog, qubits, -1)
        draw_probaility_dict(result_dict)
        machine.finalize()

绘制的概率分布图如下：

    .. image:: images/draw_probaility_dict.png
        :width: 300
        :align: center