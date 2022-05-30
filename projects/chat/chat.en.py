import requests
import sys#, os

server_ip = "46.35.186.220"
has_profile = requests.get(f"http://{server_ip}/index.php")
errormsg = ""


if has_profile.text == "false":
    print("New IP address. You're not registered.\nPlease choose user name\n(only letters and digits, up to 30, no spaces, underscores and other symbols)")
    nick = input()
    if nick.isalnum() and len(nick) <= 30:
        chat = requests.get(f"http://{server_ip}/index.php?register=" + nick)
        if chat.text == "okay":
            print("Registration successful! Please rerun the script to enter the chat.")
            #input()
        else:
            print("There was a server-side error! Please report to admin!\n(or maybe you've messed around ;)")
            #input()
    else:
        print("The name doesn't fit the requirements! Please rerun the script and try again!")
        #input()
else:
    #_ = os.system('cls')
    usrname = requests.get(f"http://{server_ip}/{has_profile.text}.txt")
    print(f"Hello, {usrname.text}!\nPlease keep in mind the chat doesn't support messages larger than 160 symbols!\nPress Enter to continue...")
    input()
    while True:
        #_ = os.system('cls')
        chat = requests.get(f"http://{server_ip}/chat.txt")
        chat_printable = chat.text.replace("@@","\n")
        print(chat_printable)
        if errormsg != "":
            print(errormsg)
            errormsg = ""
        print(f"Press Enter to refresh. Type something to make a message. Type exit to quit.\n{usrname.text}: ",end="")
        while True:
            command = input()
            if command == "":
                break
            elif command == "exit":
                sys.exit()
            else:
                if len(command) <= 160:
                    command = command.replace("@","")
                    x = requests.post(f"http://{server_ip}/index.php", data={'msg': command})
                    break
                else:
                    errormsg = "The message can't contain more than 160 symbols!"
                    break