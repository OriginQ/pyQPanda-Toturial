.. QPanda 2 documentation master file, created by
   sphinx-quickstart on Tue Jan 22 14:31:31 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

QPanda 2
====================================
|build-status|

.. |build-status| image:: https://travis-ci.org/OriginQ/QPanda-2.svg?branch=master
    :alt: build status
    :scale: 100%
    :target: https://travis-ci.org/OriginQ/QPanda-2

**一种功能齐全，运行高效的量子软件开发工具包**

QPanda 2是由本源量子开发的开源量子计算框架，它可以用于构建、运行和优化量子算法。

QPanda 2作为本源量子计算系列软件的基础库，为QRunes、Qurator、量子计算服务提供核心部件。

为了方便用户使用，QPanda 2为用户提供了Python版本的pyQPanda,本使用文档是pyQPanda的
教学文档，如希望学习C++版的QPanda 2，请参考 `QPanda使用文档 <https://qpanda-toturial.readthedocs.io/zh/latest/index.html>`_ 。
   
.. toctree::
    :maxdepth: 2

    GettingStarted

深入学习
----------

.. toctree::
    :maxdepth: 2

    QGate
    QCircuit
    QWhile
    QIf
    QProg
    QuantumMachine
    Measure
    PMeasure

工具组件
---------

.. toctree::
    :maxdepth: 2

    QGateCounter
    QProgClockCycle
    QProgStored
    OriginIRToQProg
    NodeIter
    QCircuitInfo

量子程序转换
-------------

.. toctree::
    :maxdepth: 2
    
    QProgToQASM
    QProgToOriginIR
    QProgToQuil

算法组件
---------

.. toctree::
    :maxdepth: 2

    PauliOperator
    FermionOperator
    Optimizer

.. toctree::
    :caption: VQNet
    :maxdepth: 2
    
    Var
    VarOperator
    VQG
    VQC
    GradientOptimizer
    VQNetExample
