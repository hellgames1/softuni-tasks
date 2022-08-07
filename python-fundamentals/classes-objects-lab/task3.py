""""
Task 3 - Email
"""
class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False
    def send(self):
        self.is_sent = True
    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"
emails = []
while True:
    command = input()
    if command == "Stop":
        break
    com = command.split()
    emails.append(Email(*com))
com = list(map(int,input().split(", ")))
for num in com:
    emails[num].send()
for email in emails:
    print(email.get_info())