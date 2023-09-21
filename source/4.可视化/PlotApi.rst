密度矩阵
====================

对于一些低量子比特系统而言，能够展示整个系统的量子态分布、密度矩阵分布或者Bloch轨迹，对于算法研究有很大帮助。
pyqpanda提供了类似的功能接口。

对于量子态，可以通过 ``state_to_density_matrix`` 转化为密度矩阵，参数是 **量子态数组** ，可以参考如下示例。

.. function:: state_to_density_matrix(quantum_state)

    该函数用于将量子态转换为密度矩阵。

    :param quantum_state: 要转换的量子态，以复数列表形式表示。
    :type quantum_state: list of complex numbers
    :return: 密度矩阵。
    :rtype: numpy.ndarray

    :raises RuntimeError: 如果输入不是有效的量子态。

    一个简单的例子：

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


量子态分布
====================


如果需要打印量子态的分布，可以使用 ``plot_state_city`` 接口，函数定义如下

.. function:: plot_state_city(quantum_state, title="", figsize=None, color=None, ax_real=None, ax_imag=None)

    该函数用于绘制量子态的立体分布图。

    :param quantum_state: 要绘制城市图的量子态，应为复数列表。
    :type quantum_state: list of complex
    :param title: 图的标题，默认为空字符串。
    :type title: str, optional
    :param figsize: 图的尺寸，格式为 (宽度, 高度)，默认为 None。
    :type figsize: tuple, optional
    :param color: 图的颜色设置，默认为 None。
    :type color: str, optional
    :param ax_real: 用于绘制实部的 Matplotlib 坐标轴，默认为 None。
    :type ax_real: matplotlib.axes.Axes, optional
    :param ax_imag: 用于绘制虚部的 Matplotlib 坐标轴，默认为 None。
    :type ax_imag: matplotlib.axes.Axes, optional
    :return: Matplotlib 图形对象。
    :rtype: matplotlib.figure.Figure

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

    .. image:: ./images/plot_state_city.png
        :align: center

对于密度矩阵，我们可以通过 ``plot_density_matrix`` 来打印密度矩阵，函数定义如下：

.. function:: plot_density_matrix(M, xlabels=None, ylabels=None, title=None, limits=None, phase_limits=None, fig=None, axis_vals=None, threshold=None)

    该函数用于绘制给定量子态的密度矩阵图像，以直观地呈现量子态的结构和性质。

    :param M: 要绘制的量子态的复数列表（密度矩阵）。密度矩阵是量子力学中描述量子态的矩阵表示，包含了量子态的全部信息。
    :type M: list of complex
    :param xlabels: 用于自定义X轴标签的列表。每个标签对应密度矩阵的一列。默认为 None。
    :type xlabels: list, optional
    :param ylabels: 用于自定义Y轴标签的列表。每个标签对应密度矩阵的一行。默认为 None。
    :type ylabels: list, optional
    :param title: 图像的标题，用于指明图像的主题或特定含义。默认为 None。
    :type title: str, optional
    :param limits: 图像的显示范围，可控制颜色的映射范围。默认为 None。
    :type limits: tuple, optional
    :param phase_limits: 相位的显示范围，用于调整相位颜色的映射范围。默认为 None。
    :type phase_limits: tuple, optional
    :param fig: Matplotlib图像对象，用于在现有图像上绘制。默认为 None。
    :type fig: matplotlib.figure.Figure, optional
    :param axis_vals: 自定义轴的值，用于更改轴上的刻度值。默认为 None。
    :type axis_vals: list, optional
    :param threshold: 阈值，用于控制在图像中隐藏低于此值的元素。默认为 None。
    :type threshold: float, optional
    :return: Matplotlib图像对象，呈现了量子态的密度矩阵图像。
    :rtype: matplotlib.figure.Figure

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

    .. image:: ./images/state_to_density_matrix.png
        :width: 400
        :align: center

Bloch球轨迹
====================

对于单个比特而言，有些情况下我们需要研究它的Bloch球运动轨迹，这个功能可以通过 ``plot_bloch_circuit`` 接口，函数定义如下：
 
.. function:: plot_bloch_circuit(circuit, trace=True, saveas=None, fps=20, secs_per_gate=1)

    该函数用于绘制一个量子线路的 Bloch 球视图，仅支持单量子比特。

    :param circuit: 要绘制的量子线路。
    :type circuit: QuantumCircuit
    :param trace: 是否显示 Bloch 球轨迹。默认为 True。
    :type trace: bool, optional
    :param saveas: 保存图像的文件路径。默认为 None。
    :type saveas: str, optional
    :param fps: 动画的帧率。默认为 20。
    :type fps: int, optional
    :param secs_per_gate: 每个门操作的显示时间（秒）。默认为 1。
    :type secs_per_gate: int, optional
    :return: Bloch 球视图的图像。
    :rtype: Figure

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

    .. image:: ./images/bolch_cir.jpg
        :width: 300
        :align: center


概率分布
=========

在运行一个量子线路得到概率分布后，可以通过 ``draw_probaility`` 或 ``draw_probaility_dict`` 绘制具体的概率分布，
他们的区别是第一个函数参数是dict类型，包含量子态二进制表示与对应的概率，另一个函数参数是list，表示量子态概率数组，运行示例如下：

.. function:: draw_probability(probability_dict)

    该函数用于绘制量子态概率分布的字典。

    :param probability_dict: 要绘制的量子态概率分布字典，其中键是量子态，值是概率值。
    :type probability_dict: dict
    :return: 无返回值。
    :rtype: None

    一个简单的例子如下：
    
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

    .. image:: ./images/draw_probaility_dict.png
        :width: 300
        :align: center