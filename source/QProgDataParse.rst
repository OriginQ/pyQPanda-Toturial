.. _QProgDataParse:

解析量子程序二进制文件
==========================

简介
--------------

解析 :ref:`QProgStored` 方法序列化的量子程序。

接口介绍
--------------

我们先用pyQPanda构建一个量子程序：

    .. code-block:: python

        prog = QProg()
        prog.insert(H(qubits[0]).insert(CNOT(qubits[0], qubits[1])) \
                .insert(CNOT(qubits[1], qubits[2])) \
                .insert(CNOT(qubits[2], qubits[3]))；

序列化之后经过base64编码之后得到的结果是（具体序列化的方法参照 :ref:`QProgStored`）

    .. code-block:: c

        b'AAAAAAQAAAAEAAAABAAAAA4AAQAAAAAAJAACAAAAAQAkAAMAAQACACQABAACAAMA\n'

现在就对这个结果反序列化，先将base64的结果解码成二进制数据：

    .. code-block:: c

        str_base64_data = b'AAAAAAQAAAAEAAAABAAAAA4AAQAAAAAAJAACAAAAAQAkAAMAAQACACQABAACAAMA\n'
        data = [int(x) for x in bytes(base64.decodebytes(str_base64_data))]

我们可以使用QPanda2封装的一个接口：

    .. code-block:: python

        transform_binary_data_to_qprog(qvm, data, qubits_parse, cbits_parse, parseProg);

实例
------------

    .. code-block:: python
    
        from pyqpanda import *
        import base64

        if __name__ == "__main__":
            qvm = init_quantum_machine(QMachineType.CPU)
            parseProg = QProg()
            qubits_parse = []
            cbits_parse = []
            str_base64_data = b'AAAAAAQAAAAEAAAABAAAAA4AAQAAAAAAJAACAAAAAQAkAAMAAQACACQABAACAAMA\n';
            data = [int(x) for x in bytes(base64.decodebytes(str_base64_data))]  

            transform_binary_data_to_qprog(qvm, data, qubits_parse, cbits_parse, parseProg)
        
            result = prob_run_tuple_list(parseProg, qubits_parse, -1)
            print(result)
            destroy_quantum_machine(qvm)
运行结果：

    .. code-block:: c

        0, 0.5
        15, 0.5
        1, 0
        2, 0
        3, 0
        4, 0
        5, 0
        6, 0
        7, 0
        8, 0
        9, 0
        10, 0
        11, 0
        12, 0
        13, 0
        14, 0

.. note:: 可以运行出正确的结果说明可以将序列化的量子程序正确的解析出来
