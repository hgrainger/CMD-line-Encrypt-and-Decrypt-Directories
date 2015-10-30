import os, os.path
import Tkinter as tkinter
import tkMessageBox as mbox
from Crypto.Cipher import AES

key = b'\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18'

def pad(s):
    return s + b"\0" * (AES.block_size - len(s) % AES.block_size)


def decrypt(ciphertext, key):
    iv = ciphertext[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext[AES.block_size:])
    return plaintext.rstrip(b"\0")


def decrypt_file(file_name, key):
    with open(file_name, 'rb') as fo:
        ciphertext = fo.read()
    dec = decrypt(ciphertext, key)
    with open(file_name[:-4], 'wb') as fo:
        fo.write(dec)
        os.remove(file_name)

def alert():
    window = tkinter.Tk()
    window.wm_withdraw()
    mbox.showinfo('Important Message','Now Decrypted')

def dir_to_decrypt(destdir):
    files = [ f for f in os.listdir(destdir) if os.path.isfile(os.path.join(destdir,f)) ]
    for f in files:
        decrypt_file("%s%s" % (destdir,f), key)

dir = raw_input("Please enter the Directories Full Path to Decrypt: ")

dir_to_decrypt(dir)

alert()





