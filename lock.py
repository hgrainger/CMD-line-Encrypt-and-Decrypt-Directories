import os, os.path
from Crypto import Random
from Crypto.Cipher import AES

key = b'\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18'

def pad(s):
    return s + b"\0" * (AES.block_size - len(s) % AES.block_size)


def encrypt(message, key, key_size=256):
    message = pad(message)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return iv + cipher.encrypt(message)


def encrypt_file(file_name, key):
    with open(file_name, 'rb') as fo:
        plaintext = fo.read()
    enc = encrypt(plaintext, key)
    with open(file_name + ".enc", 'wb') as fo:
        fo.write(enc)
        os.remove(file_name)


def dir_to_encrypt(destdir):
    files = [ f for f in os.listdir(destdir) if os.path.isfile(os.path.join(destdir,f)) ]
    for f in files:
        encrypt_file("%s%s" % (destdir,f), key)

dir = raw_input("Please enter the Directories Full Path to Encrypt: ")

dir_to_encrypt(dir)





