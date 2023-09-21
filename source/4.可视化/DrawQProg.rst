量子线路可视化
====================

量子线路可视化是一个用于呈现和分析量子电路的工具，它在量子计算和量子信息领域扮演着重要角色。

量子线路可视化的主要目的是通过图形化表示来理解和研究量子电路。通过直观的图像，可以更清楚地看到量子比特之间的相互作用、量子门的顺序以及量子算法的结构。

根据常用的使用场景，可视化输出主要分为 **控制台终端打印** 和 **输出为图片** 等两大部分。

在控制台输出中，我们使用文本字符来模拟量子比特和量子门操作。
每个量子比特通常用一个小方框或者是一个字母来表示，而量子门操作则以其代表的操作名称缩写来表示，比如用"H"表示Hadamard门，用"CNOT"表示控制非门等。

量子比特之间的连接关系通过使用空格、竖线和斜线等特殊字符，例如，如果一个量子门操作作用在两个量子比特之间，我们可以在这两个量子比特之间画一条连线来表示它们之间的相互作用。这样可以清楚地看到量子比特之间是如何通过量子门进行信息交换和相互影响的。

pyqpanda中可以直接通过 ``print`` 和 ``draw_qprog`` 来输出和保存量子线路可视化结果

.. function:: draw_qprog(prog, output=None, scale=0.7, filename=None, with_logo=False, line_length=100, NodeIter_first=None, NodeIter_second=None, console_encode_type='utf8')

    draw_qprog提供了一个便捷的方式将量子线路以多种不同的视觉格式呈现，通过控制台格式化输出或保存量子线路函数，具体有以下功能
    
     - ``文本形式`` ：通过使用文本图案，在控制台中显示量子线路的结构和操作序列。这种呈现方式适用于快速的调试和查看，能够以简洁的方式展示量子比特之间的连接关系和操作顺序。

     - ``图像形式`` ：将量子线路绘制成图像，提供了更丰富的视觉信息。用户可以选择不同的图像输出格式，如PNG或SVG，以适应不同的用途。图像展示适合用于演示、教学和文档编写，可以突出量子比特之间的连接关系、量子门操作的分布以及线路的整体结构。

     - ``LaTeX源代码形式`` ：将量子线路转换为LaTeX源代码，使用户能够方便地将量子线路嵌入到LaTeX文档中。这对于学术论文、技术报告和课件制作非常有用。用户可以在文档中无缝地插入量子线路图，与其他数学和物理公式相结合，从而形成一体化的呈现方式。

    :param prog: 要绘制的量子线路。
    :type prog: QuantumCircuit
    :param output: 指定绘制的输出格式，可选值为 "text"、"pic" 或 "latex"。默认为 None。
    :type output: str, optional
    :param scale: 绘制图像的缩放比例（如果小于1则缩小），仅在“pic”输出格式下使用。默认为 0.7。
    :type scale: float, optional
    :param filename: 保存图像的文件路径，默认为 None。
    :type filename: str, optional
    :param with_logo: 是否在图像中包含标识，仅在“pic”输出格式下使用。默认为 False。
    :type with_logo: bool, optional
    :param NodeIter_first: 电路绘制的起始位置。默认为 None。
    :type NodeIter_first: int, optional
    :param NodeIter_second: 电路绘制的结束位置。默认为 None。
    :type NodeIter_second: int, optional
    :param console_encode_type: 目标控制台编码类型，支持 'utf8' 和 'gbk'，仅在“pic”输出格式下使用。默认为 'utf8'。
    :type console_encode_type: str, optional
    :param line_length: 设置“text”输出类型生成的行长度。默认为 100。
    :type line_length: int, optional
    :return: 无返回值。
    :rtype: None

    :示例:
        
    .. code:: python

        from numpy import pi
        from pyqpanda import *
        from pyqpanda.Visualization import circuit_draw

        machine = CPUQVM()
        machine.init_qvm()

        qlist = machine.qAlloc_many(4)
        clist = machine.cAlloc_many(4)

        measure_prog = QProg()
        measure_prog << hadamard_circuit(qlist) \
        << CZ(qlist[1], qlist[2]) \
        << RX(qlist[2], pi / 4) \
        << RX(qlist[1], pi / 4) \
        << CNOT(qlist[0], qlist[2]) \
        << Measure(qlist[0], clist[0]) 

        print(measure_prog)

    对于上面的一段量子程序，可以直接通过 ``print`` 输出到控制台

    .. code:: python

        # 通过print直接输出量子线路字符画，该方法会在控制台输出量子线路，输出格式为utf8编码，所以在非utf8编码的控制台下，输出字符画会出现乱码情况。
        # 同时，该方法会将当前量子线路字符画信息保存到文件，文件名为 “QCircuitTextPic.txt”，文件用utf8编码，并保存在当面路径下面，
        # 所以用户也可以通过该文件查看量子线路信息，注意该文件要以uft8格式打开，否则会出现乱码。
        print(measure_prog)

    输出结果如下：

    .. figure:: ./images/draw_pic.png
       :width: 500
       :alt:

    对于需要保存为图片的使用场景，可以使用 ``draw_qprog`` 

    .. code:: python

        draw_qprog(measure_prog, 'pic', filename='D:/test_cir_draw.png')

    输出的量子线路图片效果如下：

    .. figure:: ./images/test_cir_draw.png
       :width: 500
       :alt: