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

.. code-block:: python

        import pyqpanda as pq
	import numpy as np

	if __name__=="__main__":

	    machine = pq.init_quantum_machine(pq.CPU)
	    q = machine.qAlloc_many(2)

	    x = pq.var(1)
	    y = pq.var(2)

	    temp = np.matrix([5])
	    ss=pq.var(temp)


	    vqc = pq.VariationalQuantumCircuit()
	    vqc.insert(pq.VariationalQuantumGate_H(q[0]))
	    vqc.insert(pq.VariationalQuantumGate_RX(q[0], ss))
	    vqc.insert(pq.VariationalQuantumGate_RY(q[1], y))
	    vqc.insert(pq.VariationalQuantumGate_RZ(q[0], 0.12))
	    vqc.insert(pq.VariationalQuantumGate_CZ(q[0], q[1]))
	    vqc.insert(pq.VariationalQuantumGate_CNOT(q[0], q[1]))
	    vqc.insert(pq.VariationalQuantumGate_U1(q[0], x))
	    vqc.insert(pq.VariationalQuantumGate_U2(q[0], np.pi, x))
	    vqc.insert(pq.VariationalQuantumGate_U3(q[0], np.pi, x,  y))
	    vqc.insert(pq.VariationalQuantumGate_U4(q[0], np.pi, x,  y,ss))



	    circuit1 = vqc.feed()

	    prog = pq.QProg()
	    prog.insert(circuit1)

	    print(pq.convert_qprog_to_originir(prog, machine))

	    x.set_value([[3.]])
	    y.set_value([[4.]])

	    circuit2 = vqc.feed()
	    prog2 = pq.QProg()
	    prog2.insert(circuit2)
	    print(pq.convert_qprog_to_originir(prog2, machine))
	    
	    

上述示例会得到以下结果：

.. code-block:: cpp


        QINIT 2
	CREG 0
	H q[0]
	RX q[0],(56)
	RY q[1],(2)
	RZ q[0],(0.12)
	CZ q[0],q[1]
	CNOT q[0],q[1]
	U1 q[0],(1)
	U2 q[0],(3.1415927,1)
	U3 q[0],(3.1415927,1,2)
	U4 q[0],(3.1415927,1,2,5)
	
	QINIT 2
	CREG 0
	H q[0]
	RX q[0],(56)
	RY q[1],(4)
	RZ q[0],(0.12)
	CZ q[0],q[1]
	CNOT q[0],q[1]
	U1 q[0],(3)
	U2 q[0],(3.1415927,3)
	U3 q[0],(3.1415927,3,4)
	U4 q[0],(3.1415927,3,4,5)
