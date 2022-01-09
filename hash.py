"""ハッシュ値の生成."""
import hashlib


def sample01():
    """
    helloをハッシュ化
    :return: なし
    """

    hash_hello = hashlib.sha256(b"hello").hexdigest()
    hash_hallo = hashlib.sha256(b"hallo").hexdigest()
    hash_helloworld = hashlib.sha256(b"hello world!").hexdigest()
    print(hash_hello)
    print(hash_hallo)
    print(hash_helloworld)


if __name__ == "__main__":
    sample01()
