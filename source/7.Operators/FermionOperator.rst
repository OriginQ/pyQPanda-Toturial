费米子算符类
==============

我们用如下的记号标识来表示费米子的两个形态，
湮没: :math:`X`  表示 :math:`a_x` ，
创建: :math:`X +` 表示 :math:`a_x^\dagger` ，
例如: "1 + 3 5 + 1"则代表 :math:`a_1^\dagger \ a_3 \ a_5^\dagger \ a_1`

整理规则如下

**1.** 不同数字

.. math:: ''1\quad 2'' = -1 * ''2\quad 1''
.. math:: ''1 + 2 +'' = -1 * ''2 + 1 +''
.. math:: ''1 + 2'' = -1 * ''2\quad 1 +''

**2.** 相同数字

.. math:: ''1\quad 1 + '' =  1 + ''1 + 1''
.. math:: ''1 + 1 + '' = 0
.. math:: ''1\quad 1'' = 0

跟 ``PauliOperator`` 类似，``FermionOperator`` 类也提供了费米子算符之间加、减和乘的基础的运算操作。通过整理功能可以得到一份有序排列的结果。

.. class:: FermionOperator

    费米子算符类，用于生成和操作费米子算符集合，主要用于量子化学等领域的模拟和计算。

    .. method:: __init__()

        初始化 FermionOperator 类的实例。

    .. method:: __init__(scalar: float)

        初始化 FermionOperator 类的实例。

        :param scalar: 标量值。
        :type scalar: float

    .. method:: __init__(scalar: complex)

        初始化 FermionOperator 类的实例。

        :param scalar: 复数标量值。
        :type scalar: complex

    .. method:: __init__(term: str, scalar: complex)

        初始化 FermionOperator 类的实例。

        :param term: 项的标识字符串，表示费米子项。
        :type term: str
        :param scalar: 复数标量值。
        :type scalar: complex

    .. method:: __init__(terms: Dict[str, complex])

        初始化 FermionOperator 类的实例。

        :param terms: 复数标量值和项的字典，键为项的标识字符串。
        :type terms: Dict[str, complex]

    .. method:: data() -> List[Tuple[Tuple[List[Tuple[int, bool]], str], complex]]

        获取费米子算符数据。

        :return: 包含费米子项的列表，每个元组为一项，包含项的信息和复数标量值。
        :rtype: List[Tuple[Tuple[List[Tuple[int, bool]], str], complex]]

    .. method:: error_threshold() -> float

        获取误差阈值。

        :return: 误差阈值。
        :rtype: float

    .. method:: isEmpty() -> bool

        判断费米子算符是否为空。

        :return: 如果费米子算符为空，则为 True，否则为 False。
        :rtype: bool

    .. method:: normal_ordered() -> FermionOperator

        对费米子算符进行正则排序。

        :return: 经过正则排序后的费米子算符。
        :rtype: FermionOperator

    .. method:: setErrorThreshold(threshold: float) -> None

        设置误差阈值。

        :param threshold: 误差阈值。
        :type threshold: float

    .. method:: toString() -> str

        获取费米子算符的字符串表示。

        :return: 费米子算符的字符串表示。
        :rtype: str

    .. method:: to_string() -> str

        获取费米子算符的字符串表示。

        :return: 费米子算符的字符串表示。
        :rtype: str

实例
--------------

.. code-block:: python

    from pyqpanda import *
    
    if __name__=="__main__":

        a = FermionOperator("0 1+", 2)
        b = FermionOperator("2+ 3", 3)

        plus = a + b
        minus = a - b
        muliply = a * b

        print("a + b = ", plus)
        print("a - b = ", minus)
        print("a * b = ", muliply)

        print("normal_ordered(a + b) = ", plus.normal_ordered())
        print("normal_ordered(a - b) = ", minus.normal_ordered())
        print("normal_ordered(a * b) = ", muliply.normal_ordered())

.. code-block:: python

    a + b =  {
    0 1+ : 2.000000
    2+ 3 : 3.000000
    }

    a - b =  {
    0 1+ : 2.000000
    2+ 3  : -3.000000
    }

    a * b =  {
    0 1+ 2+ 3 : 6.000000
    }

    normal_ordered(a + b) =  {
    1+ 0 : -2.000000
    2+ 3 : 3.000000
    }

    normal_ordered(a - b) =  {
    1+ 0 : -2.000000
    2+ 3  : -3.000000
    }

    normal_ordered(a * b) =  {
    2+ 1+ 3 0 : 6.000000      
    }