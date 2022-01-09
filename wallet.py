"""ウォレット."""
import os
import binascii
import ecdsa
import hmac
import hashlib

seed = os.urandom(32)
root_key = b"Bitcoin seed"
