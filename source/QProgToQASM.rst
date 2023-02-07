量子程序转化QASM
=====================
----

通过该功能模块，你可以解析通过QPanda2构建的量子程序，将其中包含的量子比特信息以及量子逻辑门操作信息提取出来，得到按固定格式存储的QASM指令集。

.. _QASM介绍:

QASM介绍
>>>>>>>>>>>>>>>
----

QASM(Quantum Assembly Language)是IBM公司提出的量子汇编语言，与 :ref:`QRunes介绍` 中的语法规则类似，一段QASM代码如下所示：

    :: 

        OPENQASM 2.0;
        include "qelib1.inc";
        qreg q[10];
        creg c[10];

        x q[0];
        h q[1];
        tdg q[2];
        sdg q[2];
        cx q[0],q[2];
        cx q[1],q[4];
        u1(pi) q[0];
        u2(pi,pi) q[1];
        u3(pi,pi,pi) q[2];
        cz q[2],q[5];
        ccx q[3],q[4],q[6];
        cu3(pi,pi,pi) q[0],q[1];
        measure q[2] -> c[2];
        measure q[0] -> c[0];


需要注意的是，QASM的语法格式与QRunes形相似而神不同，主要区别有以下几点:

 - QRunes对于需要进行转置共轭操作的量子逻辑门与量子线路，需要将目标置于DAGGER与ENDAGGER语句之间，而QASM会直接进行转化。
 - QRunes支持对量子逻辑门与量子线路施加控制操作，而QASM不支持，在对量子程序转化QASM指令集之前，会对其中包含的控制操作进行分解。


QPanda2提供了QASM转换工具接口 ``convert_qprog_to_qasm`` 该接口使用非常简单，具体可参考下方示例程序。

实例
>>>>>>>>>>>>>>
----

下面的例程通过简单的接口调用演示了量子程序转化QASM指令集的过程

    .. code-block:: python

        from pyqpanda import *

        if __name__ == "__main__":
            qvm = CPUQVM()
            qvm.init_qvm()
            q = qvm.qAlloc_many(6)
            c = qvm.cAlloc_many(6)
            prog = QProg()
            cir = QCircuit()
            cir << T(q[0]) << S(q[1]) << CNOT(q[1], q[0])
            prog << cir
            prog << X(q[0]) << Y(q[1]) << CU(1.2345, 3, 4, 5, q[5], q[2])\
                << H(q[2]) << RX(q[3], 3.14)\
                << Measure(q[0], c[0])
            
            qasm = convert_qprog_to_qasm(prog, qvm)
            print(qasm)


具体步骤如下:

 - 首先在主程序中用 ``init_quantum_machine`` 初始化一个量子虚拟机对象，用于管理后续一系列行为。

 - 接着用 ``qAlloc_many`` 和 ``cAlloc_many`` 初始化量子比特与经典寄存器数目。

 - 然后调用 ``QProg`` 构建量子程序。

 - 最后调用接口 ``convert_qprog_to_qasm`` 输出QASM指令集。``finalize()`` 用于释放系统资源。


运行结果如下：

    .. code-block:: python

        OPENQASM 2.0;
        include "qelib1.inc";
        qreg q[6];
        creg c[6];
        u3(0,0.78539816339744828,0) q[0];
        u3(0,1.5707963267948966,0) q[1];
        cx q[1],q[0];
        u3(3.1415926535897931,0,3.1415926535897931) q[0];
        u3(3.1415926535897931,0,0) q[1];
        u3(0,-0.33629632679489674,0) q[5];
        u3(1.5707963267948968,0,2.4689999999999994) q[2];
        cz q[5],q[2];
        u3(0.33629632679489924,-1.5707963267948966,1.5707963267948966) q[2];
        cz q[5],q[2];
        u3(1.1586360625022274,0.30011082466761058,-0.12333631564044467) q[2];
        u3(0,1.5707963267948963,0) q[5];
        cz q[5],q[2];
        u3(1.4173486819813736,2.7391542832240892,-1.915529794610245) q[2];
        cz q[5],q[2];
        u3(1.8052963267948967,-1.5707963267948966,1.5707963267948966) q[2];
        u3(3.1400000000000001,-1.5707963267948966,1.5707963267948966) q[3];
        measure q[0] -> c[0];

