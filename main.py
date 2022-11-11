import modules as modules


i = 0
success = bool()

def main():
    global i, success
    # Print header
    modules.printheader()
    # Authenticate using keyring
    print("In order to continue, enter your master password")
    while i <= 5 and success == False:
        success = modules.auth()[0]
        i+=1;
    # Call main event loop
    modules.maineventloop()


if __name__ == '__main__':
    main()
