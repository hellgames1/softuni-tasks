import os, sys

directory = os.listdir()
directory.remove(os.path.basename(__file__))
newdir = os.listdir()
newdir.remove(os.path.basename(__file__))
i = 0


print("Добре дошъл в скрипта за промяна на имена на файлове.\nСимволите @@ ще бъдат автоматично заменяни с индекса на файла, започващ от 1.\nИзбери какви действия искаш да предприемеш:")

while True:
    i+=1
    print(f"Действие номер {i}: \n1) замени текст с друг текст\n2) добави текст в началото на имената\n3) добави текст в края на имената\n4) замени целите имена с нещо\nИзбери: ", end="")
    command = input()
    if command != "1" and command != "2" and command != "3" and command != "4":
        i-=1
        print("Няма такава опция!")
        continue
    else:
        if command == "1":
            print("Какъв текст да заменя? ", end="")
            changes_from = input()
            print("С какъв текст да го заменя? ", end="")
            changes_to = input()
            for j in range(len(newdir)):
                newdir[j] = newdir[j].replace(changes_from.replace("@@",str(j+1)), changes_to.replace("@@",str(j+1)))
        elif command == "2":
            print("Какъв текст да добавя в началото на имената? ", end="")
            changes_from = input()
            changes_to = "null"
            for j in range(len(newdir)):
                newdir[j] = changes_from.replace("@@",str(j+1)) + newdir[j]
        elif command == "3":
            print("Какъв текст да добавя в края на имената? ", end="")
            changes_from = input()
            print("Преди разширението ли да бъде? 1)да 2)не ", end="")
            changes_to = input()

            for j in range(len(newdir)):
                if changes_to == "1":
                    ext=newdir[j][newdir[j].rfind('.'):]
                    newdir[j] = newdir[j][:newdir[j].rfind('.')]
                else:
                    ext=""
                newdir[j] = newdir[j] + changes_from.replace("@@",str(j+1)) + ext
        elif command == "4":
            print("С какво да заменя целите имена? За нумерация може да използваш символите @@")
            changes_from = input()
            print("Да запазя ли разширенията? 1)да 2)не ", end="")
            changes_to = input()
            for j in range(len(newdir)):
                if changes_to == "1":
                    ext=newdir[j][newdir[j].rfind('.'):]
                else:
                    ext=""
                newdir[j] = changes_from.replace("@@",str(j+1))+ext
        print("Добре! ", end="")
        while True:
            print("Сега?\n1) визуализирай промените до сега\n2) добави следващо действие\n3) готово! приложи промените и излез\nИзбери: ",end="")
            subcommand = input()
            if subcommand != "1" and subcommand != "2" and subcommand != "3":
                print("Няма такава опция!")
                continue
            if subcommand == "1":
                for j in range(len(directory)):
                    print(f"{directory[j]}  -->  {newdir[j]}")
            elif subcommand == "2":
                break
            elif subcommand == "3":
                for j in range(len(directory)):
                    try:
                        os.rename(directory[j], newdir[j])
                    except:
                        print(f"Грешка! Не можах да преименувам файлът {directory[j]}\nВероятно е недостъпен, използва се от друга програма в момента, или вече не съществува!")
                        print("Натисни Enter, за да излезеш от програмата...")
                        input()
                        sys.exit()
                    print(f"Преименуван файл {j+1} от {len(directory)}!")
                print("Натисни Enter, за да излезеш от програмата...")
                input()
                sys.exit()
