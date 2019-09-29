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
        prog.insert(H(qubits[0])).insert(CNOT(qubits[0], qubits[1]))\
            .insert(CNOT(qubits[1], qubits[2])).insert(CNOT(qubits[2], qubits[3]))

然后调用 ``transform_qprog_to_binary`` 接口实现序列化

    .. code-block:: python
          
        prog_str = transform_qprog_to_binary(prog, qvm)

.. note:: 量子程序序列化是两个过程， 首先将量子程序序列化为二进制， 然后再将二进制以base64的格式编码，转化为字符串。

实例
--------------

    .. code-block:: python
    
        from pyqpanda import *

        if __name__ == "__main__":
            qvm = init_quantum_machine(QMachineType.CPU)
            qubits = qvm.qAlloc_many(4)
            cbits = qvm.cAlloc_many(4)

            prog = QProg()
            prog.insert(H(qubits[0])).insert(CNOT(qubits[0], qubits[1]))\
                .insert(CNOT(qubits[1], qubits[2])).insert(CNOT(qubits[2], qubits[3]))

            prog_str = transform_qprog_to_binary(prog, qvm)
            print(prog_str)
            qvm.finalize()

        
运行结果：

    .. code-block:: python

        AAAAAAQAAAAEAAAABAAAAA4AAQAAAAAAJAACAAAAAQAkAAMAAQACACQABAACAAMA    



.. warning:: 
        新版本中接口名有所调整，旧接口 ``get_bin_data`` 将由 ``transform_qprog_to_binary`` 替代。\
      
        ``get_bin_data`` 将于下版本去除，请读者知悉。