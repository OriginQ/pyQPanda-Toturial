.. _本源量子计算云平台官网: https://qcode.qubitonline.cn/QCode/index.html

.. _OriginIR介绍:

OriginIR
=======================

OriginIR是基于QPanda的量子程序中间表示，对QPanda各种特性的支持有非常重要的作用。OriginIR不仅可以表示绝大部分量子逻辑门类型，表示针对量子线路的dagger操作，为量子线路添加控制比特，还可以支持QPanda独有的Qif、QWhile，可以实现量子程序内嵌经典程序。

OriginIR主要内容有量子比特、经典寄存器、量子逻辑门、转置共轭操作、添加控制比特操作、QIf、QWhile、经典表达式。

量子比特
---------

OriginIR使用QINIT申请量子比特，其格式为QINIT后跟空格+量子比特总数。示例：QINIT 6。需要注意的是除注释外QINIT必须出现在OriginIR程序的第一行。
在使用量子比特时，OriginIR使用q[i]表示某个具体的量子比特，此处i为量子比特的编号，i可为无符号数字型常量，也可为变量，同时也可使用c[i]组成的表达式代替，示例：q[1],q[c[0]],q[c[1]+c[2]+c[3]]。

经典寄存器
-----------

OriginIR使用CREG申请经典寄存器，其格式为CREG后跟空格+经典寄存器总数。示例：CREG 6；
在使用经典寄存器时，OriginIR使用c[i]表示某个具体的经典寄存器，i为经典寄存器编号，此处i必须为无符号数字型常量；示例：c[1]。

量子逻辑门 
-----------

OriginIR把量子逻辑门分为以下几个种类：单门无参数型关键字；单门一个参数型；单门两个参数；单门三个参数；单门四个参数；双门无参数；双门一个参数；双门四个参数；三门无参数。
需要注意的是所有单门操作，目标量子比特可以是整个量子比特数组或者单个量子比特。如果是整个量子比特数组时例如：
::
    H q

当量子比特数组大小为3时则等效为：
::
    H q[0]
    H q[1]
    H q[2]

1、单门无参数型关键字：H、T、S、X、Y、Z、X1、Y1、Z1、I；表示无参数类型的单量子逻辑门；格式为量子逻辑门关键字+空格+目标量子比特。示例：

::

    H q[0]

2、单门一个参数型关键字：RX、RY、RZ、U1；表示有一个参数的单量子逻辑门；格式为量子逻辑门关键字+空格+目标量子比特+逗号+(偏转角度)。示例：

::

    RX q[0],(1.570796)

3、	单门两个参数型关键字：U2、RPhi；表示有两个参数的单量子逻辑门；格式为量子逻辑门关键字+空格+目标量子比特+逗号+（两个偏转角度）。示例：

::

    U2 q[0],(1.570796,-3.141593)

4、	单门三个参数型关键字：U3；表示有三个参数的单量子逻辑门；格式为量子逻辑门关键字+空格+目标量子比特+逗号+（三个偏转角度）。示例：

::

    U3 q[0],(1.570796,4.712389,1.570796)


5、单门四个参数关键字：U4；表示有四个参数的单量子逻辑门；格式为量子逻辑门关键字+空格+目标量子比特+逗号+（四个偏转角度）。示例：

::

    U4 q[1],(3.141593,4.712389,1.570796,-3.141593)

6、双门无参数型关键字：CNOT、CZ、ISWAP、SQISWAP、SWAP；表示无参数的双量子逻辑门；格式为量子逻辑门关键字+空格+控制比特+逗号+目标比特。示例：

::

    CNOT q[0],q[1]

7、双门一个参数型关键字：ISWAPTHETA、CR；表示有一个参数的单量子逻辑门；格式为量子逻辑门关键字+空格+控制比特+逗号+目标比特+逗号+(偏转角度)。示例：

::

    CR q[0],q[1],(1.570796)

8、双门四个参数型关键字：CU；表示有四个参数的单量子逻辑门；格式为量子逻辑门关键字+空格+控制比特+逗号+目标比特+逗号+（四个偏转角度）。示例：

::

    CU q[1],q[3],(3.141593,4.712389,1.570796,-3.141593)

9、	三门无参数型关键字：TOFFOLI；表示无参数的三量子逻辑门；格式为量子逻辑门关键字+空格+控制比特1+逗号+控制比特2+逗号+目标比特。示例：

::

    TOFFOLI  q[0],q[1],q[2]


转置共轭操作
-----------

OriginIR中可以对一个或多个量子逻辑门进行转置共轭操作，OriginIR使用DAGGER和
ENDDAGGER关键字定义转置共轭操作的范围，一个DAGGER必须有一个ENDDAGGER匹配，示例：

::

    DAGGER
    H q[0]
    CNOT q[0],q[1]
    ENDDAGGER


添加控制比特操作
-----------

OriginIR中可以对一个或多个量子逻辑门添加控制比特，OriginIR使用CONTROL 和
ENDCONTROL关键字定义添加控制比特的范围，CONTROL后跟空格+控制比特列表；示例：

::

    CONTROL q[2],q[3]
    H q[0]
    CNOT q[0],q[1]
    ENDCONTROL


QIF
:::

OriginIR中可以表示量子条件判断程序，它通过QIF、ELSE、ENDIF框定量子条件判断程序的不同分支的范围。QIF必须匹配一个ENDIF，如果QIF有两个分支则需要有ELSE，如果QIF只有一个分支则不需要有ELSE；QIF后跟空格+判断表达式。示例：

::

    1、QIF只有一个条件分支
    QIF c[0]==c[1]
    H q[0]
    CNOT q[0],q[1]
    ENDIF

    2、QIF有两个条件分支
    QIF c[0]+c[1]<5
    H q[0]
    CNOT q[0],q[1]
    ELSE
    H q[0]
    X q[1]
    ENDIF

QWHILE
::::::

OriginIR中可以表示量子循环判断程序，它通过QWHILE和ENDQWHILE框定循环判断程序的范围，QWHILE必须匹配一个ENDQWHILE；QWHILE后跟空格+判断表达式。示例：

::

    QWHILE c[0]<5
    H q[c[0]]
    c[0]=c[0]+1
    ENDQWHILE
    
经典表达式
-----------

OriginIR可以在量子程序中嵌入经典表达式，如c[0]==c[1]+c[2]；使用示例：

::

    QWHILE c[0]<5
    H q[c[0]]
    c[0]=c[0]+1
    ENDQWHILE

该示例表示对q[0]~q[4]比特做H门操作；经典表达式中必须是经典寄存器和常量组成的表达式；经典表达式的操作符有

::

        {PLUS , "+"},
        {MINUS, "-"},
        {MUL, "*"},
        {DIV, "/"},
        {EQUAL, "==" },
        { NE, "!=" },
        { GT, ">" },
        { EGT, ">=" },
        { LT, "<" },
        { ELT, "<=" },
        {AND, "&&"},
        {OR, "||"},
        {NOT, "!"},
        {ASSIGN, "=" }


MEASURE操作
-----------

MEASURE表示对指定的量子比特进行测量操作，并把结果保存到指定的经典寄存器中。MEASURE后跟空格+目标量子比特+‘，’+目标经典寄存器。示例：
::
    MEASURE q[0],c[0]
如果申请的量子比特和经典寄存器数量相同。可以使用q表示所有量子比特，c表示所有经典比特。示例：
::
    MEAUSRE q,c
如果量子比特和经典比特数量都为3，则等效为
::
    MEAUSRE q[0],c[0]
    MEAUSRE q[1],c[1]
    MEAUSRE q[2],c[2]


RESET操作
-----------

RESET操作是将操作的量子比特的量子态恢复到0态。格式为RESET+空格+目标量子比特。其中目标量子比特可以是整个量子比特数组或者单个量子比特。
示例：	
::
    RESET q

    RESET q[1]

BARRIER操作
-----------

BARRIER操作是将操作的量子比特进行阻断，防止在线路优化和执行过程。 
格式为BARRIER+空格+目标量子比特。其中目标量子比特可以是整个量子比特数组或者单个、多个量子比特。示例：	
::
    BARRIER q
    BARRIER q[0]
    BARRIER q[0],q[1],q[2]

QGATE操作
-----------
QGATE为自定义逻辑门操作，可以将多个逻辑门组合成一个新的逻辑门使用。
它通过QGATE和ENDQGATE框定自定义逻辑门的范围。同时需要注意的是，自定义逻辑门的形参名不能与上述相关关键字冲突。示例：
::
    QGATE new_H a
    H a
    X a
    ENDQGATE 
    new_H q[1]
    QGATE new_RX a,(b)
    RX a,(PI/2+b)
    X a
    ENDQGATE 
    new_RX q[1],(PI/4)


OriginIR程序示例
-----------

QPE算法

::

    QINIT 3
    CREG 2
    H q[2]
    H q[0]
    H q[1]
    CONTROL q[1]
    RX q[2],(-3.141593)
    ENDCONTROL
    CONTROL q[0]
    RX q[2],(-3.141593)
    RX q[2],(-3.141593)
    ENDCONTROL
    DAGGER
    H q[1]
    CR q[0],q[1],(1.570796)
    H q[0]
    ENDDAGGER
    MEASURE q[0],c[0]
    MEASURE q[1],c[1]


QPanda2提供了OriginIR转换工具接口 ``convert_qprog_to_originir`` 该接口使用非常简单。

.. function:: convert_qprog_to_originir(qprog: QProg, machine: QuantumMachine) -> str

    该函数用于将给定的量子程序转化为 OriginIR 格式的字符串，以便于进一步分析和处理。OriginIR 是一个中间表示（IR），用于表示量子程序的信息。

    :param qprog: 要转化的量子程序。
    :type qprog: QProg
    :param machine: 用于转化的量子机器。
    :type machine: QuantumMachine
    :return: 转化后的 OriginIR 格式的字符串。
    :rtype: str

    该函数接受一个量子程序和一个量子机器作为参数，然后将给定的量子程序转化为 OriginIR 格式的字符串。

    示例用法::

        # 创建一个量子机器和一个量子程序
        machine = CPUQVM()
        qvm.init_qvm()

        qprog = QProg()

        # 将量子程序转化为 OriginIR 格式的字符串
        originir_str = convert_qprog_to_originir(qprog, machine)

        # 打印转化后的 OriginIR 字符串
        print(originir_str)

下面的例程通过简单的接口调用演示了量子程序转化OriginIR的过程

    .. code-block:: python

        from pyqpanda import *

        if __name__ == "__main__":

            machine = CPUQVM()
            machine.init_qvm()
            qlist = machine.qAlloc_many(4)
            clist = machine.cAlloc_many(4)
            prog = QProg()
            prog_cir = QCircuit()

            # 构建量子线路
            prog_cir << Y(qlist[2]) << H(qlist[2]) << CNOT(qlist[0],qlist[1])


            # 构建量子程序
            prog << H(qlist[2]) << Measure(qlist[1],clist[1])
            
            # 量子程序转换QriginIR，并打印OriginIR
            print(convert_qprog_to_originir(prog,machine))
            


具体步骤如下:

 - 首先在主程序中用 ``init_quantum_machine`` 初始化一个量子虚拟机对象，用于管理后续一系列行为

 - 接着用 ``qAlloc_many`` 和 ``cAlloc_many`` 初始化量子比特与经典寄存器数目

 - 然后调用 ``create_empty_qprog`` 构建量子程序

 - 最后调用接口 ``convert_qprog_to_originir`` 输出OriginIR字符串，并用 ``destroy_quantum_machine`` 释放系统资源

运行结果如下：

    .. code-block:: python

        QINIT 4
        CREG 4
        H q[2]
        MEASURE q[1],c[1]


.. note:: 对于暂不支持的操作类型，OriginIR会显示UnSupported XXXNode，其中XXX为具体的节点类型。



