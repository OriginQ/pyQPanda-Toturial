基础概念回顾
############

基础定义
********

在物理学中，量子是物理量的最小的不可分的基本单位。比特是计算机术语，指信息量最小单位。
不同于经典比特，量子比特不再只能取值0或1，还可以处于0和1的任意比例叠加的中间态。

对量子比特进行的基本运算操作叫做量子门。

量子门分为单比特门和多比特门。
单比特门有Hadamard门、Pauli-X/Y/Z门和旋转X/Y/Z门等。二比特门既有受控的单比特门（例如CNOT门等）也有交换门。
通过受控等扩展方式，可以将单比特门和二比特门进一步扩展为多比特门。
注意，测量是一种特殊的量子门，它是不可逆的，会改变量子比特的状态。

任何量子算法，都是由这些基本的量子门组合得到的。

普适量子门的定义参见 `常见量子逻辑门矩阵形式 <https://pyqpanda-toturial.readthedocs.io/zh/latest/QGate.html>`_\。

QPanda接口函数
**************

在QPanda-2.0中，量子门的定义函数形式如下：

.. code-block::
        
        gate = H(qubit)

.. note:: 输入参数为量子比特Qubit及其他参数，返回值为可以插入量子线路的量子门QGate。

在QPanda-2.0中定义的量子门种类非常丰富。\
特别地，QPanda-2.0中支持完全自定义的量子门U4门，它的接口函数同时有以下几种重载：

.. code-block:: python
        
        U4(alpha, beta, gamma, delta, qubit);
        U4(qubit, alpha, beta, gamma, delta);
        U4(matrix, qubit);
        U4(qubit, matrix);

如前文所述，量子门的接口函数有两种拓展操作：转置共轭和受控。两种操作都各有两种实现方式。

转置共轭操作的两种接口函数定义如下：

.. code-block:: python
        
        gate = H(qubit);
        gate1 = gate.dagger();
        gate.setDagger(true);

.. note:: dagger函数返回的是一个基于目标量子门的新量子门，setDagger返回的则是进行转置共轭后的目标量子门。

受控操作的两种接口函数定义如下：

.. code-block:: python
        
        gate = H(qubit);
        gate1 = gate.control(QVec);
        gate.setControl(QVec);

.. note:: 区别与转置共轭操作类似，但受控函数入参是Qvec（qubit的list）而非单个qubit。



实例
****

下面以一个程序实例，来展示基本的量子比特和量子门操作的代码实现。

.. code-block:: python

    #!/usr/bin/env python

    from pyqpanda import *

    if __name__ == "__main__":

        machine = init_quantum_machine(QMachineType.CPU_SINGLE_THREAD)
        qubits = machine.qAlloc_many(3)
        control_qubits = [qubits[0], qubits[1]]
        prog = create_empty_qprog()

        # 构建量子程序
        prog.insert(H(qubits[0])) \
            .insert(H(qubits[1])) \
            .insert(H(qubits[0]).dagger()) \
            .insert(X(qubits[2]).control(control_qubits))

        # 对量子程序进行概率测量
        result = prob_run_dict(prog, qubits, -1)
        destroy_quantum_machine(machine)

        # 打印测量结果
        for key in result:
            print(key+":"+str(result[key]))

输出结果应如下所示，分别以0.5的概率得到 :math:`\left|0\right\rangle`\和 :math:`\left|2\right\rangle` ：

.. code-block::
    
    000:0.5
    010:0.5

以上就是量子比特和量子门的基本定义和在QPanda-2.0中的调用介绍。