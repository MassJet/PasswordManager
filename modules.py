def printheader():
    """
    Prints Header for app

    """
    print("-------------------------------------")
    print("       Simple Password Manager")
    print("-------------------------------------")


def maineventloop():
    """
    Main event loop that interacts with user

    """
    while True:
        cmd = input("Will you [L]ist your passwords, [W]rite a password, or E[x]it the manager?").strip().lower()
        if cmd == 'l':
            listpassword()
        elif cmd == 'w':
            writepassword()
        elif cmd == 'x':
            break


def listpassword():
    """
    Lists your passwords

    """
    print('list p[asswrod')

def writepassword():
    """
    Writes password to pswd.bat file

    """
    print('list password')
