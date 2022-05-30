import requests
import sys

server_ip = "46.35.186.220"
has_profile = requests.get(f"http://{server_ip}/index.php")
errormsg = ""

if has_profile.text == "false":
    print("Нов IP адрес. Нямате профил.\nМоля напишете потребителско име\n(само цифри и букви на латиница, до 30 на брой, без долни черти, разстояния и други символи)")
    nick = input()
    if nick.isalnum() and len(nick) <= 30:
        chat = requests.get(f"http://{server_ip}/index.php?register=" + nick)
        if chat.text == "okay":
            print("Регистрацията беше успешна! Моля изпълнете скрипта наново, за да влезете в чата")
        else:
            print("Имаше грешка от страна на сървъра. Моля докладвайте на админа!\n(или пък сте барникали в python кода ;)")
    else:
        print("Името не спазва поставените ограничения! Моля изпълнете скрипта отново и опитайте пак!")
else:
    usrname = requests.get(f"http://{server_ip}/{has_profile.text}.txt")
    print(f"Добре дошъл, {usrname.text}!\nИмай впредвид, че чатът не поддържа кирилица и съобщения над 160 символа!\nНатисни Enter, за да продължиш...")
    input()
    while True:
        chat = requests.get(f"http://{server_ip}/chat.txt")
        chat_printable = chat.text.replace("@@","\n")
        print(chat_printable)
        if errormsg != "":
            print(errormsg)
            errormsg = ""
        print(f"Натисни Enter за да опресниш чата. Напиши нещо за да пратиш съобщение. Напиши exit за да излезеш.\n{usrname.text}: ",end="")
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
                    errormsg = "Съобщението не може да съдържа над 160 символа!"
                    break