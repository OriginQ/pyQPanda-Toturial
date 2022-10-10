
量子比特池
==========================

简介
--------------
QPanda之前版本中量子比特和经典寄存器都是通过虚拟机进行申请，管理，控制。
现在提供独立于虚拟机的方法，即量子比特、经典寄存器不通过虚拟机管理，可以由提供的比特池直接申请、释放。
为了更好的使用量子比特和经典寄存器，我们进一步支持以物理地址代表相应比特使用。

接口说明
--------------
量子比特池：

``OriginQubitPool`` 获取单例的量子比特池， 通过该池对象申请释放量子比特  

``get_capacity`` 获取最大容量  

``set_capacity`` 设置容量  

``get_qubit_by_addr`` 通过物理地址获取量子比特  

经典寄存器池：

``OriginCMem`` 获取单例的经典寄存器池，通过该池对象申请释放经典寄存器  

``get_capacity`` 获取最大容量  

``set_capacity`` 设置容量  

``get_cbit_by_addr`` 通过物理地址获取经典寄存器   

由于申请释放方法均和虚拟机提供的方法相同。 在 :ref:`QuantumMachine` 中有详细介绍。
同时对于量子比特和经典寄存器的使用，现在也可以直接通过对应比特的地址传参。

例如 :
``H(1)`` 可以理解在物理地址为1的量子比特上作用H门。
``Measure(1, 1)`` 可以理解在物理地址为1的量子比特施加Meausre测量，并将结果保存在地址为1的经典寄存器上。


实例
--------------
.. code-block:: python

    from pyqpanda import *
    from numpy import pi
    if __name__=="__main__":  
        # 量子比特可以和虚拟机 脱离关系，获取对应池的单例，这里和QPanda不同，构建的对象就是单例的池
        qpool = OriginQubitPool()
        qpool_1 = OriginQubitPool()
        cmem = OriginCMem()

        # 获取量子比特池容量
        print("get_capacity : ", qpool.get_capacity())
        # 设置量子比特池容量
        qpool.set_capacity(20)
        print("qpool get_capacity : ", qpool.get_capacity())

        #由于获取量子比特池是单例对象，上面设置容量为20，这里qool_1 获取容量也会为20
        print("qpool_1 get_capacity : ", qpool_1.get_capacity())  

        # 通过比特池申请比特，由于是单例模式，要保证申请的比特数量不超过最大容量
        qv = qpool.qAlloc_many(6)
        cv = cmem.cAlloc_many(6)

        # 构建虚拟机
        qvm = CPUQVM()
        qvm.init_qvm()
        prog = QProg()
        # 直接使用物理地址作为量子比特信息入参
        prog << H(0)\
            << H(1)\
            << H(2)\
            << H(4)\
            << X(5)\
            << X1(2)\
            << CZ(2, 3)\
            << RX(3, pi / 4)\
            << CR(4, 5, pi / 2)\
            << SWAP(3, 5)\
            << CU(1, 3, pi / 2, pi / 3, pi / 4, pi / 5)\
            << U4(4, 2.1, 2.2, 2.3, 2.4)\
            << BARRIER([0, 1,2,3,4,5])\
            << BARRIER(0)
            
        #print(prog) 

        # 测量方法也可以使用比特物理地址 
        res_0 = qvm.prob_run_dict(prog, [ 0,1,2,3,4,5 ])
        #res_1 = qvm.prob_run_dict(prog, qv)  #同等上述方法
        #print(res_0)

        # 同样经典比特地址也可以作为经典比特信息入参
        prog << Measure(0, 0)\
            << Measure(1, 1)\
            << Measure(2, 2)
            

        # 使用经典比特地址入参 
        res_2 = qvm.run_with_configuration(prog, [ 0,1,2,3,4,5 ], 5000)
        # res_3 = qvm.run_with_configuration(prog, cv, 5000) #同等上述方法
        #print(res_2)



        # 同时我们还可以再次利用这里申请的qv，避免多次使用虚拟机多次申请比特的问题发生
        qvm_noise = NoiseQVM()
        qvm_noise.init_qvm()
        res_4 = qvm_noise.run_with_configuration(prog, [ 0,1,2,3,4,5 ], 5000)
        print(res_4)

运行结果：
::

    get_capacity :  29
    qpool get_capacity :  20
    qpool_1 get_capacity :  20
    {'000000': 299, '000001': 290, '000010': 986, '000011': 1007, '000100': 238, '000101': 265, '000110': 929, '000111': 986}

