更新日志
============

3.8.2 - 2024-01-05
--------------------

**新增功能和重要更新：**

1.量子计算服务适配了本源悟空芯片上线，并且可以支持originir量子程序参数， ``real_chip_type.origin_72`` 即为72比特芯片类型，使用方法可以参考 :ref:`真实芯片计算服务` 

    .. code-block:: python

        machine = QCloud()
        machine.set_configure(72,72);

        # online, xxx 替换为实际的用户api_token
        machine.init_qvm("XXX",False)

        qlist = machine.qAlloc_many(6)
        clist = machine.cAlloc_many(6)

        # 构建量子程序，可以手动输入，也可以来自OriginIR或QASM语法文件等
        measure_prog = QProg()
        measure_prog << H(qlist[0])\
                    << CNOT(qlist[0], qlist[1])\
                    << CNOT(qlist[1], qlist[2])\
                    << Measure(qlist[0], clist[0])\
                    << Measure(qlist[1], clist[1])\
                    << Measure(qlist[2], clist[2])

        batch_prog = [measure_prog for _ in range (6)]

        pmeasure_prog = QProg()
        pmeasure_prog << H(qlist[0])\
                    << CNOT(qlist[0], qlist[1])\
                    << CNOT(qlist[1], qlist[2])
        
        prog_string = convert_qprog_to_originir(measure_prog, machine)
        originir_list = [convert_qprog_to_originir(prog, machine) for prog in batch_prog]

        real_chip_measure_result = machine.real_chip_measure(measure_prog, 1000, real_chip_type.origin_72)
        originir_result =  machine.real_chip_measure(prog_string, 1000, real_chip_type.origin_72)

        print(real_chip_measure_result)
        print(originir_result)

2.ldd多控门分解接口( ``ldd_decompose`` )适配了RXX,RYY,RZX,RZZ,MS等特殊双门以及 ``QOracle`` 的受控形式，示例程序如下

    .. code-block:: python

        from pyqpanda import *
        from scipy.stats import unitary_group

        machine = CPUQVM()
        machine.init_qvm()
        q = machine.qAlloc_many(5)
        c = machine.cAlloc_many(5)

        prog = QProg()
        prog << random_qcircuit(q, 10)

        # 生成任意酉矩阵
        unitary_matrix = unitary_group.rvs(2**2,random_state=169384)

        prog << X([q[2], q[3], q[4]])\
            << RXX(q[0], q[1], 1).control([q[2], q[3], q[4]])\
            << RYY(q[0], q[1], 2).control([q[2], q[3], q[4]])\
            << QOracle([q[0], q[1]], unitary_matrix).control([q[2], q[3], q[4]])

        in_matrix = get_unitary(prog)

        def compare_complex_lists(list1, list2, tolerance=1e-6):
            array1 = np.array(list1)
            array2 = np.array(list2)

            real_close = np.allclose(array1.real, array2.real, atol=tolerance)
            imag_close = np.allclose(array1.imag, array2.imag, atol=tolerance)
            return real_close and imag_close

        out_matrix = get_unitary(ldd_decompose(prog))

        import numpy as np
        if(compare_complex_lists(in_matrix, out_matrix)):
            print("ldd_decompose success.")

**其他更新：**

1.修复了ISWAP的dagger形式在多个虚拟机下的计算结果错误
2.修复了部分情况下pyqpanda导入依旧需要libcurl的问题

3.8.1 - 2023-12-25
--------------------

**新增功能和重要更新：**

1.新增了稀疏态量子态初态接口，用于稀疏方式进行初态制备，需要满足初态归一化条件，代码示例：

    .. code-block:: python

        machine = CPUQVM()
        machine.set_configure(72,72);

        machine.init_qvm()

        qlist = machine.qAlloc_many(6)
        clist = machine.cAlloc_many(6)

        sparse_state = {'000000' : 0.5 + 0.5j, '000001' : 0.5 + 0.5j}
        machine.init_sparse_state(sparse_state, qlist)

        prog = QProg()
        prog << I(qlist[0])

        machine.directly_run(prog)  
        probs = machine.get_qstate();

        print(probs)

2.量子云虚拟机添加了批量任务提交，目前仅可用于芯片任务的批量任务提交。

    .. code-block:: python

        machine = QCloud()
        machine.set_configure(72,72);

        #xxx替换为量子云用户token
        machine.init_qvm("XXX", True) 

        qlist = machine.qAlloc_many(6)
        clist = machine.cAlloc_many(6)

        measure_prog = QProg()
        measure_prog << hadamard_circuit(qlist)\
                    << CZ(qlist[0], qlist[1])\
                    << Measure(qlist[0], clist[0])\
                    << Measure(qlist[1], clist[1])\
                    << Measure(qlist[2], clist[2])

        batch_prog = [measure_prog for _ in range (6)]

        pmeasure_prog = QProg()
        pmeasure_prog  << hadamard_circuit(qlist)\
                    << CZ(qlist[0], qlist[1])

        batch_measure_result = machine.real_chip_measure_batch(batch_prog, 1000, real_chip_type.origin_72);
        print(batch_measure_result)


3.虚拟机计算模拟和originir指令添加了Mlmer–Srensen"逻辑门（MS门）

    .. code-block:: python

        MS q[0],q[1]

4.新增了CircuitComposer，用于优化打印时的信息显示

    .. code-block:: python

        import pyqpanda as pq
        from pyqpanda import circuit_composer

        def test_append():
            circ1 = CircuitComposer(n_qubits)
            circuit = pq.QCircuit()
            circuit << pq.H(q[0]) << pq.CNOT(q[0], q[1]) << pq.CNOT(q[1], q[2])
            circ1.append(circuit)
            circ1 << pq.BARRIER(q)
            circ1.append(pq.QFT(q[3:]), "QFT")

            print(circ1)
            print(circ1.circuit)

        if __name__ == '__main__':
            n_qubits = 6
            qvm = pq.CPUQVM()
            qvm.init_qvm()
            q = qvm.qAlloc_many(n_qubits)

            test_append()

**其他更新：**

1.修复量子虚拟机set_configure设置与init的冲突，该问题会导致部分情况下的内存泄露

3.8.0 - 2023-10-31
-------------------------

.. _`pyqpanda-algorithm`: https://pyqpanda-algorithm-tutorial.readthedocs.io/en/latest

**更新和代码改动内容：**

1.新增量子程序关于单双门数、层数、总逻辑门数量相关的统计接口 ``count_prog_info`` ,示例

    .. code-block:: python

        # 统计 QProg 的信息
        prog_info = count_prog_info(my_qprog)

        # 统计 QCircuit 的信息，并启用优化
        optimized_info = count_prog_info(my_qcircuit, optimize=True)

        # 获取统计结果的各种属性
        num_layers = prog_info.layer_num
        num_gates = prog_info.gate_num
        num_double_gates = prog_info.double_gate_num
        # ... 其他属性获取
    
    基于分层统计的量子程序数据分析，可用于评估量子程序的运行时间、深度及复杂度，有利于更好的对量子算法进行改进，
    该接口同时提供了较为全面的可视化输出接口，具体可参考 :ref:`QProgInfoCount` 

1. 基于Clifford的 ``stabilizer`` 模拟器添加了噪声模拟，目前仅支持比特翻转,相位反转,比特相位反转,去极化以及相位阻尼这五个噪声模型，具体可以参考下面的代码和 :ref:`Stabilizer` 中的接口介绍。

    .. code-block:: python

        from pyqpanda import *

        machine = Stabilizer()
        machine.set_configure(72,72)

        machine.init_qvm()

        qlist = machine.qAlloc_many(6)
        clist = machine.cAlloc_many(6)

        measure_prog = QProg()
        measure_prog << X(qlist[0])\
                    << X(qlist[1])\
                    << CNOT(qlist[1], qlist[2])\
                    << CNOT(qlist[2], qlist[3])\
                    << measure_all(qlist, clist)

        machine.set_noise_model(NoiseModel.BITFLIP_KRAUS_OPERATOR,GateType.PAULI_X_GATE,0.2)
        print(machine.run_with_configuration(measure_prog,10000))

2. 将pyqpanda中关于算法部分全部移植到 ``pyqpanda-algorithm`` 算法库，这个是一个独立于pyqpanda的算法模块包，详细模块和接口功能具体可见 `pyqpanda-algorithm`_


3. 密度矩阵噪声设置现在可以正确叠加，参考如下代码:
   
    .. code-block:: python

        machine = DensityMatrixSimulator()
        machine.init_qvm()

        prog = QProg()
        q = machine.qAlloc_many(2)
        c = machine.cAlloc_many(2)

        prog.insert(X(q[0]))\
            .insert(CNOT(q[0], q[1]))

        density_matrix1 = machine.get_density_matrix(prog)

        # case 1 expectation: 00 -> 0.42 , 11 -> 0.58
        machine.set_noise_model(NoiseModel.BITFLIP_KRAUS_OPERATOR, GateType.PAULI_X_GATE, 0.3)
        machine.set_noise_model(NoiseModel.BITFLIP_KRAUS_OPERATOR, GateType.PAULI_X_GATE, 0.3)
        density_matrix2 = machine.get_density_matrix(prog)

4. ClassicalCondition添加c_and、c_or、c_not功能，用于构建量子逻辑分支程序时实现复杂的表达式判断，可以参考下面的代码

    .. code-block:: python

        p = QProg();
        p << H(qubits[0]) \
            << CNOT(qubits[0], qubits[1]) \
            << H(qubits[2]) \
            << Measure(qubits[0], cbits[0])\
            << Measure(qubits[1], cbits[1])\
            << Measure(qubits[2], cbits[2])

        true_prog1 = QProg();
        true_prog2 = QProg();
        true_prog3 = QProg();
        true_prog4 = QProg();

        true_prog3 << X(qubits[2]);

        if_prog3 = create_if_prog((cbits[0] == 0).c_and(cbits[1] == 0).c_and(cbits[2] == 0), true_prog3)

**修复和解决的问题：**

1. 修复量子态编码中关于复数数据重载函数在python中调用出现丢失虚部，导致只索引double类型接口错误。

2. 解决某些使用GPU虚拟机情况下，cuda与Eigen3的运行冲突问题

3. 修改了经典寄存器部分情况下有误，造成无法使用qif和qwhile的问题

4. 优化了量子线路映射和转化过程中的错误
   
5. 解决CPUQVM部分初始化和虚拟机释放场景下使用引入的内存泄漏问题  
   
6. 解决了部分映射接口在使用时异常出现程序崩溃和死循环的错误

7. 修改了所有模拟器可能在计算含有BARRIER的量子程序过程中出错的问题

8. 解决控制swap逻辑门，进行多控门分解时，控制信息丢失问题
    
3.7.17.1 - 2023-7-25
-------------------------

**本次小版本更新重点解决的问题如下: **

1.量子门统计相关接口，添加对枚举和整型的兼容性支持

    .. code-block:: python

        from numpy import pi
        from pyqpanda import *

        machine = CPUQVM()
        machine.init_qvm()

        q = machine.qAlloc_many(3)
        c = machine.cAlloc_many(3)

        prog = QProg()
        prog =random_qprog(2,2,10,machine,q)
            
        count_result = count_qgate_num(prog, 7)    

        #上版运行结果：报错，提示数据类型不兼容
        #本次更新结果：正常运行得到结果

        print(count_result)

2.解决单个比特在释放时(qFree接口)程序异常退出的严重性bug

    .. code-block:: python

        from numpy import pi
        from pyqpanda import *

        machine = CPUQVM()

        machine.init_qvm()

        q = machine.qAlloc_many(3)
        c = machine.cAlloc_many(3)

        machine.qFree(q[0])

        #上版运行结果：程序异常退出
        #本次更新结果 : 程序正常结束

        print("qFree success") 

3.修复了qasm相关指令集转化接口，在重复调用时比特重复申请的异常

    .. code-block:: python

        from numpy import pi
        from pyqpanda import *

        machine = CPUQVM()
        machine.init_qvm()

        # 编写QASM文件
        f = open('test_qasm.txt', mode='w',encoding='utf-8')
        f.write("""// test QASM file
            OPENQASM 2.0;
            include "qelib1.inc";
            qreg q[2];
            creg c[2];
            x q[0];
            x q[1];
            """)
        f.close()

        for i in range(5):

            prog_trans, qv, cv = convert_qasm_to_qprog("test_qasm.txt", machine)
            print(prog_trans)

        #上版运行结果：每次的线路比特都不一样
        #本次更新结果 : 每次的线路完全相同

3.7.17 - 2023-5-22
--------------------

**新增功能和重要更新：**

1.新增 ``Clifford模拟器`` ，主要用于基础量子纠错场景以及高比特且稀疏的Clifford门集构成的量子线路模拟，具体接口可以参考 :ref:`Stabilizer` 。 

2.量子云虚拟机相关更新

    （1）为了适配了新版本的本源量子云平台做了相关改动，对每个用户的认证标识符做了签名加密处理，但接口使用方式与之前相同
    （2）完善相关的错误处理，现在出错和异常信息输出更加具体明确

3.新增Pauli算符与矩阵的转化接口，通过矩阵转换Pauli算符接口名为 ``matrix_decompose_hamiltonian`` ,示例如下：

    .. code-block:: python

        import pyqpanda as pq
        import numpy as np

        matrix = np.array([[2,1,4,2],[1,3,2,6],[4,2,2,1],[2,6,1,3]])
        hamiltonian = pq.matrix_decompose_hamiltonian(matrix)
        print(hamiltonian)

4.提供一种利用矩阵乘积态（MPS）的低秩表达近似分布振幅制备算法，可以通过一种较少的CNOT的门完成对分布振幅的表达，并且这种表达是一种近邻接形式，因此可以直接作用于芯片，由于双门个数的减少，也有利于增加分布制备的成功率。

    .. code-block:: python

        import pyqpanda as pq
        import numpy as np

        N = 6
        machine = pq.CPUQVM()
        machine.init_qvm()
        q = machine.qAlloc_many(N)
        input = np.random.rand(2**N)
        input = input/np.linalg.norm(input)
        print(input)
        cir_encode = pq.Encode()
        cir_encode.approx_mps(q,input)

        # 测保真度
        print(cir_encode.get_fidelity(input))

        #获取对应的线路
        cir=cir_encode.get_circuit()


    .. code-block:: python

        #input
        [0.16112594 0.16100983 0.1400971  0.17698809 0.00271532 0.03514281
        0.21320235 0.16615301 0.05702894 0.00801802 0.1383352  0.19258674
        0.17222723 0.04907042 0.08964018 0.18973404 0.19969125 0.04078985
        0.09852639 0.0812352  0.01124633 0.15024028 0.0052733  0.08204391
        0.13542787 0.0063939  0.01784828 0.20612599 0.00029431 0.11172891
        0.03021631 0.04188075 0.11371365 0.01309453 0.15079619 0.10912272
        0.10914789 0.09004797 0.14673464 0.01355957 0.14773146 0.06804273
        0.18411989 0.11896504 0.20181007 0.14760838 0.01292288 0.05372168
        0.16185868 0.0282684  0.20429462 0.15065767 0.00913953 0.05270058
        0.14767897 0.05914504 0.14426304 0.17902859 0.14117762 0.14085366
        0.16269993 0.11606257 0.18384488 0.08961622]

        #保真度
        0.9900438487247981

5.Pauli算符的构造函数现在提供可选参数，用于决定是否合并同类项，同时也可以显式调用手动合并函数

    .. code-block:: python

        import pyqpanda as pq
        import numpy as np

        #默认不合并同类项
        operator = pq.PauliOperator({"X0 Y2" : -0.044750,
                                    "Z0 Z1" : 0.189766,
                                    "Z1 Z0" : 0.270597,
                                    "Z3" : -0.242743})

        print(operator)

        #合并同类项
        operator = pq.PauliOperator({"X0 Y2" : -0.044750,
                                    "Z0 Z1" : 0.189766,
                                    "Z1 Z0" : 0.270597,
                                    "Z3" : -0.242743},True)

        print(operator)

        #手动合并
        operator.reduce_duplicates()

    输出结果如下：

    .. code-block:: python


        #默认不合并同类项
        {
            "X0 Y2" : -0.044750,
            "Z0 Z1" : 0.189766,
            "Z0 Z1" : 0.270597,
            "Z3" : -0.242743
        }

        #合并同类项
        {
            "X0 Y2" : -0.044750,
            "Z0 Z1" : 0.460363,
            "Z3" : -0.242743
        }

    上述可选合并默认参数的使用方式适用于以下Pauli算符的构造函数

    .. code-block:: python

        import pyqpanda as pq
        import numpy as np

        operator = pq.PauliOperator({"X0 X1" : -0.044750, "Z0 Z1" : 0.189766}, True)
        operator = pq.PauliOperator(np.array([0, 1, 1, 0]).reshape(2, 2), True)
        operator = pq.PauliOperator("X0 X1", 0.122, True)

**其他更新：**

1.修复在某些情况下，GPU虚拟机无法在linux下运行的问题

2.修复pyqpanda画量子线路时，Barrier门会出现比特和图像不符的现象

3.在编译优化方面，解决了高深度量子线路编译时，偶尔出现的内存崩溃问题

4.修复部分振幅虚拟机，分解Toffoli门和CU门无法正确识别分解结果的问题，现在部分振幅虚拟机对全部的单双门和Toffoli门均有很好地支持

5.噪声虚拟机添加线程数量控制

6.解决密度矩阵噪声在算符类噪声施加比特参数的错误


3.7.16 - 2023-1-12
--------------------

**新增功能和重要更新:**

1.新增 ``密度矩阵模拟器`` ，适用于小型量子系统下的密度矩阵模拟，同时提供约化密度矩阵，概率分布，哈密顿量期望以及噪声线路模拟等接口，具体可以参考 :ref:`密度矩阵模拟器` 。 

2.优化了泡利算符的构造方式，新增了通过矩阵来构造泡利算符的接口。

3.优化了泡利算符的构造方式，新增了形如 ``operator = 1.5 * x(0) + 0.6 * y(1) + 2.1 * z(2)`` 的更简洁的构造方式。

4.单振幅虚拟机添加获取对应振幅接口。

其他更新
--------------------

1.修复在只有measure线路等情况下，输出latex信息显示和转换失败的问题。

2.更新变分组件，添加三角函数相关接口。

3.优化了获取矩阵接口，现在可以添加了量子比特可选参数，获取一个量子线路中指定比特对应的矩阵。

4.修复退相干噪声计算错误的问题。

5.修复某些情况下GPU模拟器运行错误问题。

6.修复ISWAP门默认参数未统一的问题。

7.删除Encode类中归一化函数，并修改为入参检测归一化。
