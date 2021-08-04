量子逻辑门
====================
----

经典计算中，最基本的单元是比特，而最基本的控制模式是逻辑门。我们可以通过逻辑门的组合来达到我们控制电路的目的。类似地，处理量子比特的方式就是量子逻辑门。
使用量子逻辑门，我们有意识的使量子态发生演化。所以量子逻辑门是构成量子算法的基础。

量子逻辑门由酉矩阵表示。最常见的量子门在一个或两个量子位的空间上工作，就像常见的经典逻辑门在一个或两个位上操作一样。

常见量子逻辑门矩阵形式
--------------------------------------

.. |I| image:: images/QGate_I.png
   :width: 50px
   :height: 50px

.. |H| image:: images/QGate_H.png
   :width: 50px
   :height: 50px

.. |T| image:: images/QGate_T.png
   :width: 50px
   :height: 50px

.. |S| image:: images/QGate_S.png
   :width: 50px
   :height: 50px

.. |X| image:: images/QGate_X.png
   :width: 50px
   :height: 50px

.. |Y| image:: images/QGate_Y.png
   :width: 50px
   :height: 50px
   
.. |Z| image:: images/QGate_Z.png
   :width: 50px
   :height: 50px

.. |X1| image:: images/QGate_X1.png
   :width: 50px
   :height: 50px

.. |Y1| image:: images/QGate_Y1.png
   :width: 50px
   :height: 50px
   
.. |Z1| image:: images/QGate_Z1.png
   :width: 50px
   :height: 50px

.. |RX| image:: images/QGate_RX.png
   :width: 50px
   :height: 50px

.. |RY| image:: images/QGate_RY.png
   :width: 50px
   :height: 50px

.. |RZ| image:: images/QGate_RZ.png
   :width: 50px
   :height: 50px

.. |U1| image:: images/QGate_U1.png
   :width: 50px
   :height: 50px

.. |U2| image:: images/QGate_U2.png
   :width: 50px
   :height: 50px

.. |U3| image:: images/QGate_U3.png
   :width: 50px
   :height: 50px

.. |U4| image:: images/QGate_U4.png
   :width: 50px
   :height: 50px

.. |CNOT| image:: images/QGate_CNOT.png
   :width: 50px
   :height: 50px

.. |CR| image:: images/QGate_CR.png
   :width: 50px
   :height: 50px

.. |iSWAP| image:: images/QGate_iSWAP.png
   :width: 50px
   :height: 50px

.. |SWAP| image:: images/QGate_SWAP.png
   :width: 50px
   :height: 50px

.. |CZ| image:: images/QGate_CZ.png
   :width: 50px
   :height: 50px

.. |CU| image:: images/QGate_CU.png
   :width: 50px
   :height: 50px

.. |Toffoli| image:: images/QGate_Toff.png
   :width: 50px
   :height: 50px

单比特量子逻辑门：
`````````````````````````````````````````````````
.. tabularcolumns:: |m{0.06\textwidth}<{\centering}|c|c|

.. list-table:: 
   :align: center
   :class: longtable 

   * - |I|                                                     
     - ``I``                     
     - :math:`\begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}\quad`
   * - |H|                                                      
     - ``Hadamard``              
     - :math:`\begin{bmatrix} 1/\sqrt {2} & 1/\sqrt {2} \\ 1/\sqrt {2} & -1/\sqrt {2} \end{bmatrix}\quad`
   * - |T|                                                     
     - ``T``                     
     - :math:`\begin{bmatrix} 1 & 0 \\ 0 & \exp(i\pi / 4) \end{bmatrix}\quad`
   * - |S|                                                     
     - ``S``                      
     - :math:`\begin{bmatrix} 1 & 0 \\ 0 & 1i \end{bmatrix}\quad`
   * - |X|                                                     
     - ``Pauli-X``               
     - :math:`\begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}\quad`
   * - |Y|                                                     
     - ``Pauli-Y``               
     - :math:`\begin{bmatrix} 0 & -1i \\ 1i & 0 \end{bmatrix}\quad`
   * - |Z|                                                     
     - ``Pauli-Z``               
     - :math:`\begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}\quad`
   * - |X1|                                                    
     - ``X1``                    
     - :math:`\begin{bmatrix} 1/\sqrt {2} & -1i/\sqrt {2} \\ -1i/\sqrt {2} & 1/\sqrt {2} \end{bmatrix}\quad`
   * - |Y1|                                                    
     - ``Y1``                    
     - :math:`\begin{bmatrix} 1/\sqrt {2} & -1/\sqrt {2} \\ 1/\sqrt {2} & 1/\sqrt {2} \end{bmatrix}\quad`
   * - |Z1|                                                    
     - ``Z1``                    
     - :math:`\begin{bmatrix} \exp(-i\pi/4) & 0 \\ 0 & \exp(i\pi/4) \end{bmatrix}\quad`
   * - |RX|                                                    
     - ``RX``                    
     - :math:`\begin{bmatrix} \cos(\theta/2) & -1i×\sin(\theta/2) \\ -1i×\sin(\theta/2) & \cos(\theta/2) \end{bmatrix}\quad`
   * - |RY|                                                    
     - ``RY``                    
     - :math:`\begin{bmatrix} \cos(\theta/2) & -\sin(\theta/2) \\ \sin(\theta/2) & \cos(\theta/2) \end{bmatrix}\quad`
   * - |RZ|                                                    
     - ``RZ``                    
     - :math:`\begin{bmatrix} \exp(-i\theta/2) & 0 \\ 0 & \exp(i\theta/2) \end{bmatrix}\quad`
   * - |U1|                                                    
     - ``U1``                    
     - :math:`\begin{bmatrix} 1 & 0 \\ 0 & \exp(i\theta) \end{bmatrix}\quad`
   * - |U2|                                                    
     - ``U2``                    
     - :math:`\begin{bmatrix} 1/\sqrt {2} & -\exp(i\lambda)/\sqrt {2} \\ \exp(i\phi)/\sqrt {2} & \exp(i\lambda+i\phi)/\sqrt {2} \end{bmatrix}\quad`
   * - |U3|                                                    
     - ``U3``                    
     - :math:`\begin{bmatrix} \cos(\theta/2) & -\exp(i\lambda)×\sin(\theta/2) \\ \exp(i\phi)×\sin(\theta/2) & \exp(i\lambda+i\phi)×\cos(\theta/2) \end{bmatrix}\quad`
   * - |U4|                                                    
     - ``U4``                    
     - :math:`\begin{bmatrix} u0 & u1 \\ u2 & u3 \end{bmatrix}\quad`


多比特量子逻辑门：
`````````````````````````````````````````````````
.. tabularcolumns:: |m{0.1\linewidth}<{\centering}|c|c|

.. list-table:: 
   :widths: auto
   :align: center
   :class: longtable 

   * - |CNOT|                                                      
     - ``CNOT``                  
     - :math:`\begin{bmatrix} 1 & 0 & 0 & 0  \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{bmatrix}\quad`
   * - |CR|                                                        
     - ``CR``                    
     - :math:`\begin{bmatrix} 1 & 0 & 0 & 0  \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & \exp(i\theta) \end{bmatrix}\quad`
   * - |iSWAP|                                                      
     - ``iSWAP``                 
     - :math:`\begin{bmatrix} 1 & 0 & 0 & 0  \\ 0 & \cos(\theta) & -i×\sin(\theta) & 0 \\ 0 & -i×\sin(\theta) & \cos(\theta) & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}\quad`
   * - |SWAP|                                                      
     - ``SWAP``                  
     - :math:`\begin{bmatrix} 1 & 0 & 0 & 0  \\ 0 & 0 & 1 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}\quad`
   * - |CZ|                                                        
     - ``CZ``                    
     - :math:`\begin{bmatrix} 1 & 0 & 0 & 0  \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & -1 \end{bmatrix}\quad`
   * - |CU|                                                        
     - ``CU``                    
     - :math:`\begin{bmatrix} 1 & 0 & 0 & 0  \\ 0 & 1 & 0 & 0 \\ 0 & 0 & u0 & u1 \\ 0 & 0 & u2 & u3 \end{bmatrix}\quad`
   * - |Toffoli|                                                    
     - ``Toffoli``               
     - :math:`\begin{bmatrix} 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0  \\ 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1  \\ 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 \\ \end{bmatrix}\quad`

.. _api_introduction:

QPanda 2把所有的量子逻辑门封装为API向用户提供使用，并可获得QGate类型的返回值。比如，您想要使用Hadamard门，就可以通过如下方式获得：

     .. code-block:: python
          
         from pyqpanda import *
         import numpy as np
         init(QMachineType.CPU)
         qubits = qAlloc_many(4)
         h = H(qubits[0])

其中参数为目标比特，返回值为量子逻辑门

pyqpanda中支持的不含角度的单门有： ``I``、 ``H``、 ``T``、 ``S``、 ``X``、 ``Y``、 ``Z``、 ``X1``、 ``Y1``、 ``Z1``

qubit如何申请会在 :ref:`QuantumMachine` 部分介绍。

单门带有一个旋转角的逻辑门门，例如RX门：

     .. code-block:: python
          
         rx = RX(qubits[0]，np.pi/3)

第一个参数为目标比特
第二个参数为旋转角度 

pyqpanda中支持的单门带有一个旋转角度的逻辑门有： ``RX``、``RY``、``RZ``、``U1``
   

pyqpanda中还支持 ``U2``、``U3``、``U4`` 门，其用法如下：

      .. code-block:: python

         # U2(qubit, phi, lambda) 有两个角度
         u2 = U2(qubits[0]，np.pi, np.pi/2) 

         # U3(qubit, theta, phi, lambda) 有三个角度
         u3 = U3(qubits[0]，np.pi, np.pi/2, np.pi/4)
         
         # U4(qubit, alpha, beta, gamma, delta) 有四个角度
         u4 = U4(qubits[0]，np.pi, np.pi/2, np.pi/4, np.pi/2)   

两比特量子逻辑门的使用和单比特量子逻辑门的用法相似，只不过是输入的参数不同，例如CNOT门：

     .. code-block:: python
          
         cnot = CNOT(qubits[0]，qubits[1])

第一个参数为控制比特
第二个参数为目标比特 
注：两个比特不能相同

pyqpanda中支持的双门不含角度的逻辑门有： ``CNOT``、``CZ`` 、``SWAP``、``iSWAp``、``SqiSWAP``

两比特量子逻辑门的使用和单比特量子逻辑门的用法相似，只不过是输入的参数不同，举个使用CNOT的例子：

     .. code-block:: python
          
         cnot = CNOT(control_qubit, target_qubit);

CNOT门接收两个参数，第一个是控制比特，第二个是目标比特。

pyqpanda中支持的双门含旋转角度的逻辑门有： ``CR``、``CU`` 、``CP``

双门带有旋转角度的门，例如CR门：

      .. code-block:: python
            
         cr = CR(qubits[0]，qubits[1]，np.pi)

第一个参数为控制比特, 第二个参数为目标比特, 第三个参数为旋转角度 

支持CU门，使用方法如下：

      .. code-block:: python

         # CU(control, target, alpha, beta, gamma, delta) 有四个角度   
         cu = CU(qubits[0]，qubits[1]，np.pi,np.pi/2,np.pi/3,np.pi/4)

获得三量子逻辑门 ``Toffoli`` 的方式：

     .. code-block:: python

          toffoli = Toffoli(qubits[0], qubits[1], qubits[2])

三比特量子逻辑门Toffoli实际上是CCNOT门，前两个参数是控制比特，最后一个参数是目标比特。

pyqpanda还支持在量子逻辑门中添加量子比特数组操作，即将该数组中的所有量子比特赋予同一种逻辑门运算，举个使用单门H的例子：

     .. code-block:: python

          # 这里返回的是一个量子线路
          circuit = H(Qvec);

这里的Qvec即为存放量子比特的数组。在对多门进行数组操作时，则是传入对应的多个数组，并按照数组下标顺序进行逻辑门运算。

接口介绍
----------------

在本章的开头介绍过，所有的量子逻辑门都是酉矩阵，那么您也可以对量子逻辑门做转置共轭操作，获得一个量子逻辑门 ``dagger`` 之后的量子逻辑门可以用下面的方法：

      .. code-block:: python
            
         rx_dagger = RX(qubits[0], np.pi).dagger()

或：

      .. code-block:: python

         rx_dagger = RX(qubits[0], np.pi)
         rx_dagger.set_dagger(true)

也可以为量子逻辑门添加控制比特,获得一个量子逻辑门 control 之后的量子逻辑门可以用下面的方法：

      .. code-block:: python

         qvec = [qubits[0], qubits[1]]
         rx_control = RX(qubits[2], np.pi).control(qvec)

或：
      .. code-block:: python

         qvec = [qubits[0], qubits[1]]
         rx_control = RX(qubits[2], np.pi)
         rx_control.set_control(qvec)

pyqpanda 还封装了一些比较方便的接口，会简化一些量子逻辑门的操作

      .. code-block:: python

         cir = apply_QGate(qubits, H)

qubits的每个量子比特都添加H门

实例
----------------

以下实例主要是向您展现QGate类型接口的使用方式.

   .. code-block:: python

         from pyqpanda import *

         if __name__ == "__main__":
            init(QMachineType.CPU)
            qubits = qAlloc_many(3)
            control_qubits = [qubits[0], qubits[1]]
            prog = create_empty_qprog()

            # 构建量子程序
            prog  << H(qubits) \
                  << H(qubits[0]).dagger() \
                  << X(qubits[2]).control(control_qubits)

            # 对量子程序进行概率测量
            result = prob_run_dict(prog, qubits, -1)

            # 打印测量结果
            print(result)
            finalize()

计算结果如下：

    .. code-block:: python
        
      {'000': 0.24999999999999295, '001': 0.0, '010': 0.24999999999999295, '011': 0.0, '100': 0.24999999999999295, '101': 0.0, '110': 0.24999999999999295, '111': 0.0}
