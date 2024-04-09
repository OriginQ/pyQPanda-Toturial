import math
import random
import binascii
import numpy as np
import hashlib
from hashlib import sha3_256, sha3_512, shake_128, shake_256

# 下面三个数字满足: q = k*n+1
q = 3329

n = 256
# 每个多项式包含0次项到63次项
k = 13

eta1, eta2 = 3, 2

# 多项式的个数
# kk 取不同的值分别对应Kyber不同的安全级别
kk = 2

# bar_k = int(math.log(q, 2)) + 1
bar_k = 12
# bar_r = int(pow(4, k)/q)
bar_r = 20158

ted = int(q/2)

du, dv = 10, 4


def compress(x, d_u):
    new_x = round((pow(2, d_u)/q)*x)
    mod = pow(2, d_u)
    new_x = new_x % mod
    return new_x


def decompress(x, d_u):
    new_x = round((q / pow(2, d_u)) * x)
    return new_x


def CBD(byte_array, eta):
    f = [0] * 256
    new_list = hex_to_bits(byte_array)

    for ic in range(0, 256):
        ac, bc = 0, 0
        for jc in range(0, eta):
            ac = ac + int(new_list[2 * ic * eta + jc])
            bc = bc + int(new_list[2 * ic * eta + eta + jc])
        f[ic] = (ac - bc)
    return f


def PRF(ss, bd, eta):
    ss = bytes(ss)
    bd = bytes(bd)
    data = (ss + bd)

    # 使用SHA-3 (SHAKE-256)计算哈希值
    hash_value = hashlib.shake_256(data).digest(64 * eta)

    return hash_value.hex()


def H(data):
    data = binascii.unhexlify(data)

    sha3 = hashlib.sha3_256()
    sha3.update(data)
    string = sha3.hexdigest()
    hex_string = bytes.fromhex(string)
    hex_string = binascii.hexlify(hex_string)
    return hex_string


# Montgomery约化
def mont_red(xx):

    return xx * mont_inv % q


# Montgomery乘法
def mont_mul(aa, bb):

    cc = aa * bb

    return mont_red(cc)


def barrett_red(xx):
    xx = int(xx)

    tem = xx * bar_r
    tem = tem >> (2 * bar_k + 2)
    tedd = xx - tem * q

    if tedd < q:
        return tedd
    if tedd >= q:
        return tedd - q


# 按照索引树的顺序计算相应顺序的根
# def gen_zeta():
#
#     zass = [0] * 128
#     for ic in range(0, 128):
#         zass[ic] = mont * pow(17, int(tree[ic]), q) % q
#
#     return zass


# 对应于上面顺序根排列的逆根排列
# def gen_zetas_inv():
#     zetas_inv0 = [0] * 128
#
#     ic = 64
#     kc = 0
#     while ic != 0:
#         for j in range(ic, 2 * ic):
#             zetas_inv0[kc] = mont * pow(17, -int(tree[j]), q) % q
#             kc = kc + 1
#
#         ic = int(ic / 2)
#     zetas_inv0[127] = int(mont * (mont * (q - 1) * (q - 1) / 128 % q) % q)
#
#     return zetas_inv0


# 适配于ntt3的特殊乘法规则，不像一般的计算内积
def ntt3_mul(fff, ggg):
    new_vv = []

    # 每四个一组进行计算，共64组
    for ic in range(64):
        # 尽量保持计算时间一致
        r0, r1 = ntt3_mul0(fff[4 * ic + 0], fff[4 * ic + 1], ggg[4 * ic + 0], ggg[4 * ic + 1], zetas[64 + ic])
        r2, r3 = ntt3_mul0(fff[4 * ic + 2], fff[4 * ic + 3], ggg[4 * ic + 2], ggg[4 * ic + 3], -zetas[64 + ic])

        new_vv += [r0, r1, r2, r3]

    for ic in range(n):
        # new_vv[ic] = new_vv[ic] * (2**16 % q) % q
        new_vv[ic] = new_vv[ic] * 2285 % q
    return new_vv


# 分别计算实部和虚部的乘法
def ntt3_mul0(a0, a1, b0, b1, ze):

    # 两个虚部相乘
    r0 = (a1 * b1) * 169 % q
    r0 = (r0 * ze) * 169 % q
    # 加上两个实部相乘
    r0 += (a0 * b0) * 169 % q

    # 虚部和实部交叉相乘
    r1 = (a0 * b1) * 169 % q
    r1 += (a1 * b0) * 169 % q

    # 返回实部，虚部
    return r0, r1


# 第三种ntt变换，适配于Kyber参数集
def ntt3(vvv):
    new_v = [0] * len(vvv)
    for ic in range(0, len(vvv)):
        new_v[ic] = vvv[ic]

    kd, l = 1, 128

    while l >= 2:
        ind = 0
        while ind < n:
            zeta = zetas[kd]
            kd = kd + 1
            j = 0
            for j in range(ind, ind + l):
                t = (zeta * new_v[j + l]) * 169 % q
                new_v[j + l] = (new_v[j] - t)
                new_v[j] = (new_v[j] + t)
            ind = l + (j + 1)
        l = l >> 1

    for ic in range(0, len(vvv)):
        new_v[ic] = new_v[ic] % q

    return new_v


def intt3(vvv):
    new_v = [0] * len(vvv)
    for ic in range(0, len(vvv)):
        new_v[ic] = vvv[ic]

    l, l_upper = 2, 128
    kd = l_upper - 1
    while l <= 128:
        ind = 0
        while ind < n:
            zeta = zetas[kd]
            kd = kd - 1
            j = 0
            for j in range(ind, ind + l):
                t = new_v[j]
                new_v[j] = (t + new_v[j + l]) % q
                new_v[j + l] = (new_v[j + l] - t)
                new_v[j + l] = (zeta * new_v[j + l]) * 169 % q
            ind = j + l + 1
        l = l << 1

    for j in range(n):
        # new_v[j] = new_v[j] * 1441 * 169 * 169 % q
        new_v[j] = new_v[j] * 3303 % q

    return new_v


# 生成二叉树索引
# def gen_index_tree(nn):
#     ind_list = [0] * nn
#     tem = 2
#     ind_list[1] = nn / 2
#     nn = int(nn / 2)
#     while int(nn / 2) != 0:
#         nn = int(nn / 2)
#
#         for ic in range(tem, 2 * tem):
#             ind_list[ic] = ind_list[ic - tem] + nn
#         tem = tem * 2
#
#     return ind_list


# 计算ntt的系数表
# def cal_roots_ntt(ind):
#     tem = [0] * 1
#     tem[0] = -1 % q
#
#     while len(tem) < ind:
#
#         new_tem = [0] * (len(tem) * 2)
#         for ic in range(0, len(tem)):
#             tempt = sqr_q(tem[ic])
#             new_tem[2 * ic] = tempt[0]
#             new_tem[2 * ic + 1] = tempt[1]
#         tem = new_tem
#
#     return tem


# def exgcd(a, bd):
#     if bd == 0:
#         return 1, 0, a
#     else:
#         x, y, qq = exgcd(bd, a % bd)
#         x, y = y, (x - (a // bd) * y)
#         return x, y, qq


# 产生公钥pk与私钥sk
def Genkey(dd):

    if n & (n-1) != 0:
        raise ValueError("n值应为为2的幂次")

    if q != k*n+1:
        raise ValueError("q should be equal to k*n+1")

    for ic in range(2, int(math.sqrt(q))):
        if math.gcd(q, ic) > 1:
            raise ValueError("q should be prime")

    s = np.zeros([kk, n])
    e = np.zeros([kk, n])

    rho, sigma = G(dd)
    # print("rho:", rho)
    # print("sigma:", sigma)

    a = generate_mat_a(rho, kk)

    N = 0
    for ic in range(0, kk):
        input_bytes = PRF(sigma, bytes([N]), eta1)
        s[ic, :] = CBD(input_bytes, eta1)
        N = N + 1

    for ic in range(0, kk):
        e[ic, :] = CBD(PRF(sigma, bytes([N]), eta1), eta1)
        N = N + 1

    # 将随机阵用NTT包装一下作为私钥
    new_s = np.zeros([kk, n])
    new_e = np.zeros([kk, n])
    t = np.zeros([kk, n])

    for ic in range(0, kk):
        new_s[ic, :] = ntt3(s[ic, :])
        new_e[ic, :] = ntt3(e[ic, :])

    # 矩阵a在这一步没必要进行NTT变换
    vec = np.zeros([kk, kk, n])
    for ic in range(0, kk):
        for j in range(0, kk):
            vec[ic, j, :] = ntt3_mul(a[ic, j, :], new_s[j, :])

    tem = np.zeros([kk, n])
    for ic in range(0, kk):
        for ii in range(0, n):
            for j in range(0, kk):

                tem[ic, ii] = tem[ic, ii] + vec[ic, j, ii]

            t[ic, ii] = (tem[ic, ii] + new_e[ic, ii]) % q

    pk_cpa = encode([t], 12)

    pk_cpa = bits_to_bytes(pk_cpa)
    pk_cpa = binascii.hexlify(pk_cpa + rho)

    sk_cpa = encode([new_s], 12)
    sk_cpa = bits_to_bytes(sk_cpa)
    sk_cpa = binascii.hexlify(sk_cpa)

    return [pk_cpa, sk_cpa]


# 加密函数
def Enc(pk_cpa, ran_m, rand):
    rand = binascii.unhexlify(rand)
    ran1 = hex_to_bits(binascii.hexlify(ran_m))

    ran = [0] * n
    for i in range(n):
        ran[i] = int(ran1[i])

    pk_cpa = binascii.unhexlify(pk_cpa)

    newt = pk_cpa[:-32]
    rho = pk_cpa[-32:]
    newt = binascii.hexlify(newt)
    newt = hex_to_bits(newt)
    newt = decode(newt, 12)

    for ic in range(0, len(ran)):
        if ran[ic] != 0 and ran[ic] != 1:
            raise ValueError("m[i] should be 0 or 1")

    for ic in range(0, n):
        ran[ic] = ran[ic] * (int(q/2) + 1)

    newa = generate_mat_a(rho, kk)
    for ii in range(0, kk):
        for jj in range(ii + 1, kk):
            for ll in range(0, n):
                tem = newa[jj, ii, ll]
                newa[jj, ii, ll] = newa[ii, jj, ll]
                newa[ii, jj, ll] = tem

    N = 0
    # 三个随机误差均由字节串r导出
    rr = np.zeros([kk, n])
    # 小系数误差
    e1 = np.zeros([kk, n])
    for ic in range(0, kk):
        input_bytes = PRF(rand, bytes([N]), eta1)
        rr[ic, :] = CBD(input_bytes, eta1)
        N = N + 1
    for ic in range(0, kk):
        e1[ic, :] = CBD(PRF(rand, bytes([N]), eta2), eta2)
        N = N + 1

    e2 = CBD(PRF(rand, bytes([N]), eta2), eta2)

    new_r = np.zeros([kk, n])
    for ic in range(0, kk):
        new_r[ic, :] = ntt3(rr[ic, :])

    # 产生密文
    # 计算A*NTT(r)
    newu = np.zeros([kk, n])

    vec = np.zeros([kk, kk, n])
    for ic in range(0, kk):
        for j in range(0, kk):
            vec[ic, j, :] = ntt3_mul(newa[ic, j, :], new_r[j, :])

    for ic in range(0, kk):
        for ii in range(0, n):
            for j in range(0, kk):
                newu[ic, ii] = newu[ic, ii] + vec[ic, j, ii]
            newu[ic, ii] = newu[ic, ii] % q

    u = np.zeros([kk, n])

    for ic in range(0, kk):
        u[ic, :] = intt3(newu[ic, :])
        for j in range(0, n):
            u[ic, j] = (u[ic, j] + e1[ic, j]) % q
    # 计算v
    v = [0] * n
    newv = [0]*n
    vec = np.zeros([kk, n])
    for ic in range(0, kk):
        vec[ic, :] = ntt3_mul(newt[ic, :], new_r[ic, :])

    for ic in range(0, n):
        for kd in range(0, kk):
            newv[ic] = newv[ic] + vec[kd, ic]

    newv = intt3(newv)

    for ic in range(0, n):

        newv[ic] = newv[ic] + e2[ic]
        v[ic] = (newv[ic] + ran[ic]) % q

    for ic in range(0, kk):
        for j in range(0, n):
            u[ic, j] = compress(u[ic, j], du)
    for ic in range(0, n):
        v[ic] = compress(v[ic], dv)

    u_code = encode([u], du)
    u_code = bits_to_bytes(u_code)

    v_code = encode([[v]], dv)
    v_code = bits_to_bytes(v_code)

    uv_code = binascii.hexlify(u_code + v_code)

    return uv_code


# 解密函数
def Dec(uv_code, sk_cpa):
    # print("Cipher:", uv_code)
    sk_cpa = binascii.unhexlify(sk_cpa)
    sk_cpa = binascii.hexlify(sk_cpa)
    sk_cpa = hex_to_bits(sk_cpa)
    sk_cpa = decode(sk_cpa, 12)

    uv_code = binascii.unhexlify(uv_code)
    uv_code = binascii.hexlify(uv_code)
    # print("length of Cipher:", int(len(uv_code)/2))
    ud = uv_code
    ud = hex_to_bits(ud)
    ud = decode(ud, du)

    vd = uv_code[int(kk * n * du / 4):]

    vd = hex_to_bits(vd)

    v = decode(vd, dv)

    for ic in range(0, kk):
        for j in range(0, n):
            ud[ic, j] = decompress(ud[ic, j], du)

    v = v[0]
    for ic in range(0, n):
        v[ic] = decompress(v[ic], dv)

    dem = [0] * n
    vv = [0] * n
    newu = np.zeros([kk, n])
    for ic in range(0, kk):
        newu[ic, :] = ntt3(ud[ic, :])

    vec = np.zeros([kk, n])
    for ic in range(0, kk):
        vec[ic, :] = ntt3_mul(sk_cpa[ic, :], newu[ic, :])

    for ic in range(0, n):
        for kd in range(0, kk):
            vv[ic] = vv[ic] + vec[kd, ic]
        vv[ic] = vv[ic] % q

    xx = intt3(vv)

    for ic in range(0, n):
        dem[ic] = (v[ic] - xx[ic]) % q

    for ic in range(0, n):
        dem[ic] = compress(dem[ic], 1)

    return dem


# 打乱函数之一，用于生成矩阵A，第二第三个变量为整数，但是需要转化为字节的形式
def XOF(bytes32, int_a, int_b):

    int_a, int_b = bytes([int_a]), bytes([int_b])

    input_bytes = bytes32 + int_a + int_b

    if len(input_bytes) != 34:
        raise ValueError("Length of input bytes should be equal to 32")

    return shake_128(input_bytes).digest(3 * n)


# 由种子生成随机矩阵，方阵中的每个元素都是一个长度为n的多项式
def generate_mat_a(rho, len_a):
    mat_A = np.zeros([len_a, len_a, n])
    for j in range(len_a):
        for ic in range(len_a):
            tem = XOF(rho, ic, j)
            mat_A[j, ic, :] = Parse(tem)

    return mat_A


# 打乱函数之一
def G(bytes32):

    # print(bytes32)
    output = sha3_512(bytes32).digest()
    # print("hash:", output)

    return output[:32], output[32:]


# 将字节转化为多项式的系数，对应于文档的算法1
# 生成的多项式属于NTT域，低次项系数在前
def Parse(bytes96):

    ii, jj = 0, 0
    coeff = [0] * n

    while jj < n:
        d1 = bytes96[ii] + 256 * (bytes96[ii + 1] % 16)
        d2 = (bytes96[ii + 1] // 16) + 16 * bytes96[ii + 2]

        if d1 < q:
            coeff[jj] = d1
            jj = jj + 1

        if d2 < q and jj < n:
            coeff[jj] = d2
            jj = jj + 1

        ii = ii + 3

    return coeff


# 多项式编码到字节串，文档算法3的逆算法
def encode(fff, l):

    fff_bytes = ''
    # 先生成比特串，然后利用bits_to_bytes函数还原回字节串

    for jj in range(0, len(fff[0])):
        for ii in range(0, n):
            fff_bytes = fff_bytes + format(int(fff[0][jj][ii]), f'0{l}b')[::-1]

    return fff_bytes


# 将字节串解码成多项式，输入的字节数是32的倍数
def decode(fff_bits, l):
    # 判断输入的字节串应当被翻译为多少个多项式
    ind = int(len(fff_bits) / (l*256))

    rr = list(fff_bits)

    coeff = np.zeros([ind, n])

    for hh in range(0, ind):
        for ii in range(0, n):
            for jj in range(0, l):
                coeff[hh, ii] = coeff[hh, ii] + int(rr[n * l * hh + ii * l + jj]) * (2**jj)

    return coeff


# 按照文档中的规则将字节串切割为比特串
def hex_to_bits(hex_str):
    hex_str = hex_str.decode('utf-8') if isinstance(hex_str, bytes) else hex_str
    hex_pairs = [hex_str[ic:ic+2] for ic in range(0, len(hex_str), 2)]
    bit_str = ''

    for hex_pair in hex_pairs:
        byte = int(hex_pair, 16)  # 转换为整数
        tem = format(byte, '08b')  # 转换为比特串
        bit_str = bit_str + tem[::-1]

    return bit_str


# 将比特串按照规则还原为字节串
def bits_to_bytes(ss):

    ind = int(len(ss)/8)
    byte32 = bytes()

    for ii in range(0, ind):

        tem = int(ss[ii * 8: (ii + 1) * 8][::-1], 2)

        byte32 = byte32 + bytes([tem])

    return byte32


# 将输入比特串修改为固定长度
def kdf(in_str, length):

    return shake_256(in_str).digest(length)


# 生成第三种ntt所需的预计算数据，仅适用于(3329, 256, 13)这一参数集
# tree = gen_index_tree(128)
tree = [0, 64.0, 32, 96.0, 16, 80.0, 48, 112.0, 8, 72.0, 40, 104.0, 24, 88.0, 56, 120.0, 4, 68.0, 36, 100.0, 20, 84.0,
        52, 116.0, 12, 76.0, 44, 108.0, 28, 92.0, 60, 124.0, 2, 66.0, 34, 98.0, 18, 82.0, 50, 114.0, 10, 74.0, 42,
        106.0, 26, 90.0, 58, 122.0, 6, 70.0, 38, 102.0, 22, 86.0, 54, 118.0, 14, 78.0, 46, 110.0, 30, 94.0, 62, 126.0,
        1, 65.0, 33, 97.0, 17, 81.0, 49, 113.0, 9, 73.0, 41, 105.0, 25, 89.0, 57, 121.0, 5, 69.0, 37, 101.0, 21, 85.0,
        53, 117.0, 13, 77.0, 45, 109.0, 29, 93.0, 61, 125.0, 3, 67.0, 35, 99.0, 19, 83.0, 51, 115.0, 11, 75.0, 43,
        107.0, 27, 91.0, 59, 123.0, 7, 71.0, 39, 103.0, 23, 87.0, 55, 119.0, 15, 79.0, 47, 111.0, 31, 95.0, 63, 127.0]

# mont = int(pow(2, 16, q))
mont = 2285

# mont_inv = exgcd(mont, q)[0] % q
mont_inv = 169

# zetas = gen_zeta()
zetas = [2285, 2571, 2970, 1812, 1493, 1422, 287, 202, 3158, 622, 1577, 182, 962, 2127, 1855, 1468, 573, 2004, 264, 383,
         2500, 1458, 1727, 3199, 2648, 1017, 732, 608, 1787, 411, 3124, 1758, 1223, 652, 2777, 1015, 2036, 1491, 3047,
         1785, 516, 3321, 3009, 2663, 1711, 2167, 126, 1469, 2476, 3239, 3058, 830, 107, 1908, 3082, 2378, 2931, 961,
         1821, 2604, 448, 2264, 677, 2054, 2226, 430, 555, 843, 2078, 871, 1550, 105, 422, 587, 177, 3094, 3038, 2869,
         1574, 1653, 3083, 778, 1159, 3182, 2552, 1483, 2727, 1119, 1739, 644, 2457, 349, 418, 329, 3173, 3254, 817,
         1097, 603, 610, 1322, 2044, 1864, 384, 2114, 3193, 1218, 1994, 2455, 220, 2142, 1670, 2144, 1799, 2051, 794,
         1819, 2475, 2459, 478, 3221, 3021, 996, 991, 958, 1869, 1522, 1628]

# zetas_inv = gen_zetas_inv()
zetas_inv = [1701, 1807, 1460, 2371, 2338, 2333, 308, 108, 2851, 870, 854, 1510, 2535, 1278, 1530, 1185, 1659, 1187,
             3109, 874, 1335, 2111, 136, 1215, 2945, 1465, 1285, 2007, 2719, 2726, 2232, 2512, 75, 156, 3000, 2911,
             2980, 872, 2685, 1590, 2210, 602, 1846, 777, 147, 2170, 2551, 246, 1676, 1755, 460, 291, 235, 3152, 2742,
             2907, 3224, 1779, 2458, 1251, 2486, 2774, 2899, 1103, 1275, 2652, 1065, 2881, 725, 1508, 2368, 398, 951,
             247, 1421, 3222, 2499, 271, 90, 853, 1860, 3203, 1162, 1618, 666, 320, 8, 2813, 1544, 282, 1838, 1293,
             2314, 552, 2677, 2106, 1571, 205, 2918, 1542, 2721, 2597, 2312, 681, 130, 1602, 1871, 829, 2946, 3065,
             1325, 2756, 1861, 1474, 1202, 2367, 3147, 1752, 2707, 171, 3127, 3042, 1907, 1836, 1517, 359, 758, 1441]


def CCA_KeyGen():
    dd = random.randbytes(32)

    cca_pk, sk2 = Genkey(dd)

    H_cca_pk = H(cca_pk)

    z = random.randbytes(32)
    z = binascii.hexlify(z)

    cca_sk = binascii.unhexlify(sk2 + cca_pk + H_cca_pk + z)
    cca_sk = binascii.hexlify(cca_sk)

    return cca_pk, cca_sk


def CCA_Enc(cca_pk, m_unhex):
    m_hash = binascii.unhexlify(H(binascii.hexlify(m_unhex)))

    K_bar, rand = G(m_hash + binascii.unhexlify(H(cca_pk)))

    rand = binascii.hexlify(rand)

    c_text = Enc(cca_pk, m_hash, rand)

    K_key = kdf(K_bar + binascii.unhexlify(H(c_text)), 32)

    return c_text, K_key


def CCA_Dec(c_text, cca_sk):

    cpa_sk = cca_sk[0: 3 * kk * n]
    cpa_pk = cca_sk[3 * kk * n: 6 * kk * n + 64]
    H_cca_pk = cca_sk[6 * kk * n + 64: 6 * kk * n + 128]
    z = cca_sk[-6 * kk * n + 128:]

    m2 = Dec(c_text, cpa_sk)
    new_m2 = ''.join([str(i) for i in m2])

    m2 = bits_to_bytes(new_m2)

    K_bar, rand = G(m2 + binascii.unhexlify(H_cca_pk))
    rand = binascii.hexlify(rand)

    c2 = Enc(cpa_pk, m2, rand).decode('utf-8')
    if not isinstance(c_text, str):
        c_text = c_text.decode('utf-8')

    if c2 == c_text:
        return kdf(K_bar + binascii.unhexlify(H(c_text)), 32)

    else:
        print("错了")
        return kdf(binascii.unhexlify(z) + binascii.unhexlify(H(c_text)), 32)


if __name__ == "__main__":

    cca_pk1, cca_sk1 = CCA_KeyGen()
    print("cca_pk:", cca_pk1)
    print("cca_sk:", cca_sk1)
    new_m = random.randbytes(32)

    Cipher, scr_key = CCA_Enc(cca_pk1, new_m)
    print("Cipher:", Cipher)
    print("K1:", scr_key)
    new_k = CCA_Dec(Cipher, cca_sk1)
    print("K2:", new_k)
