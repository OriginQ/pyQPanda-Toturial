开始使用pyqpanda
========================

系统配置和安装
--------------

.. _QPanda2: https://qpanda-tutorial.readthedocs.io/zh/latest/index.html
.. _`Microsoft Visual C++ Redistributable x64`: https://aka.ms/vs/17/release/vc_redist.x64.exe


为了兼容 \ **高效**\与\ **便捷**\，QPanda2提供了C++ 和 Python两个版本，本文中主要介绍python版本的使用。
如要了解和学习C++版本的使用请移步 QPanda2_。

系统配置
>>>>>>>>>>>>

pyqpanda是以C++为宿主语言，其对系统的环境要求如下：


Windows
---------------------
.. list-table::

    * - software
      - version
    * - `Microsoft Visual C++ Redistributable x64`_ 
      - 2015
    * - Python
      - >= 3.8 && <= 3.11

Linux
---------------------

.. list-table::

    * - software
      - version
    * - GCC
      - >= 5.4.0 
    * - Python
      - >= 3.8 && <= 3.11


下载pyqpanda
>>>>>>>>>>>>>>>>>

如果你已经安装好了python环境和pip工具， 在终端或者控制台输入下面命令：

    .. code-block:: python

        pip install pyqpanda

.. note:: 在linux下若遇到权限问题需要加 ``sudo``
.. note:: 在ubuntun高版本环境可能会出现libffi库导入失败问题，需要安装合适版本的libffi，通过 ``conda install -c conda-forge libffi`` 