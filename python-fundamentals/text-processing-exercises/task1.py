""""
Task 1 - Valid Usernames
"""
usernames = input().split(", ")
for username in usernames:
    if 3<=len(username)<=16:
        if username.replace("_","").replace("-","").isalnum():
            if not " " in username:
                print(username)