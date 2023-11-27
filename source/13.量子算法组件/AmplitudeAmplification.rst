振幅放大
======================


振幅放大（Amplitude Amplification）线路的主要作用为对于给定纯态的振幅进行放大，从而调整其测量结果概率分布。

算法背景
****

假设某个实际问题转化而来的量子模型的解为 :math:`|\varphi_1\rangle`，归一化的叠加态 :math:`|\psi\rangle` 可由 :math:`|\varphi_1\rangle` ，和它的正交量子态如下表示：:math:`|\psi\rangle=\sin\theta|\varphi_1\rangle+\cos\theta|\varphi_0\rangle` 此处，:math:`|\varphi_0\rangle=|\varphi_1^\perp\rangle` ，已知 :math:`|\psi\rangle` 和 :math:`\theta` ，求 :math:`|\varphi_1\rangle` 利用振幅放大算法可以放大上述表达式中目标基向量 :math:`|\varphi_{1}\rangle` 的系数，得到形如
 
 .. math::
   \begin{aligned}
      |\psi_k\rangle=\sin{k\theta}|\varphi_1\rangle+\cos{k\theta}|\varphi_0\rangle,~k\theta\approx\frac{\pi}{2}
   \end{aligned}
的量子态，此时对 :math:`|\psi_k\rangle` 测量得到问题解 :math:`|\varphi_{1}\rangle` 的概率被放大到约为1，因此振幅放大量子线路又被称为提取线路。

考虑一个N维Hilbert空间，存在一个自共轭投影算符 :math:`{\rm P}：{\rm H}\mapsto{\rm H}` 使得

.. math::   
   {\rm P}|x\rangle=
   \begin{cases}
      |x\rangle,~x\in {\rm H_0}\\
      -|x\rangle,~x\in {\rm H_1}
   \end{cases}

其中 :math:`{\rm H}={\rm H_0}\oplus{\rm H_1}`，要求出一个 :math:`x\in{\rm H_1}`.

首先构造出包含问题解的叠加态. 考虑N维量子态 :math:`|0\rangle_N` ，由 :math:`{\rm H}={\rm H_0}\oplus{\rm H_1}` 可知存在一个不含测量的可逆量子算符 :math:`\mathcal{A}` 使得

.. math::
   \begin{aligned}
      \mathcal{A}|0\rangle_N=|\psi\rangle=\cos\theta|\varphi_0\rangle+\sin\theta|\varphi_1\rangle
   \end{aligned}


其中 :math:`|\varphi_0\rangle=|\varphi_1^\perp\rangle,~\varphi_0\in{\rm H_0},~\varphi_1\in{\rm H_1}.`

其次构造出能快速放大解 :math:`|\varphi_1\rangle` 的系数的量子门. 定义幺正算符 :math:`{\rm Q}=-({\rm I}-2|\psi\rangle\langle\psi|){\rm P}`，则有

.. math::
   \begin{aligned}
      {\rm Q}|\varphi_0\rangle=-({\rm I}-2|\psi\rangle\langle\psi|)|\varphi_0\rangle=\cos{2\theta}|\varphi_0\rangle+\sin{2\theta}|\varphi_1\rangle
   \end{aligned}

.. math::
   \begin{aligned}
      {\rm Q}|\varphi_1\rangle=({\rm I}-2|\psi\rangle\langle\psi|)|\varphi_1\rangle=-\sin{2\theta}|\varphi_0\rangle+\cos{2\theta}|\varphi_1\rangle.
   \end{aligned}

于是在 :math:`\{|\varphi_0\rangle,~|\varphi_1\rangle\}张成的子空间{\rm H}_{\psi}内有{\rm Q}=\begin{bmatrix} \cos{2\theta} & -\sin{2\theta} \\ \sin{2\theta} & \cos{2\theta} \end{bmatrix}`.

Q门可视为角度为 :math:`2\theta` 的旋转量子门操作. 实际上若记 :math:`{\rm P}={\rm I}-2|\varphi_1\rangle\langle\varphi_1|` ，
Q门可视为对 :math:`|\varphi_0\rangle` 和对 :math:`|\varphi_1\rangle` 的镜像变换的组合。 :math:`|0\rangle_N` 经过 :math:`\mathcal{A}` 门和n次Q门旋转之后得到的量子态为

.. math::
   \begin{aligned}
      {\rm Q}^n|\psi\rangle=\cos{(2n+1)\theta}|\varphi_0\rangle+\sin{(2n+1)\theta}|\varphi_1\rangle.
   \end{aligned}

当选取 :math:`n=\lfloor\dfrac{\pi}{4\theta}\rfloor` 时，测量量子态 :math:`{\rm Q}^n|\psi\rangle` 得到目标解 :math:`|\varphi_{1}\rangle` 的概率 :math:`\sin^2{(2n+1)\theta}` 趋于最大. 于是测量量子态 :math:`{\rm Q}^n|\psi\rangle` 能够以逼近 1 的概率得到问题的解.

进一步地，对振幅放大操作进行一般化推广，记

.. math::
   \begin{aligned}
      {\rm Q}=-\mathcal{A}S_{0}\mathcal{A}^{-1}S_{P}
   \end{aligned}

其中

.. math::
   \begin{aligned}
   S_{0}=\begin{cases}
      |x\rangle, ~x\in H_{0}\\
      k|x\rangle, ~~x\in H_{1}
      \end{cases},~~
      S_{P}=\begin{cases}
      kx, ~x=0\\
      x, ~x\ne 0
      \end{cases}.
   \end{aligned}

则有

.. math::
   \begin{aligned}
         \begin{split}
            {\rm Q}|\varphi_0\rangle   &=k(1+\cos^{2})(\theta)|\varphi_0\rangle+(1-k)\cos^{2}(\theta)|\varphi_1\rangle,\\
            {\rm Q}|\varphi_1\rangle
            &=k(k-1)\sin^{2}(\theta)|\varphi_0\rangle+k((1-k)\sin^{2}(\theta)-1)|\varphi_1\rangle.
         \end{split}  
   \end{aligned}

证明的关键在于利用幺正算符 :math:`\mathcal{A}` 性质得到

.. math::
   \begin{aligned}
      \langle \varphi|\varphi_{1}\rangle = \langle 0|\mathcal{A}^{\dagger}|\varphi_{1}\rangle= \langle 0|\mathcal{A}^{-1}|\varphi_{1}\rangle=\sin^{2}{\theta}.
   \end{aligned}

即

.. math::
   \begin{aligned} 
      \mathcal{A}^{-1}|\varphi_{1}\rangle=\sin^{2}{\theta}|0\rangle+\lambda|1\rangle
   \end{aligned}

此处的 :math:`{\rm Q}` 为一般意义上的振幅放大算子，通过合理的选择 :math:`k` ，可以得到不同的结果（比如更快的振幅放大）.


代码实例
****

取 :math:`\Omega=\{0,1\}, \left|\psi\right\rangle = \sin{\frac{\pi}{6}}\left|1\right\rangle+
\cos{\frac{\pi}{6}}\left|0\right\rangle,\ P_1=I-2\left|1\right\rangle \left\langle 1\right|=Z,
P=I-2\left|\psi\right\rangle \left\langle\psi\right|`，

振幅放大量子线路的相应代码实例如下

.. code-block:: python

    #!/usr/bin/env python

    import pyqpanda as pq
    from numpy import pi

    if __name__ == "__main__":

        machine = pq.init_quantum_machine(pq.QMachineType.CPU)
        qvec = machine.qAlloc_many(1)
        prog = pq.create_empty_qprog()

        # 构建量子程序
        prog.insert(pq.RY(qvec[0], pi/3))
        prog.insert(pq.Z(qvec[0]))
        prog.insert(pq.RY(qvec[0], pi*4/3))

        # 对量子程序进行概率测量
        result = pq.prob_run_dict(prog, qvec, -1)
        pq.destroy_quantum_machine(machine)

        # 打印测量结果
        for key in result:
             print(key+":"+str(result[key]))

输出结果应如下所示，分别以 :math:`1` 和 :math:`0` 的概率\
得到 :math:`\left|1\right\rangle`\和 :math:`\left|0\right\rangle` ：

.. code-block:: python
    
    0:0
    1:1
