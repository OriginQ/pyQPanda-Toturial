Change Log


2.1.2 - 2020-07-19

add
*******

1. 添加 SU4 线路映射功能
2. 添加含噪声虚拟机中添加角度旋转误差接口 set_rotation_angle_error
3. 添加通过泡利矩阵设置噪声模型的方法 set_noise_kraus_matrix
4. 添加通酉矩阵和概率设置噪声的方法 set_noise_unitary_matrix
5. 添加生成随机线路的功能 RandomCircuit
6. 添加 Base_QCircuit 文件夹存放基础量子线路，QFT，QPE 等
7. 添加 HHL 算法
8. 添加 QARM 算法
9. 添加 QSVM 算法
10. 添加 QITE 算法
11. 添加 QGate::remap 接口，映射逻辑门量子bit到不同的量子bit

update
***********

12. convert_qasm_to_qprog 支持科学记数表达式：如 1.0e-10
13. 修改 runwithconfiguration 返回结果的显示方式
14. 修复 free qubit 内存泄漏
15. 修复 U4 gamma 值为nan的问题
16. 更新线路优化算法
17. 修复 Psi4Wrapper 中成员变量未赋初值的bug

2.1.2 - 2020-06-01

add
*******

1. QAdder 量子加法器功能
2. amplitude_encode实现经典数据的量子态振幅编码
3. run_with_configuration 添加测量次数的接口
4. QCodar一种用于各种NISQ设备的上下文持续时间

update
***********

1. 感知的Qubit映射
2. 修改 QCloudMachine 接口
3. 修改 SQISWAP 、U2 、U3 门中的bug
4. 调整 topology_match 功能，使QVec完成物理比特映射

2.1.1 - 2020-03-15
==============================

add
*******

1. QCloudMachine 添加商业云功能
2. ChemiQ可以生成动态库

update
***********

1. 修改GTEST测试框架
2. 修改NoiseQVM中的算法错误
3. 修改QIF和QWHILE中的执行错误
4. 修改注释部分的乱码引起的编译错误

2.1.0 - 2020-11-8
===========================

add
*******

1. 添加逻辑门：I门
2. 添加接口：fill_qprog_by_I：通过I门填充QProg
3. 添加接口：cast_qprog_qgate：转换Qprog到Qgate
4. 添加接口：cast_qprog_qmeasure：转换Qprog到Qmeasure
5. 添加接口：cast_qprog_qcircuit：转换Qprog到QCircuit，遇到流控节点或者测量节点，返回false
6. 添加接口：NoiseModel::set_noise_model():设置NoiseModel配置接口
7. 添加接口：flatten()：添加展开量子程序中的嵌套节点的功能
8. 添加功能：单振幅量子虚拟机中添加SWAP门
9. 添加接口：convert_qprog_to_binary：转换QProg到二进制
10. 添加接口：convert_binary_data_to_qprog：转换二进制到QProg
11. 添加接口：convert_originir_to_qprog：转换Qoriginir到QProg
12. 添加接口：convert_qasm_to_qprog：新增QASM转QProg的方法
13. 添加接口：convert_qprog_to_originir：转换QProg到Qoriginir
14. 添加接口：convert_qprog_to_quil：转换QProg到QUil
15. 添加接口：convert_qprog_to_qasm：转换QProg到QASM


update
***********

1. 调整QPanda2 的Utilities目录：Compiler：存放QProg到其他平台的适配转换，QProgInfo：存放线路信息查询相关接口，QProgTransform：Qprog的其他形式转换比如有向无环图，Tools：存放其他工具类接口
2. 调整接口：原字符画接口print_prog改为：draw_qprog
3. 修改接口名：QVM::setConfigure为 QVM::setConfig
4. 添加新的含噪声虚拟机模型:DECOHERENCE_KRAUS_OPERATOR_P1_P2, BITFLIP_KRAUS_OPERATOR, DEPOLARIZING_KRAUS_OPERATOR, BIT_PHASE_FLIP_OPRATOR, PHASE_DAMPING_OPRATOR
5. 调整接口：通过重载std::cout，直接输出目标线路的字符画

2.0.0 - 2019-9-30
===========================

add
*******

1. 添加接口createEmptyCircuit：创建空的量子线路
2. 添加接口QWhile::getClassicalCondition： 获得经典表达式
3. 添加接口createWhileProg：创建QWhile
4. 添加接口createIfProg： 创建QIf
5. 添加接口createEmptyQProg：创建量子程序
6. 添加接口 QVM::setConfigure: 设置比特数和经典寄存器数
7. 添加接口QVM:: qAlloc: 申请量子比特
8. 添加接口QVM::qAllocMany：申请多个量子比特
9. 添加接口QVM::getAllocateQubitNum：获取申请的量子比特数
10. 添加接口QVM::getAllocateCMemNum 获取申请的经典寄存器数
11. 添加接口QVM::cAlloc: 申请一个经典寄存器
12. 添加接口QVM::cAllocMany：申请多个经典寄存器
13. 添加接口SingleAmplitudeQVM：pMeasureBinIndex： 通过二进制下标进行PMeasure操作
14. 添加接口SingleAmplitudeQVM：pMeasureDecIndex： 通过十进制下标进行PMeasure操作
15. 添加接口CPUQVM:: pMeasureNoIndex: PMeasure操作
16. 添加接口validateSingleQGateType： 验证单量子逻辑门有效性
17. 添加接口validateDoubleQGateType：验证双量子逻辑门有效性
18. 添加接口getUnsupportQGateNum：统计量子程序（包含量子线路、QIF、QWHILE）中不支持的逻辑门的数量
19. 添加接口getQGateNum：统计量子程序（包含量子线路、QIF、QWHILE）中逻辑门的数量
20. 添加接口transformBinaryDataToQProg： 解析二进制数据转化为量子程序
21. 添加接口transformQProgToBinary：量子程序转化为二进制数据

update
***********

1. QPanda重构了项目框架把QPanda分为Applications、QAlg、Components、Core四层。

================
1.3.4 - 2019-08-05
1、接口 QProgToBinary名改变为qProgToBinary
2、接口getQProgClockCycle的参数顺序改变(QuantumMachine *qm, QProg &prog)->(QProg &prog, QuantumMachine *qm)
3、QPanda和pyqpanda 添加apply_Gate 接口；
4、更新DJ算法和Grove算法；
5、更新量子程序遍历框架；
6、添加部分振幅取任意振幅子集的接口
7、pyqpanda 添加设置setConfig的接口
8、pyqpanda QVec添加append 、pop接口
9、pyqpanda 修改Measure_all接口名为measure_all
10、pyqpanda 修改Measure接口名为measure
1.3.3 - 2019-06-20
单振幅和部分振幅虚拟机支持更多的量子比特；QIf和QWhile接口重构；更新DJ算法；QStat精度兼容double和float类型
1.3.2 - 2019-05-27
添加量子线路深拷贝功能，修改部分程序bug
1.3.1 - 2019-05-07
修复量子程序转换的bug 修复QCloudMachine编译问题
1.3.0 - 2019-04-28 
-------------------------
add
*******
1. 添加量子机器学习框架VQNet。
2. 添加部分振幅量子虚拟机PartialAmplitudeQVM。
3. 添加单振幅量子虚拟机SingleAmplitudeQVM。
4. 添加含噪声量子虚拟机NoiseQVM。
5. 添加云虚拟机QCloudQVM。
6. 添加量子程序持久化存储功能QProgStored
7. 添加解析持久化存储的量子程序文件QProgDataParse
8. 添加统计量子程序中逻辑门个数的功能QGateCounter

update
***********

1. 更新QProgToQASM的对外接口为transformQProgToQASM
2. 更新QProgToQRunes的对外接口为transformQProgToQRunes
3. 更新量子虚拟机部分对外接口


1.2.0 - 2019-01-18 
-------------------------
add
*******

1. 用户可使用QProg()、QCircuit()、QWhileProg(...)、QIfProg(...)构造相关对象。
2. 对外隐藏CBit类型，统一替换为ClassicalCondition。
3. 实现ClassicalCondition 的+,-,*,/，>,>=,<,<=,=,==功能。
4. 实现经典运算在量子虚拟机使用的左值和右值引用功能；实现在量子程序中插入经典运算的功能。
5. 实现在操作量子逻辑门时，目标量子比特集合下边可为变量的功能。
6. 添加qAllocMany接口。此接口可以申请多个量子比特，输入参数为量子比特数，返回值类型修改为QVec。
7. 添加cAllocMany接口，此接口可以申请多个经典寄存器，返回值类型修改为std::vector<ClassicalCondition>。
8. cFreeAll的输入参数类型修改为std::vector<ClassicalCondition>。
9. 添加getProbTupleList接口。使用PMEASURE获取量子程序结果，并返回pair<量子态，概率>类型的vector。
10. 添加getProbList接口。使用PMEASURE获取量子程序结果，并返回概率值的vector。
11. 添加getProbDict接口。使用PMEASURE获取量子程序结果，并返回pair<量子态，概率>类型的map。
12. 添加probRunTupleList接口，根据输入的量子程序，使用PMEASURE获取量子程序结果，并返回pair<量子态，概率>类型的vector。
13. 添加probRunList接口，根据输入的量子程序，使用PMEASURE获取量子程序结果，并返回概率的vector。
14. 添加probRunDict接口，根据输入的量子程序，使用PMEASURE获取量子程序结果，并返回pair<量子态，概率>类型的map。
15. 添加runWithConfiguration接口，根据输入的量子程序和循环次数，统计测量结果，并返回pari<量子态，概率>的map。
16. 添加MeasureAll接口，返回一个量子程序，该量子程序对输入的所有量子比特进行Measure操作。
17. 添加initQuantumMachine接口，此接口可根据输入的QuantumMachine_type返回一个QuantumMachine类型的虚拟机指针。

update
***********

1. cAlloc和cAlloc(size_t)返回值修类型修改为ClassicalCondition
2. cFree的输入参数类型改为ClassicalCondition&
3. 删除getCBitValue接口
4. PMeasure接口的qubit_vector参数数据类型改为QVec
5. PMeasure_no_index接口的qubit_vector参数数据类型改为QVec
6. quick_measure接口的qubit_vector参数数据类型改为QVec
7. init接口添加QuantumMachine_type参数，可以设置生成的量子虚拟机的类型
8. CreateHadamardQCircuit接口的输入参数pQubitVector数据类型改为QVec


