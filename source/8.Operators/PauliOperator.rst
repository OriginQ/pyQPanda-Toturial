泡利算符类
============================

泡利算符是一组三个2×2的幺正厄米复矩阵，又称酉矩阵。我们一般都以希腊字母 :math:`\sigma`  （西格玛）来表示，记作 :math:`\sigma_x` ，:math:`\sigma_y` ，:math:`\sigma_Z` 。
在 ``QPanda`` 中我们称它们为 :math:`X`  门，:math:`Y` 门，:math:`Z` 门。
它们对应的矩阵形式如下表所示。

.. |X| image:: ./images/QGate_X.png
   :width: 50px
   :height: 50px

.. |Y| image:: ./images/QGate_Y.png
   :width: 50px
   :height: 50px
   
.. |Z| image:: ./images/QGate_Z.png
   :width: 50px
   :height: 50px

====================== ======================= ==========================================================================
| |X|                       | :math:`\sigma_x`                 | :math:`\begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}\quad`
| |Y|                       | :math:`\sigma_y`                 | :math:`\begin{bmatrix} 0 & -i \\ i & 0 \end{bmatrix}\quad`
| |Z|                       | :math:`\sigma_z`                 | :math:`\begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}\quad`
====================== ======================= ==========================================================================

泡利算符的运算规则如下：

**1.** 泡利算符与自身相乘得到是单位矩阵

.. math:: \sigma_x\sigma_x = I
.. math:: \sigma_y\sigma_y = I
.. math:: \sigma_z\sigma_z = I

**2.** 泡利算符与单位矩阵相乘，无论是左乘还是右乘，其值不变

.. math:: \sigma_xI = I\sigma_x = \sigma_x 
.. math:: \sigma_yI = I\sigma_y = \sigma_y 
.. math:: \sigma_zI = I\sigma_z = \sigma_z 

**3.** 顺序相乘的两个泡利算符跟未参与计算的泡利算符是 :math:`i` 倍的关系

.. math:: \sigma_x\sigma_y = i\sigma_z
.. math:: \sigma_y\sigma_z = i\sigma_x
.. math:: \sigma_z\sigma_x = i\sigma_y

**4.** 逆序相乘的两个泡利算符跟未参与计算的泡利算符是 :math:`-i` 倍的关系

.. math:: \sigma_y\sigma_x = -i\sigma_z
.. math:: \sigma_z\sigma_y = -i\sigma_x
.. math:: \sigma_x\sigma_z = -i\sigma_y


模块介绍
-------------

.. class:: PauliOperator

    Pauli 算符类
    ============

    该类实现了生成和操作 Pauli 算符集合的功能，用于表示量子哈密顿量或量子操作。Pauli 算符是由 Pauli 矩阵组成的线性组合，常用于描述量子系统的演化和能级。

    .. method:: __init__()

        初始化 PauliOperator 类实例。

    .. method:: __init__(value: complex)

        初始化 PauliOperator 类实例，给定复数值。

        :param value: 复数值。
        :type value: complex

    .. method:: __init__(matrix: numpy.ndarray, is_reduce_duplicates: bool = False)

        初始化 PauliOperator 类实例，给定矩阵表示。

        :param matrix: 表示 Pauli 算符的矩阵，要求为 numpy.ndarray[numpy.float64[m, n]] 类型。
        :type matrix: numpy.ndarray
        :param is_reduce_duplicates: 是否进行重复项削减。默认为 False。
        :type is_reduce_duplicates: bool, optional

    .. method:: __init__(key: str, value: complex, is_reduce_duplicates: bool = False)

        初始化 PauliOperator 类实例，给定键值对。

        :param key: 代表 Pauli 算符的字符串键。
        :type key: str
        :param value: 复数值。
        :type value: complex
        :param is_reduce_duplicates: 是否进行重复项削减。默认为 False。
        :type is_reduce_duplicates: bool, optional

    .. method:: __init__(pauli_map: Dict[str, complex], is_reduce_duplicates: bool = False)

        初始化 PauliOperator 类实例，给定 Pauli 算符字典。

        :param pauli_map: 包含 Pauli 算符键值对的字典。
        :type pauli_map: Dict[str, complex]
        :param is_reduce_duplicates: 是否进行重复项削减。默认为 False。
        :type is_reduce_duplicates: bool, optional

    .. method:: dagger() -> PauliOperator

        返回 Pauli 算符的共轭转置。

        :return: Pauli 算符的共轭转置。
        :rtype: PauliOperator

    .. method:: data() -> List[Tuple[Tuple[Dict[int, str], str], complex]]

        返回 Pauli 算符数据的列表形式。

        :return: 包含 Pauli 算符数据的列表，每个元组包含表示和复数值。
        :rtype: List[Tuple[Tuple[Dict[int, str], str], complex]]

    .. method:: error_threshold() -> float

        返回 Pauli 算符的错误阈值。

        :return: Pauli 算符的错误阈值。
        :rtype: float

    .. method:: getMaxIndex() -> int

        返回 Pauli 算符最大索引，下标从0开始

        :return: Pauli 算符最大索引。
        :rtype: int

    .. method:: get_max_index() -> int

        返回 Pauli 算符最大索引，下标从0开始

        :return: Pauli 算符最大索引。
        :rtype: int

    .. method:: isAllPauliZorI() -> bool

        检查是否所有 Pauli 算符都是 Pauli-Z 或单位算符。

        :return: 若所有算符均为 Pauli-Z 或单位算符则返回 True，否则返回 False。
        :rtype: bool

    .. method:: isEmpty() -> bool

        检查 Pauli 算符是否为空。

        :return: 若 Pauli 算符为空则返回 True，否则返回 False。
        :rtype: bool

    .. method:: is_all_pauli_z_or_i() -> bool

        检查是否所有 Pauli 算符都是 Pauli-Z 或单位算符。

        :return: 若所有算符均为 Pauli-Z 或单位算符则返回 True，否则返回 False。
        :rtype: bool

    .. method:: is_empty() -> bool

        检查 Pauli 算符是否为空。

        :return: 若 Pauli 算符为空则返回 True，否则返回 False。
        :rtype: bool

    .. method:: reduce_duplicates() -> None

        削减重复的 Pauli 算符项。

    .. method:: remapQubitIndex(remap_dict: Dict[int, int]) -> PauliOperator

        重新映射量子比特索引。

        :param remap_dict: 指定索引映射关系的字典。
        :type remap_dict: Dict[int, int]
        :return: 重新映射后的 Pauli 算符。
        :rtype: PauliOperator

    .. method:: remap_qubit_index(remap_dict: Dict[int, int]) -> PauliOperator

        重新映射量子比特索引。

        :param remap_dict: 指定索引映射关系的字典。
        :type remap_dict: Dict[int, int]
        :return: 重新映射后的 Pauli 算符。
        :rtype: PauliOperator

    .. method:: setErrorThreshold(threshold: float) -> None

        设置 Pauli 算符的错误阈值。

        :param threshold: 错误阈值。
        :type threshold: float

    .. method:: set_error_threshold(threshold: float) -> None

        设置 Pauli 算符的错误阈值。

        :param threshold: 错误阈值。
        :type threshold: float

    .. method:: toHamiltonian(sparse: bool) -> List[Tuple[Dict[int, str], float]]

        将 Pauli 算符转换为哈密顿量。

        :param sparse: 是否以稀疏矩阵形式表示哈密顿量。
        :type sparse: bool
        :return: 哈密顿量数据列表，每个元组包含表示和复数值。
        :rtype: List[Tuple[Dict[int, str], float]]

    .. method:: toString() -> str

        返回 Pauli 算符的字符串表示。

        :return: Pauli 算符的字符串表示。
        :rtype: str

    .. method:: to_hamiltonian(sparse: bool) -> List[Tuple[Dict[int, str], float]]

        将 Pauli 算符转换为哈密顿量。

        :param sparse: 是否以稀疏矩阵形式表示哈密顿量。
        :type sparse: bool
        :return: 哈密顿量数据列表，每个元组包含表示和复数值。
        :rtype: List[Tuple[Dict[int, str], float]]

    .. method:: to_matrix() -> numpy.ndarray

        返回 Pauli 算符的矩阵表示。

        :return: Pauli 算符的矩阵表示。
        :rtype: numpy.ndarray

    .. method:: to_string() -> str

        返回 Pauli 算符的字符串表示。

        :return: Pauli 算符的字符串表示。
        :rtype: str


我们可以很容易的通过各种方式构造泡利算符类，例如

.. code-block:: python

    from pyqpanda import *
    
    if __name__=="__main__":
        # 构造一个空的泡利算符类
        p1 = PauliOperator()

        # 2倍的"泡利Z0"张乘"泡利Z1"
        p2 = PauliOperator("Z0 Z1", 2)

        # 2倍的"泡利Z0"张乘"泡利Z1" + 3倍的"泡利X1"张乘"泡利Y2"
        p3 = PauliOperator({"Z0 Z1": 2, "X1 Y2": 3})
        
        # 构造一个单位矩阵，其系数为2，等价于p4 = PauliOperator("", 2)
        p4 = PauliOperator(2)

其中PauliOperator p2("Z0 Z1", 2)表示的是 :math:`2\sigma_{0}^{z}\otimes\sigma_{1}^{z}`。

.. note:: 
    
    构造泡利算符类的时候，字符串里面包含的字符只能是空格、 \\(X\\)、 \\(Y\\) 和 \\(Z\\)中的一个或多个，包含其它字符将会抛出异常。
    另外，同一个字符串里面同一泡利算符的比特索引不能相同，例如：PauliOperator("Z0 Z0", 2)将会抛出异常。

泡利算符类之间可以做加、减、乘等操作，计算返回结果还是一个泡利算符类。

.. code-block:: python

    a = PauliOperator("Z0 Z1", 2)
    b = PauliOperator("X5 Y6", 3)

    plus = a + b
    minus = a - b
    muliply = a * b

泡利算符类支持打印功能，我们可以将泡利算符类打印输出到屏幕上，方便查看其值。

.. code-block:: python

    a = PauliOperator("Z0 Z1", 2)
    
    print(a)

我们在实际使用的时候，常常需要知道该泡利算符类操作了多少个量子比特，这时候我们通过调用泡利算符类getMaxIndex接口即可得到。
如果是空的泡利算符类调用getMaxIndex接口则返回0，否则返回其最大下标索引值加1的结果。

.. code-block:: python

    a = PauliOperator("Z0 Z1", 2)
    b = PauliOperator("X5 Y6", 3)
    
    # 输出的值为1
    print(a.getMaxIndex())
    # 输出的值为6
    print(b.getMaxIndex())

如果我们构造的的泡利算符类，其中泡利算符的下标索引不是从0开始分配的，例如PauliOperator("X5 Y6", 3)调用getMaxIndex接口返回的使用的比特数是7，其实
只使用了2个比特。我们如何才能返回其真实用到的比特数呢。我们可以调用泡利算符类里面remapQubitIndex接口，它的功能是对泡利算符类中的索引从0比特开始分配映射，
并返回新的泡利算符类，该接口需要传入一个map来保存前后下标的映射关系。

.. code-block:: python

    b = PauliOperator("X5 Y6", 3)

    index_map = {}
    a = b.remapQubitIndex(index_map)
    
    # 输出的值为 6
    print(b.getMaxIndex())
    # 输出的值为 1
    print(a.getMaxIndex())


实例
-------------

以下实例主要是展示 ``PauliOperator`` 接口的使用方式。

.. code-block:: python
    
    from pyqpanda import *
    
    if __name__=="__main__":

        a = PauliOperator("Z0 Z1", 2)
        b = PauliOperator("X5 Y6", 3)

        plus = a + b
        minus = a - b
        muliply = a * b

        print("a + b = ", plus)
        print("a - b = ", minus)
        print("a * b = ", muliply)

        print("Index : ", muliply.getMaxIndex())

        index_map = {}
        remap_pauli = muliply.remapQubitIndex(index_map)

        print("remap_pauli : ", remap_pauli)
        print("Index : ", remap_pauli.getMaxIndex())

输出结果如下：
            
    .. code-block:: python

        a + b =  {
        "Z0 Z1" : 2.000000,
        "X5 Y6" : 3.000000
        }
        
        a - b =  {
        "Z0 Z1" : 2.000000,
        "X5 Y6" : -3.000000
        }

        a * b =  {
        "Z0 Z1 X5 Y6" : 6.000000
        }

        Index :  6
        remap_pauli :  {
        "Z0 Z1 X2 Y3" : 6.000000
        }

        Index :  3
