可变量子逻辑门(VQG)
======================
要在VQNet中使用量子操作 ``qop`` 或 ``qop_pmeasure`` ,就必须要包含可变量子线路(``VQC``)，而可变量子逻辑门则是构成 ``VQC`` 的基本单位。 可变量子逻辑门(``VariationalQuantumGate``，别名: ``VQG``)，内部维护着一组变量参数以及一组常量参数。
在构造 ``VQG`` 的时候只能对其中一组参数进行赋值。若含有一组常量参数，则可以通过 ``VQG`` 生成含确定参数的普通量子逻辑门, 若含有变量参数，则可以动态修改参数值，并生成对应的参数的普通量子逻辑门。

目前在QPanda::Variational中定义了如下可变量子逻辑门，它们都继承自 ``VQG`` 。

================================     ============== 
 VQG                                   别名
================================     ==============  
VariationalQuantumGate_I              VQG_I  
VariationalQuantumGate_H              VQG_H 
VariationalQuantumGate_T              VQG_T
VariationalQuantumGate_S              VQG_S
VariationalQuantumGate_X              VQG_X
VariationalQuantumGate_Y              VQG_Y
VariationalQuantumGate_Z              VQG_Z
VariationalQuantumGate_X1             VQG_X1
VariationalQuantumGate_Y1             VQG_Y1
VariationalQuantumGate_Z1             VQG_Z1
VariationalQuantumGate_U1             VQG_U1
VariationalQuantumGate_U2             VQG_U2
VariationalQuantumGate_U3             VQG_U3
VariationalQuantumGate_U4             VQG_U4
VariationalQuantumGate_RX             VQG_RX
VariationalQuantumGate_RY             VQG_RY
VariationalQuantumGate_RZ             VQG_RZ
VariationalQuantumGate_CRX            VQG_CRX
VariationalQuantumGate_CRY            VQG_CRY
VariationalQuantumGate_CRZ            VQG_CRZ
VariationalQuantumGate_CNOT           VQG_CNOT
VariationalQuantumGate_CZ             VQG_CZ
VariationalQuantumGate_SWAP           VQG_SWAP
VariationalQuantumGate_iSWAP          VQG_iSWAP
VariationalQuantumGate_SqiSWAP        VQG_SqiSWAP
================================     ============== 


接口介绍
-----------------

.. cpp:class:: VariationalQuantumGate

   .. cpp:function:: VariationalQuantumGate()

        **功能**
            构造函数。
        **参数**
            无

   .. cpp:function:: size_t n_var()
      
        **功能**
            该可变量子逻辑门内部变量个数。
        **参数**
            无
        **返回值**
            变量个数。

   .. cpp:function:: std::vector<var>& get_vars()

        **功能**      
            获取该可变量子逻辑门内部变量。
        **参数**
            无
        **返回值**
            该可变量子逻辑门内部变量。

   .. cpp:function:: std::vector<double>& get_constants()
      
        **功能**
            获取该可变量子逻辑门内部常量。
        **参数**
            无
        **返回值**
            该可变量子逻辑门内部常量。

   .. cpp:function:: int var_pos(var _var)

        **功能**      
            获取变量在该可变量子逻辑门内部索引。
        **参数**
            - _var 变量
        **返回值**
            内部索引，如果不存在在返回-1。

   .. cpp:function:: virtual QGate feed() const = 0
      
        **功能**
            实例化 ``QGate`` 。
        **参数**
            无
        **返回值**
            普通量子逻辑门。

   .. cpp:function:: virtual QGate feed(std::map<size_t, double> offset) const

        **功能**      
            通过指定偏移来实例化 ``QGate`` 。
        **参数**
            - offset 变量对应的偏移映射
        **返回值**
            普通量子逻辑门。

   .. virtual std::shared_ptr<VariationalQuantumGate> copy() = 0
      
        **功能**
            获取当前可变逻辑门的一份拷贝。
        **参数**
            无
        **返回值**
            当前可变逻辑门的一份拷贝。

下面将简要介绍各个可变量子逻辑门的构造方式

.. cpp:class:: VariationalQuantumGate_H

   .. cpp:function:: VariationalQuantumGate_H(Qubit* q)

        **功能**
            H门构造函数。
        **参数**
            - q 目标比特 

.. cpp:class:: VariationalQuantumGate_RX

   .. cpp:function:: VariationalQuantumGate_RX(Qubit* q, var _var)

        **功能**
            RX门构造函数。
        **参数**
            - q 目标比特 
            - _var 参数变量

   .. cpp:function:: VariationalQuantumGate_RX(Qubit* q, double angle)

        **功能**
            RX门构造函数。
        **参数**
            - q 目标比特 
            - angle 参数

.. cpp:class:: VariationalQuantumGate_RY

   .. cpp:function:: VariationalQuantumGate_RY(Qubit* q, var _var)

        **功能**
            RY门构造函数。
        **参数**
            - q 目标比特 
            - _var 参数变量

   .. cpp:function:: VariationalQuantumGate_RY(Qubit* q, double angle)

        **功能**
            RY门构造函数。
        **参数**
            - q 目标比特 
            - angle 参数

.. cpp:class:: VariationalQuantumGate_RZ

   .. cpp:function:: VariationalQuantumGate_RZ(Qubit* q, var _var)

        **功能**
            RZ门构造函数。
        **参数**
            - q 目标比特 
            - _var 参数变量

   .. cpp:function:: VariationalQuantumGate_RZ(Qubit* q, double angle)

        **功能**
            RZ门构造函数。
        **参数**
            - q 目标比特 
            - angle 参数

.. cpp:class:: VariationalQuantumGate_CZ

   .. cpp:function:: VariationalQuantumGate_CZ(Qubit* q1, Qubit* q2)

        **功能**
            CZ门构造函数。
        **参数**
            - q1 控制比特 
            - q2 目标比特

.. cpp:class:: VariationalQuantumGate_CNOT

   .. cpp:function:: VariationalQuantumGate_CNOT(Qubit* q1, Qubit* q2)

        **功能**
            CNOT门构造函数。
        **参数**
            - q1 控制比特 
            - q2 目标比特
可变量子逻辑门的使用方法和量子逻辑门的使用方法类似，这里就不再一一赘述，有问题可以查看量子逻辑门相关内容。

动态修改参数方法
----------
若构造的VQC中含有变量参数，可以通过以下方法动态修改参数值，并生成对应的参数的普通量子逻辑门。

（1）：setValue()，使用方法如下：


    object.setValue(newValue);

（2）："="运算符重新赋值，使用方法如下：


    object = newValue;

实例
----------

.. code-block:: cpp

    #include "QPanda.h"
    #include "Variational/var.h"

    int main()
    {
        using namespace QPanda;
	using namespace QPanda::Variational;

	constexpr int qnum = 4;

	QuantumMachine* machine = initQuantumMachine(CPU);
	auto q = machine->qAllocMany(qnum);

	MatrixXd m1(1, 1);
	MatrixXd m2(1, 1);
	m1(0, 0) = 1;
	m2(0, 0) = 2;

	double x1 = 1.562;
	double x2 = 2.3658;
	var x(m1);
	var y(m2);
	var ts(1.5);
	ts = 1.8;

	

	VQC vqc;
	vqc.insert(VQG_H(q[0]));
	vqc.insert(VQG_T(q[0]));
	vqc.insert(VQG_S(q[1]));


	vqc.insert(VQG_X(q[2]));
	vqc.insert(VQG_Y(q[1]));
	vqc.insert(VQG_Z(q[2]));

	vqc.insert(VQG_X1(q[2]));
	vqc.insert(VQG_Y1(q[1]));
	vqc.insert(VQG_Z1(q[2]));

	vqc.insert(VQG_RPhi(q[0], ts, x));
	vqc.insert(VQG_U1(q[0], ts));
	vqc.insert(VQG_U2(q[1], PI, PI/2));
	vqc.insert(VQG_U3(q[2], PI, PI / 2, PI / 4));


	//vqc.insert();

	vqc.insert(VQG_RX(q[0], x1));
	vqc.insert(VQG_RY(q[1], x2));
	vqc.insert(VQG_RZ(q[0], 0.123));
	vqc.insert(VQG_CZ(q[0], q[1]));
	vqc.insert(VQG_CR(q[0], q[1], PI));
	vqc.insert(VQG_CNOT(q[0], q[1]));

	QCircuit circuit = vqc.feed();
	QProg prog;
	prog << circuit;

	std::cout << convert_qprog_to_originir(prog, machine) << std::endl << std::endl;

	m1(0, 0) = 3.3;
	m2(0, 0) = 4;

	double s = 2.36559;

	x.setValue(m1);
	y.setValue(m2);
	
	ts.setValue(3.145);
	ts = 3.148;

	QCircuit circuit2 = vqc.feed();
	QProg prog2;
	prog2 << circuit2;

	std::cout << convert_qprog_to_originir(prog2, machine) << std::endl;

	return 0;
    }

上述示例会得到以下结果：

.. code-block:: cpp


        QINIT 4
        CREG 0
        H q[0]
        T q[0]
        S q[1]
        X q[2]
        Y q[1]
        Z q[2]
        X1 q[2]
        Y1 q[1]
        Z1 q[2]
        RPhi q[0],(1.8,1)
        U1 q[0],(1.8)
        U2 q[1],(3.1415927,1.5707963)
        U3 q[2],(3.1415927,1.5707963,0.78539816)
        RX q[0],(1.562)
        RY q[1],(2.3658)
        RZ q[0],(0.123)
        CZ q[0],q[1]
        CR q[0],q[1],(3.1415927)
        CNOT q[0],q[1]

        QINIT 4
        CREG 0
        H q[0]
        T q[0]
        S q[1]
        X q[2]
        Y q[1]
        Z q[2]
        X1 q[2]
        Y1 q[1]
        Z1 q[2]
        RPhi q[0],(3.148,3.3)
        U1 q[0],(3.148)
        U2 q[1],(3.1415927,1.5707963)
        U3 q[2],(3.1415927,1.5707963,0.78539816)
        RX q[0],(1.562)
        RY q[1],(2.3658)
        RZ q[0],(0.123)
        CZ q[0],q[1]
        CR q[0],q[1],(3.1415927)
        CNOT q[0],q[1]
       
