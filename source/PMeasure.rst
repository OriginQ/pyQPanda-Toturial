.. _PMeasure:

概率测量
==================

概率测量是指获得目标量子比特的振幅，目标量子比特可以是一个量子比特也可以是多个量子比特的集合。 在QPanda2中概率测量又称为PMeasure 。
概率测量和 :ref:`Measure` 是完全不同的过程，Measure是执行了一次测量， 并返回一个确定的0/1结果，并且改变了量子态，

接口介绍
----------------

QPanda2提供了三种获得PMeasure结果的方式，其中有 ``prob_run_list`` 、 ``prob_run_tuple_list``  、 ``prob_run_dict``。

- ``prob_run_list`` ： 获得目标量子比特的概率测量结果列表。
- ``prob_run_tuple_list``： 获得目标量子比特的概率测量结果，为字典类型，其对应的下标为十进制。
- ``prob_run_dict`` ：  获得目标量子比特的概率测量结果，为字典类型，其对应的下标为二进制。

这三个函数的使用方式是一样的，下面就以 ``prob_run_dict`` 为例介绍，使用方式如下：

    .. code-block:: python

        prog = QProg()
        prog << H(qubits[0])\
             << CNOT(qubits[0], qubits[1])\
             << CNOT(qubits[1], qubits[2])\
             << CNOT(qubits[2], qubits[3])

        result = prob_run_dict(prog, qubits, 3)

第一个参数是量子程序， 第二个参数是 ``QVec`` 它指定了我们关注的量子比特。
第三个参的值为-1时，获取所有的概率测量结果，大于0时表示获取最大的前几个数。

实例
-----------

    .. code-block:: python

        from pyqpanda import *

        if __name__ == "__main__":
            qvm = CPUQVM()
            qvm.init_qvm()
            qubits = qvm.qAlloc_many(2)
            cbits = qvm.cAlloc_many(2)

            prog = QProg()
            prog << H(qubits[0])\
                << CNOT(qubits[0], qubits[1])

            print("prob_run_dict: ")
            result1 = qvm.prob_run_dict(prog, qubits, -1)
            print(result1)

            print("prob_run_tuple_list: ")
            result2 = qvm.prob_run_tuple_list(prog, qubits, -1)
            print(result2)

            print("prob_run_list: ")
            result3 = qvm.prob_run_list(prog, qubits, -1)
            print(result3)



运行结果：

    .. code-block:: python

        prob_run_dict: 		    
        {'00': 0.4999999999999999, '01': 0.0, '10': 0.0, '11': 0.4999999999999999}		         
        prob_run_tuple_list: 		      
        [(0, 0.4999999999999999), (3, 0.4999999999999999), (1, 0.0), (2, 0.0)]		       
        prob_run_list: 		   
        [0.4999999999999999, 0.0, 0.0, 0.4999999999999999]

.. note::

    ``概率测量`` 不支持噪声虚拟机
