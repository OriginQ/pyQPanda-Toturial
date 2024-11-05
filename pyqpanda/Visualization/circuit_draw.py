from pyqpanda import circuit_layer
from pyqpanda import draw_qprog_text
from pyqpanda import draw_qprog_latex
from pyqpanda import fit_to_gbk
from pyqpanda import count_prog_info
from .matplotlib_draw import *


def draw_circuit_pic(prog, pic_name, scale = 0.7,verbose=False,fold = 30):
    """
    Draws a visual representation of a quantum circuit based on a given program.

    Args:
        prog (dict): 
            The quantum program that specifies the quantum circuit.
        pic_name (str): 
            The name of the output file for the circuit picture.
        scale (float, optional): 
            The scale factor for the circuit drawing. Defaults to 0.7.
        verbose (bool, optional): 
            If set to True, prints additional information during the drawing process. Defaults to False.
        fold (int, optional): 
            The number of folds to apply when drawing the circuit. Defaults to 30.

    The function utilizes the MatplotlibDrawer class to create the circuit image, which is then saved to the specified file. The drawer is configured with quantum register information, classical register information, and the operations defined in the program. The scale and fold parameters influence the visual presentation of the circuit.
    """
    layer_info = circuit_layer(prog)
    qcd = MatplotlibDrawer(
        qregs=layer_info[1], cregs=layer_info[2], ops=layer_info[0], scale = scale,fold = fold)
    qcd.draw(pic_name, verbose)


def draw_qprog(prog, output=None, scale=0.7, fold =30, filename=None, with_logo=False, line_length=100, NodeIter_first=None,
               NodeIter_second=None, console_encode_type='utf8'):
    """
    Visualizes a quantum circuit in various formats based on the specified output type.

    Supported output formats include:
    - 'text': ASCII art representation suitable for console output.
    - 'pic': Colorful image representation rendered in Python.
    - 'latex': LaTeX source code for the circuit, suitable for inclusion in LaTeX documents.

    Args:
        prog (object): 
            The quantum circuit object to be visualized.
        scale (float, optional): 
            The scale factor for the image output. Defaults to 0.7.
        fold (int, optional): 
            The maximum fold size for the image output. Defaults to 30.
        filename (str, optional): 
            The file path to save the image output. Defaults to 'QCircuit_pic.jpg' for 'pic' output.
            For 'latex' output, defaults to 'QCircuit_latex.tex'.
        with_logo (bool, optional): 
            Include the pyQPanda logo in the LaTeX output. Defaults to False.
        line_length (int, optional): 
            The length of each line in the ASCII art output. Defaults to 100.
        NodeIter_first (object, optional): 
            The starting position of the circuit segment to be visualized.
        NodeIter_second (object, optional): 
            The ending position of the circuit segment to be visualized.
        console_encode_type (str, optional): 
            The console encoding type, with 'utf8' and 'gbk' supported.
            Defaults to 'utf8'.

    Returns:
        str: 
            The visual representation of the quantum circuit, which is returned as a string depending on the output format.
    """
    default_output = 'text'
    if output is None:
        output = default_output

    text_pic = 'null'
    if output == 'pic':
        if filename is None:
            filename = 'QCircuit_pic.jpg'
        draw_circuit_pic(prog,filename,scale,fold = fold)
    elif output == 'text':
        if filename is None:
            filename = ''
        if NodeIter_first is None and NodeIter_second is None:
            text_pic = draw_qprog_text(prog, line_length, filename)
        elif NodeIter_first is None:
            text_pic = draw_qprog_text(
                prog, line_length, filename, prog.begin(), NodeIter_second)
        elif NodeIter_second is None:
            text_pic = draw_qprog_text(
                prog, line_length, filename, NodeIter_first, prog.end())

        if console_encode_type == 'gbk':
            text_pic = fit_to_gbk(text_pic)

        # print(text_pic)
    elif output == 'latex':
        if filename is None:
            filename = 'QCircuit_latex.tex'
        if NodeIter_first is None and NodeIter_second is None:
            text_pic = draw_qprog_latex(
                prog, line_length, filename, with_logo)
        elif NodeIter_first is None:
            text_pic = draw_qprog_latex(
                prog, line_length, filename, with_logo, prog.begin(), NodeIter_second)
        elif NodeIter_second is None:
            text_pic = draw_qprog_latex(
                prog, line_length, filename, with_logo, NodeIter_first, prog.end())

    return text_pic

def show_prog_info_count(prog):
    """
    Visualizes the distribution of nodes and layers within a quantum circuit represented by `prog`.

    This function creates a pie chart to display the proportion of different types of nodes and layers in
    the quantum circuit. It utilizes the information obtained from the `count_prog_info` function, which
    provides counts for single, double, and multi-control gate nodes, as well as layer-related metrics.

    Args:
        prog (object): 
            The quantum circuit object for which the distribution is to be visualized.

    Returns:
        None: 
            This function does not return any value; it only displays the visualization.

    The visualization is composed of two pie charts:
        The first chart shows the distribution of node types: Single Gate, Double Gate, Multi Control Gate, and Other Nodes.
        The second chart illustrates the distribution of layer types: Single Gate Layer, Double Gate Layer, and Other Layers.

    Note: 
        This function assumes that the `count_prog_info` function is properly implemented and that the
        `prog` object has the necessary attributes to compute the required counts.
    """
    info_count = count_prog_info(prog)

    labels_node = ['Single Gate Node', 'Double Gate Node', 'Multi Control Gate Node', 'Other Nodes']
    sizes_node = [info_count.single_gate_num, 
                  info_count.double_gate_num, 
                  info_count.multi_control_gate_num, 
                  info_count.node_num - info_count.single_gate_num - info_count.double_gate_num - info_count.multi_control_gate_num]

    labels_layer = ['Single Gate Layer', 'Double Gate Layer', 'Other Layers']
    sizes_layer = [info_count.single_gate_layer_num, info_count.double_gate_layer_num, info_count.layer_num - info_count.single_gate_layer_num - info_count.double_gate_layer_num]

    fig, axes = plt.subplots(nrows=2, figsize=(6, 8))
    plt.subplots_adjust(hspace=0.2)

    total_node_num = info_count.node_num
    wedges_node, texts_node, autotexts_node = axes[0].pie(sizes_node, labels=labels_node, autopct='%.1f%%', startangle=140, wedgeprops={'linewidth': 1, 'edgecolor': 'white'})
    axes[0].set_title(f'Total Nodes Distribution (Total Nodes: {total_node_num})', fontsize=14)
    axes[0].set_aspect('equal')

    for i, (label, size) in enumerate(zip(labels_node, sizes_node)):
        texts_node[i].set_text(f'{label} ({size})')

    total_layer_num = info_count.layer_num
    wedges_layer, texts_layer, autotexts_layer = axes[1].pie(sizes_layer, labels=labels_layer, autopct='%.1f%%', startangle=140, wedgeprops={'linewidth': 1, 'edgecolor': 'white'})
    axes[1].set_title(f'Total Layers Distribution (Total Layers: {total_layer_num})', fontsize=14)
    axes[1].set_aspect('equal')

    for i, (label, size) in enumerate(zip(labels_layer, sizes_layer)):
        texts_layer[i].set_text(f'{label} ({size})')

    plt.show()
    