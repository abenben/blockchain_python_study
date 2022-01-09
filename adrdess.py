import hashlib
import os
import binascii

import base58
import ecdsa


def make_private_key():
    """秘密鍵生成

    秘密鍵を生成する.
    :return: 秘密鍵
    """

    private_key = os.urandom(32)

    print(private_key)
    print(binascii.hexlify(private_key))
    return private_key


def make_public_key(private_key):
    """公開鍵生成

    秘密鍵から公開鍵を生成する.
    :param private_key: 秘密鍵
    :return: 公開鍵
    """

    print(binascii.hexlify(private_key))
    public_key = ecdsa.SigningKey.from_string(private_key, ecdsa.SECP256k1).verifying_key.to_string()
    print(binascii.hexlify(public_key))

    public_key_y = int.from_bytes(public_key[32:], "big")

    if public_key_y % 2 == 0:
        public_key_conpressed = b"\x02" + public_key[32:]
    else:
        public_key_conpressed = b"\x02" + public_key[32:]

    print(binascii.hexlify(public_key_conpressed))

    return public_key


def make_address(public_key):
    """アドレス生成
    

    :param public_key:公開鍵 
    :return: アドレス
    """

    print(binascii.hexlify(public_key))

    # バージョンバイト＋公開鍵のハッシュ値
    prefix_and_pubkey = b"\x04" + public_key

    intermediate = hashlib.sha256(prefix_and_pubkey).digest()
    repemd160 = hashlib.new('ripemd160')
    repemd160.update(intermediate)
    hash160 = repemd160.digest()

    prefix_and_hash160 = b"\x00" + hash160

    # Double-SHA256のハッシュ値
    # hashlib.sha256が入れ子になっていることを確認！
    double_hash = hashlib.sha256(hashlib.sha256(prefix_and_hash160).digest()).digest()

    # 先頭４バイトチェックサム
    checksum = double_hash[:4]

    # バージョンバイト＋公開鍵のハッシュ値とチェックサムを連結
    pre_address = prefix_and_hash160 + checksum
    # Base58エンコード
    address = base58.b58encode(pre_address)

    print(address.decode())

    return address


if __name__ == '__main__':
    """
    メイン処理
    """

    private_key = make_private_key()
    public_key = make_public_key(private_key)
    address = make_address(public_key)
