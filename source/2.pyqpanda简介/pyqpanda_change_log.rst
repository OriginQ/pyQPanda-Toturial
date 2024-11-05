更新日志
============


3.8.4 - 2024-11-1
--------------------

**新增功能和重要更新：**

1.添加接口，通过QuantumMachine获取哈密顿期望。请查看 :ref:`Measure` 部分获取更多信息。

2.添加接口，通过QCloud获取哈密顿期望。请查看 :ref:`Measure` 部分获取更多信息。

3.提供根据配置选择硬件计算资源运行全振幅虚拟机。更多信息请参考 :ref:`全振幅量子虚拟机` 。

4.更新接口，补充功能，使得可以选择是否在可视化过程中隐藏含参门的全部参数。更多信息请参考 :ref:`DrawQProg` 。

5.更新接口，完善了将QASM指令字符串转换为OriginIR指令字符串的的功能。支持转换的QASM指令字符串对应的操作有：barrier、ccx、ch、cp、crx、cry、crz、cswap、csx、cu、cx、cy、cz、h、id、measure、p、rccx、rx、ry、rz、reset、rzz、s、sx、sdg、sxdg、swap、t、tdg、u、x、y、z。请查看 :ref:`QASMToOriginIR` 部分获取更多信息。

6.更新接口，完善了将QASM指令字符串转换为QProg对象的功能。支持转换的QASM指令字符串对应的操作有：barrer、ccx、ch、cp、crx、cry、crz、cswap、csx、cu、cx、cy、cz、h、id、measure、p、rccx、rx、ry、rz、reset、rzz、s、sx、sdg、sxdg、swap、t、tdg、u、x、y、z。请查看 :ref:`QASMToQProg` 部分获取更多信息。

7.更新接口，完善了将Pyquil指令字符串转换为OriginIR指令字符串的功能。支持转换的Pyquil指令字符串对应的操作有：I、Z、Y、X、H、S、T、CZ、CNOT、SWAP、PSWAP、ISWAP、XY。请查看 :ref:`PyquilToOriginIR` 部分获取更多信息。

8.更新接口，完善了将Pyquil指令字符串转换为QProg对象的功能。支持转换的Pyquil指令字符串对应的操作有：I、Z、Y、X、H、S、T、CZ、CNOT、SWAP、PSWAP、ISWAP、XY。请查看 :ref:`PyquilToQProg` 部分获取更多信息。



3.8.3.4 - 2024-4-30
--------------------

**新增功能和重要更新：**

1.本源量子云计算服务初始化混合加密配置使用选项优化，新增了指定随机数功能，用于对量子计算任务传输和通信中的数据加密过程添加用户指定的随机数。

    设置方式为将 **QCloud** 初始化函数的参数 ``enable_pqc_encryption`` 设置为 ``True`` 即可，默认为 ``False`` 不开启，同时可以传入用户指定的随机数，接受 **192字符大小的16进制字符串，或者96个字节，默认为os.urandom(96)** ，如果参数长度不符合要求，内部会自动进行处理。

    .. code-block:: python

        from pyqpanda import *

        machine = QCloud()
        machine.set_configure(72,72)

        machine.init_qvm(token=my_api_key, enable_pqc_encryption=True, random_num=os.urandom(96))

**错误修改和优化**

1.修改了绘制量子态概率分布接口 ``draw_probability`` 的拼写错误。

2.修改了C++17标准导致的QVec数据结构，封装成对应的python数据结构在python环境下内存异常错误。

3.修改了可视化模块的实际显示问题，包括数字偏移及换行乱码问题修复，以及latex可视化未添加measure操作会崩溃的bug。

4.修改了几处由于C++17升级导致的GPU量子虚拟机运行异常错误

5.修改了量子云计算服务12进制与二进制转换未正确生效以及结果前后不一致的问题

3.8.3.3 - 2024-4-13
--------------------

**新增功能和重要更新：**

1.本源量子云计算服务虚拟机初始化接口和经典量子混合加密使用方式调整。

(1) **QCloud** 初始化函数的参数修改如下
 
    .. code-block:: python

        def init_qvm(self, 
                user_token: str, 
                enable_logging: bool = False,
                log_to_console: bool = True,
                use_bin_or_hex = True,
                enable_pqc_encryption = False,
                random_num : Union[bytes, str] = os.urandom(96),
                request_time_out = 100):

            """
            Initialize the quantum virtual machine (QVM) with specific configurations.
            
            Parameters:
            user_token (str): User authentication token.
            enable_logging (bool): Whether to enable logging, default is False.
            log_to_console (bool): Whether to log to the console, default is True.
            use_bin_or_hex (bool): Whether to use binary or hexadecimal representation, default is True.
            enable_pqc_encryption (bool): Whether to enable PQC encryption, default is False.
            random_num (Union[bytes, str]): Random number used for encryption initialization, default is 96 bits of random bytes.
            request_time_out (int): Timeout for HTTP requests, default is 100 seconds.
            
            """
            
            # init quantum virtual machine
    
    其中参数说明如下:

    - **enable_logging** 用于控制是否记录日志，默认为False
  
    - **log_to_console** 用于控制在开启日志的情况下，将日志输出为文件或者是输出到控制台, 默认为True，即输出到控制台
    
    - **use_bin_or_hex** ，选择使用二进制还是十六进制表示，默认为True，即使用二进制表示。
  
    - **enable_pqc_encryption** ，用于控制是否开启PQC加密，默认为False，不开启。
  
    - **random_num** ，用于指定PQC加密的随机数，默认为96个字节的随机数。
  
    - **request_time_out** ，用于指定HTTP请求的超时时间，默认为100秒。

(2) PQC加密初始化使用方式调整，以前由虚拟机内部获取并更新秘钥，现在必须手动获取pqc本地密钥以及手动更新,首先通过 **get_pqc_encryption** 获取一对密钥，然后通过 **update_pqc_keys** 更新。

    .. code-block:: python

        machine = QCloud()
        machine.set_configure(72,72)

        machine.init_qvm(user_token="your api token",
                         enable_logging=True,
                         log_to_console=True,
                         use_bin_or_hex=True,
                         enable_pqc_encryption=True)
        
        sym_iv, sym_kys = machine.get_pqc_encryption()
        machine.update_pqc_keys(sym_iv, sym_kys)
  

(3) 量子云计算服务新增了获取芯片拓扑结构接口，并支持获取芯片的拓扑信息，或者输出图形化展示。

    .. code-block:: python

        machine = QCloud()
        machine.set_configure(72,72)

        realtime_topology = machine.get_realtime_topology(72)

        machine.show_chip_topology(72)

3.8.3.2 - 2024-04-03
--------------------

**新增功能和重要更新：**

1.调整了基准测试三个算法接口参数和用法，包括 ``单双门随机基准测试`` , ``双门交叉熵基准测试`` ,和 ``量子体积QV`` ，具体可以参考 :ref:`量子芯片基准测试` 

2.本源量子云计算服务新增了混合加密配置使用选项，用于对量子计算任务传输和通信中的任务数据开启 **混合加密** 从而保护数据安全和隐私，可以根据需要选择开启或打开。

开启方式为：将 **QCloud** 初始化函数的参数 ``enable_pqc_encryption`` 设置为 ``True`` 即可，默认为 ``False`` 不开启。

    .. code-block:: python

        from pyqpanda import *

        machine = QCloud()
        machine.set_configure(72,72)

        machine.init_qvm(token=my_api_key, enable_pqc_encryption=True)

当今，随着量子计算机在硬件技术、纠错方法、算法理论与应用等多个维度的不断进步，传统的公钥算法由于无法抵御量子计算机的攻击逐渐变得脆弱，面临着被未来量子计算机攻击的风险。为了提供更强大的安全保护，本源量子云平台引入了一种端到端的 **后量子(PQC)混合加密** 方法，以保护云服务的用户端和服务端之间的信息传输，在有效抵御量子计算机的各种攻击的同时考虑了现有后量子密码极低但潜在的风险，并借助融合传统公钥密钥(RSA类、ECC类)算法规避了这一隐患。

     **混合加密**： 混合加密是一种结合了两种密码算法的模式，该模式或部分或完整地继承各部分密码模块的某些特性，用于混合的两个功能相近的算法可以均为经典密码算法，也可以同时来自PQC。考虑到现有公钥密码算法面对量子计算机的脆弱性以及现阶段PQC算法潜在的风险，混合算法的两部分“原料”一般一半来自经典，一半来自PQC。例如，苹果于最近推出的iMessage加密方案以及谷歌在其浏览器中部署的混合加密方案均为Kyber(PQC的一种)与ECC类算法的混合。

本源量子云采用的混合加密方法来自NIST将要形成标准的 ``格基密码算法Kyber`` 以及 ``ECC类算法`` ，并且在具体的实现过程中尽量采用国家认证的SM系列算法，例如，ECC类算法选取SM2算法，混合流程中用以密钥导出的函数(KDF)选用SM3算法，建立会话密钥后后续加解密采用SM4算法，并使用了安全度较高的CBC模式。

3.解决了部分情况下由于全局虚拟机导致的originir转换异常

4.电路模块可视化完善，包括：
     - 修复导出text偶尔丢失量子逻辑门的错误
     - 对png格式下自定义名称过长进行限制

3.8.3 - 2024-03-01
--------------------

**新增功能和重要更新：**

1.修改了量子虚拟机初始化错误，该错误会导致多个量子虚拟机重复初始化过程引发未知异常，涉及到的虚拟机有张量网络虚拟机,部分振幅虚拟机，单振幅虚拟机，密度矩阵模拟器和Clifford模拟器等

2.解决了mac部分python环境（3.10,3.11）下的包的导入异常问题

3.修改了量子比特池初始化和清空操作不彻底的错误，该错误会导致清空后设置最大容量时内存异常

3.8.2.3 - 2024-01-05
--------------------

**新增功能和重要更新：**

1.量子云计算服务芯片任务添加了相关限制，单个任务的层数不能超过 **500** 层，并且单门控制比特数量不能超过 **2** 个（Toffoli门除外），
双门不支持添加控制比特，如果量子线路中有相关计算需求，需要先调用多控门分解接口 **ldd_decompose** ，参考如下代码：

    .. code-block:: python

        import numpy as np
        from pyqpanda import *

        online_api_key = "XXX"
    
        machine = QCloud()
        machine.set_configure(72,72);

        # online
        machine.init_qvm(online_api_key,True)

        q = machine.qAlloc_many(6)
        c = machine.cAlloc_many(6)

        measure_prog = QProg()
        measure_prog << X(q[1])\
                    << X(q[2])\
                    << H(q[0]).control([q[1], q[2], q[3]])\
                    << CNOT(q[0], q[1])\
                    << CNOT(q[1], q[2]).control([q[1], q[2], q[3]])\
                    << Measure(q[0], c[0])
        
        decomposed_prog = ldd_decompose(measure_prog)
        measure_result = machine.real_chip_measure(decomposed_prog, 1000, real_chip_type.origin_72)

        print(measure_result)

3.8.2 - 2024-01-05
--------------------

**新增功能和重要更新：**

1.量子计算服务适配了本源悟空芯片上线，并且可以支持originir量子程序参数， ``real_chip_type.origin_72`` 即为72比特芯片类型，使用方法可以参考 :ref:`真实芯片计算服务` 

    .. code-block:: python

        from pyqpanda import *

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

        from pyqpanda import *

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

        from pyqpanda import *

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

        batch_measure_result = machine.batch_real_chip_measure(batch_prog, 1000, real_chip_type.origin_72);
        print(batch_measure_result)


3.虚拟机计算模拟和originir指令添加了Mlmer–Srensen"逻辑门（MS门）

    .. code-block:: python

        MS q[0],q[1]

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

        from pyqpanda import *

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

        from pyqpanda import *

        machine = CPUQVM()
        machine.init_qvm()

        qubits = machine.qAlloc_many(3)
        cbits = machine.cAlloc_many(3)

        p = QProg()
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



