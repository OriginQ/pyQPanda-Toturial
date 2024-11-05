.. PyQPanda documentation master file, created by
   sphinx-quickstart on Tue Jan 22 14:31:31 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

PyQPanda
====================================
|build-status|

.. |build-status| image:: https://travis-ci.org/OriginQ/QPanda-2.svg?branch=master
    :alt: build status
    :scale: 100%
    :target: https://travis-ci.org/OriginQ/QPanda-2

**一种功能齐全，运行高效的量子软件开发工具包**

QPanda 2是由本源量子开发的开源量子计算框架，它可以用于构建、运行和优化量子算法。

QPanda 2作为本源量子计算系列软件的基础库，为OriginIR、Qurator、量子计算服务提供核心部件。

为了方便用户使用，QPanda 2为用户提供了Python版本的pyQPanda,本使用文档是pyQPanda的
教学文档，如希望学习C++版的QPanda 2，请参考 `QPanda使用文档 <https://qpanda-tutorial.readthedocs.io/zh/latest/index.html>`_ 。
   
.. toctree::
    :maxdepth: 2
    :caption: 量子计算入门

    ./1.量子计算入门/index

.. toctree::
    :maxdepth: 2
    :caption: pyqpanda简介

    ./2.pyqpanda简介/index

.. toctree::
    :maxdepth: 2
    :caption: 量子编程基础

    # ./3.量子编程基础/index

.. toctree::
    :maxdepth: 2
    :caption: 量子操作总结

    ./4.量子操作总结/index

.. toctree::
    :maxdepth: 2
    :caption: 可视化

    ./5.可视化/index

.. toctree::
    :maxdepth: 2
    :caption: 模拟器

    ./6.模拟器/index

.. toctree::
    :maxdepth: 2
    :caption: 量子云与真实计算计算服务

    ./7.量子云与真实计算计算服务/index

.. toctree::
    :maxdepth: 2
    :caption: Operators

    ./8.Operators/index

.. toctree::
    :maxdepth: 2
    :caption: 量子线路编译

    ./16.量子计算编译优化/index

.. toctree::
    :maxdepth: 2
    :caption: 量子线路转译

    ./10.量子线路编译/index

.. .. toctree::
..     :maxdepth: 2
..     :caption: 量子线路优化

..     ./11.量子线路优化/index

.. toctree::
    :maxdepth: 2
    :caption: 量子计算机基准测试与校准

    ./12.量子计算机基准测试与校准/index

.. toctree::
    :maxdepth: 2
    :caption: 量子算法组件

    ./13.量子算法组件/index

.. .. toctree::
..     :maxdepth: 2
..     :caption: 量子算法应用

..     ./14.量子算法应用/index

.. .. toctree::
..     :maxdepth: 2
..     :caption: 量子计算编译优化

..     ./16.量子计算编译优化/index

.. .. toctree::
..     :caption: 深入学习
..     :maxdepth: 2

..     QGate
..     QCircuit
..     QWhile
..     QIf
..     QProg
..     QuantumMachine
..     QubitPool
..     Measure
..     PMeasure
..     QCloudServer

.. .. toctree::
..     :caption: 量子程序编译及优化
..     :maxdepth: 2
    
..     QProgToQASM
..     QASMToQProg
..     QProgToQuil
..     QProgStored
..     QProgDataParse
..     OriginIRToQProg
..     QProgToOriginIR
..     MatrixDecompostion
..     GraphMatch
..     ..QCodarMatch

.. .. toctree::
..     :caption: 量子程序分析
..     :maxdepth: 2

..     NodeIter
..     QGateCounter
..     QProgInfoCount
..     QCircuitInfo
..     MultiControlGateDecomposition
..     DrawQProg
..     PlotApi
..     ..QGateValidity
..     QuantumVolume
..     RandomizedBenchmarking
..     CrossEntropyBenchmarking
	
.. .. toctree:
..     :caption: 实用工具
..     :maxdepth: 2
    
..     GraphMatch
..     FillQProgByI
..     MatrixDecompostion

.. .. toctree::
..     :caption: 组件
..     :maxdepth: 2

..     PauliOperator
..     FermionOperator
..     Optimizer
..     HamiltonianSimulation

.. .. toctree::
..     :caption: VQNet
..     :maxdepth: 2
    
..     Var
..     VarOperator
..     VQG
..     VQC
..     GradientOptimizer
..     VQNetExample
    
.. .. toctree::
..     :caption: 量子算法基础
..     :maxdepth: 2
    
..     QubitAndQGate
..     QPreparation
..     QuantumStatePreparation
..     HadamardAndSWAP
..     AmplitudeAmplification
..     QFT
..     QPE
..     QArithmetic
..     HHL
..     Grover
..     Shor
..     QITE

.. toctree::
    :caption: API接口
    :maxdepth: 3

    autoapi/pyqpanda/pyQPanda/index
    autoapi/pyqpanda/utils/index
    autoapi/pyqpanda/Visualization/index
    autoapi/pyqpanda/OriginService/index

