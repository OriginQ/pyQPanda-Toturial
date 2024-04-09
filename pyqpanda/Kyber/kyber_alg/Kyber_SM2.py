#!/usr/bin/env python
# -*- coding: utf-8 -*-
# cython: language_level=3


from . import Kyber
import random
from typing import Tuple
import binascii
from pysmx.SM2 import generate_keypair
from pysmx.SM2 import Encrypt
from pysmx.SM2 import Decrypt
from pysmx.SM3 import SM3
from pysmx.SM3 import hash_msg
from gmssl import sm4


def key_gen_hybrid() -> Tuple[str, str]:
    """
    Generates the public key and private key for the hybrid encryption scheme.

    Returns:
        Tuple containing the public key and private key.
        - pk (bytes): Public key containing two parts of information.
        - sk (bytes): Private key containing two parts of information,
          private key for Kyber algorithm and private key for SM2 encryption.
    """

    len_para = 64
    KEYs = Kyber.CCA_KeyGen()
    # 公钥包含两部分，等式左侧信息与矩阵信息
    pk1, sk1 = [KEYs[0]], KEYs[1]
    pk1 = pk1[0]

    pk2, sk2 = generate_keypair(len_para)

    pk2 = binascii.hexlify(pk2)
    sk2 = binascii.hexlify(sk2)

    return (pk1 + pk2).decode('utf-8'), (sk1 + sk2).decode('utf-8')


def enc_hybrid(pk: str):
    """
    Encrypts the given message using the hybrid encryption scheme.

    Args:
        - pk (bytes): Public key containing two parts of information, Kyber pk || SM2 pk .
        - msg (list): List of messages to be encrypted.

    Returns:
        Tuple containing the encrypted ciphertext, symmetric key, and encrypted message.
        - c_text (bytes): Encrypted ciphertext containing two parts of information,
          ciphertext encrypted using Kyber algorithm and ciphertext encrypted using SM2 encryption.
        - sym_key (str): Symmetric key used for encryption.
        - msg_enc (list): Encrypted message.
    """

    pk1 = pk[0: 1600]
    pk2 = pk[-128:]

    len_para = 64
    pk2 = binascii.unhexlify(pk2)
    if len(pk2) != 64 or len(pk1) != 1600:
        raise TypeError("pk error!")

    info11 = random.randbytes(32)
    info11 = info11.hex()

    # 密钥产生
    m1 = random.randbytes(32)
    c_text1, K_key = Kyber.CCA_Enc(pk1, m1)

    sec_K = binascii.hexlify(K_key).decode('utf-8')

    info0 = info11 + sec_K
    info0 = binascii.unhexlify(info0)
    sm33 = SM3()
    sm33.update(info0)
    sym_key = sm33.hexdigest()

    info11 = binascii.unhexlify(info11)
    c_text2 = Encrypt(info11, pk2, len_para, 0)

    c_text2 = binascii.hexlify(c_text2)
    sym_iv = sym_key[32:]

    sym_key = xor_hex_strings(sym_key[0:32], sym_key[32:])

    return c_text1, c_text2, sym_key, sym_iv


def dec_hybrid(c_text1, c_text2, sk) -> [str, str]:
    """
    Decrypts the given ciphertext using the hybrid encryption scheme.

    Args:
        - c_text (bytes): Ciphertext to be decrypted, containing two parts of information,
          ciphertext encrypted using Kyber algorithm and ciphertext encrypted using SM2 encryption.
        - sk (bytes): Private key containing two parts of information,
          private key for Kyber algorithm and private key for SM2 encryption.
        - msg_enc (list): Encrypted message.

    Returns:
        Decrypted message.
    """

    sk1 = sk[:3264]
    sk2 = sk[3264:]

    sk2 = binascii.unhexlify(sk2)
    c_text2 = binascii.unhexlify(c_text2)

    len_para = 64

    sec_E = Decrypt(c_text2, sk2, len_para)
    sec_E = binascii.hexlify(sec_E).decode()

    sec_K = Kyber.CCA_Dec(c_text1, sk1)

    sec_K = binascii.hexlify(sec_K).decode('utf-8')
    # print("sec_K:", sec_K)
    # print("sec_E:", sec_E)

    info1 = sec_E + sec_K
    info1 = binascii.unhexlify(info1)
    sm3 = SM3()
    sm3.update(info1)
    sym_key = sm3.hexdigest()
    # print("sm3_hashed:", sym_key)

    IV = sym_key[32:]

    sym_key = xor_hex_strings(sym_key[0:32], sym_key[32:])

    return sym_key, IV


def xor_hex_strings(hex_str1: str, hex_str2: str):
    """
    Performs a bitwise XOR operation on two hexadecimal strings.

    Args:
        hex_str1 (str): The first hexadecimal string.
        hex_str2 (str): The second hexadecimal string.

    Returns:
        The result of the XOR operation as a hexadecimal string.
    """
    # 将16进制字符串转换为字节串
    bytes1 = bytes.fromhex(hex_str1)
    bytes2 = bytes.fromhex(hex_str2)

    # 对字节串进行逐位异或操作
    result_bytes = bytes(x ^ y for x, y in zip(bytes1, bytes2))

    # 将结果转换为16进制字符串
    result_hex_str = result_bytes.hex()

    return result_hex_str


def sm4_encode(key, IV, data):

    """
    Encrypts the given data using the SM4 encryption algorithm.

    Args:
        key (str): The encryption key.
        data (str): The data to be encrypted.

    Returns:
        The encrypted data as a hexadecimal string.
        :param key:
        :param data:
        :param IV:
    """

    sm4Alg = sm4.CryptSM4()
    key = binascii.unhexlify(key.encode('utf-8'))
    IV = binascii.unhexlify(IV)
    sm4Alg.set_key(key, sm4.SM4_ENCRYPT)
    dateStr = data
    enRes = sm4Alg.crypt_cbc(IV, dateStr.encode())
    enHexStr = enRes.hex()

    return enHexStr


def sm4_decode(key, IV, data):

    sm4Alg = sm4.CryptSM4()
    key = binascii.unhexlify(key.encode('utf-8'))
    IV = binascii.unhexlify(IV)
    sm4Alg.set_key(key, sm4.SM4_DECRYPT)
    deRes = sm4Alg.crypt_cbc(IV, bytes.fromhex(data))
    deHexStr = deRes.decode()

    return deHexStr


if __name__ == "__main__":

    # 混合加密第一环节************************************************************************************
    pk0, sk0 = key_gen_hybrid()
    print("pk:", pk0)
    print("sk:", sk0)

    # 混合加密第二阶段************************************************************************************

    cipher0, cipher1, key0, iv = enc_hybrid(pk0)

    print("cipher1:", cipher0)
    print("cipher2:", cipher1)
    print("sym_key:", key0)
    print("sym_iv:", iv)

    text = 'hello OriginQ![\%tdy se76s66443a5hfd$nnn]'
    c_text = sm4_encode(key0, iv, text)

    # 混合加密的第三环节*********************************************************************************
    key0, iv = dec_hybrid(cipher0, cipher1, sk0)
    print("sym_key:", key0)
    print("sym_iv:", iv)

    print("cipher3(SM4_CBC):", c_text)
    cc_text = sm4_decode(key0, iv, c_text)
    print("明文：", cc_text)
