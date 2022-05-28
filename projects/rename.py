import os, sys
# създава списъци с файловете в директорията, като маха името на самия скрипт от този списък, тей като не може да преименува себе си
directory = os.listdir()
directory.remove(os.path.basename(__file__))
newdir = os.listdir()
newdir.remove(os.path.basename(__file__))
i = 0


print("Добре дошъл в скрипта за промяна на имена на файлове.\nИзбери какви действия искаш да предприемеш:")
# основен цикъл - всяка итерация на този цикъл е една промяна, която се записва да бъде изпълнена накрая
while True:
    i+=1
    print(f"Действие номер {i}: \n1) замени текст с друг текст\n2) добави текст в началото на имената\n3) добави текст в края на имената\nИзбери: ", end="")
    command = input()
    # ако напишеш нещо друго освен 1,2 3, върти наново цикъла
    # намалява i с 1, за да може после като се изпълни i+=1 да е същото, тей като още нищо не си направил
    if command != "1" and command != "2" and command != "3":
        i-=1
        print("Няма такава опция!")
        continue
    else:
    # ако си дал правилна команда, в зависимост от нея се променят имената във втория списък newdir[]
        if command == "1":
            print("Какъв текст да заменя? ", end="")
            changes_from = input()
            print("С какъв текст да го заменя? ", end="")
            changes_to = input()

            for j in range(len(newdir)):
                newdir[j] = newdir[j].replace(changes_from, changes_to)

        elif command == "2":
            print("Какъв текст да добавя в началото на имената? ", end="")
            changes_from = input()
            changes_to = "null"

            for j in range(len(newdir)):
                newdir[j] = changes_from + newdir[j]

        elif command == "3":
            print("Какъв текст да добавя в края на имената? ", end="")
            changes_from = input()
            changes_to = "null"

            for j in range(len(newdir)):
                newdir[j] = newdir[j] + changes_from

        print("Добре! ", end="")
        while True:
            # след като се извърши преименуването, те пита да прилагаш ли промените, да видиш промените или да добавиш още промени
            # всичко това е в цикъл ^ само за да може ако напишеш невалиден input да опиташ отново
            print("Сега?\n1) визуализирай промените до сега\n2) добави следващо действие\n3) готово! приложи промените и излез\nИзбери: ",end="")
            subcommand = input()
            if subcommand != "1" and subcommand != "2" and subcommand != "3":
                print("Няма такава опция!")
                continue
            if subcommand == "1":
                # визуализацията е много проста - просто принтира всеки елемент от двата списъка, разделени със стрелки
                for j in range(len(directory)):
                    print(f"{directory[j]}  -->  {newdir[j]}")
            elif subcommand == "2":
                # ако искаш следващо действие, излез от този цикъл, което ще завърти нова итерация на основния цикъл
                break
            elif subcommand == "3":
                # самото преименуване - за всеки файл в списъка...
                for j in range(len(directory)):
                # ...try except изпълнява кода под try и ако излезе грешка изпълнява кода под except
                    try:
                        os.rename(directory[j], newdir[j])
                    except:
                        print(f"Грешка! Не можах да преименувам файлът {directory[j]}\nВероятно е недостъпен, използва се от друга програма в момента, или вече не съществува!")
                        print("Натисни Enter, за да излезеш от програмата...")
                        #изчаква за enter и излиза от програмата
                        input()
                        sys.exit()
                    #ако няма грешка и файлът е преименуван, изпиши го и давай следващата итерация (пробвай следващия файл и така нататък)
                    print(f"Преименуван файл {j+1} от {len(directory)}!")
                #след като преименуването е успешно, изчаква за enter и излиза от програмата
                print("Натисни Enter, за да излезеш от програмата...")
                input()
                sys.exit()
