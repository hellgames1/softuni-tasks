import os, sys

directory = os.listdir()
directory.remove(os.path.basename(__file__))
newdir = os.listdir()
newdir.remove(os.path.basename(__file__))
i = 0


print("Welcome to Batch Rename Script.\nChoose what actions to take:")

while True:
    i+=1
    print(f"Action Number {i}: \n1) replace text with other text\n2) insert text at beginning\n3) insert text at end\nChoose: ", end="")
    command = input()
    if command != "1" and command != "2" and command != "3":
        i-=1
        print("No such option!")
        continue
    else:
        if command == "1":
            print("What text to replace? ", end="")
            changes_from = input()
            print("Replace with what? ", end="")
            changes_to = input()
            for j in range(len(newdir)):
                newdir[j] = newdir[j].replace(changes_from, changes_to)
        elif command == "2":
            print("What text to insert at beginning? ", end="")
            changes_from = input()
            changes_to = "null"
            for j in range(len(newdir)):
                newdir[j] = changes_from + newdir[j]
        elif command == "3":
            print("What text to insert at end? ", end="")
            changes_from = input()
            changes_to = "null"
            for j in range(len(newdir)):
                newdir[j] = newdir[j] + changes_from
        print("Okay! ", end="")
        while True:
            print("Now?\n1) visualize the changes\n2) add next action\n3) done! apply changes and exit\nChoose: ",end="")
            subcommand = input()
            if subcommand != "1" and subcommand != "2" and subcommand != "3":
                print("No such option!")
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
                        print(f"Error! Couldn't rename the file {directory[j]}\nIt might be inaccessible, in use by another program, or doesn't exist anymore!")
                        print("Press Enter to exit...")
                        input()
                        sys.exit()
                    print(f"Renamed file {j+1} of {len(directory)}!")
                print("Press Enter to exit...")
                input()
                sys.exit()
