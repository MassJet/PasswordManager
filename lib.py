from hashlib import pbkdf2_hmac
import keyring, platform, sys, json, os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from os.path import expanduser
import base64

from typing import Tuple


CONF = str()
MASTER = str()


if "macos" or "linux" in platform.platform().lower():
    CONF = expanduser("~")+"/.sb/"
else: 
    sys.stderr.write("No preset config path for windows yet! Please enter Config path to use: ")
    sys.stderr.flush()
    CONF = input()
def printheader():
    
    print("-------------------------------------")
    print("             MassPass         ")
    print("-------------------------------------")


def auth() -> Tuple[bool, str]:
    global MASTER
    import getpass
    user_input = getpass.getpass()
    MASTER = keyring.get_password('sbTokenService', 'sb')
    if user_input == MASTER:
        return (True, MASTER)
    else: return (False, str())
# Interact w/ user event loop
def maineventloop():
    
    while True:
        cmd = input("Choose one of the following commands: [l]ist, [a]dd, [g]et, [r]emove, [c]onfig, e[x]it:\t").strip().lower()
        if cmd == 'l':
            list_pws(MASTER)
        elif cmd == 'w':
            write_pw()
        elif cmd == 'x':
            print("Goodbye!")
            quit(0)

# list all passwords
def list_pws(master: str):
    #TODO
    pass
    
# write a password
def write_pw():
    print('list password')

