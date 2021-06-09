.. _QProgStored:

量子程序序列化
==========================

简介
--------------
定义一种协议将量子程序序列化为二进制数据，方便量子程序的存储与传输。

接口介绍
--------------

我们先用pyqpanda构建一个量子程序：

    .. code-block:: python
          
        prog = QProg()
        prog << H(qubits[0]) \
            << CNOT(qubits[0], qubits[1]) \
            << CNOT(qubits[1], qubits[2]) \
            << CNOT(qubits[2], qubits[3])

然后调用 ``convert_qprog_to_binary`` 接口实现序列化

    .. code-block:: python
          
        prog_str = convert_qprog_to_binary(prog, qvm)

.. note:: 量子程序序列化是两个过程， 首先将量子程序序列化为二进制， 然后再将二进制以base64的格式编码，转化为字符串。

实例
--------------

    .. code-block:: python
    
        from pyqpanda import *
        import base64

        if __name__ == "__main__":
            qvm = init_quantum_machine(QMachineType.CPU)
            qubits = qvm.qAlloc_many(4)
            cbits = qvm.cAlloc_many(4)

            # 构建量子程序
            prog = QProg()
            prog << H(qubits[0]) \
                << CNOT(qubits[0], qubits[1]) \
                << CNOT(qubits[1], qubits[2]) \
                << CNOT(qubits[2], qubits[3])

            # 量子程序序列化
            binary_data = convert_qprog_to_binary(prog, qvm)
            
            # 将得到的二进制数据以base64的方式编码，并打印
            str_base64_data =  base64.encodebytes(bytes(binary_data))
            print(str_base64_data)

            destroy_quantum_machine(qvm)

        
运行结果：

    .. code-block:: c

        b'AAAAAAQAAAAEAAAABAAAAA4AAQAAAAAAJAACAAAAAQAkAAMAAQACACQABAACAAMA\n'  

.. note:: 二进制数据不能直接输出，以base64的编码格式编码，得到相应的字符串

.. warning:: 
        新增接口 ``convert_qprog_to_binary()`` ，与老版本接口 ``transform_qprog_to_binary()`` 功能相同。

