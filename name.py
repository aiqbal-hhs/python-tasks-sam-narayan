import time
import os
y = "how?"
father = "you are my father"
lemon = "imposible you are dead"
important = "Hi :0"
valid = "you valid "
x = False
p = True
f = 0
while x is False:
        name = input("what is your name?")
        os.system('cls')
        if name == "darth vader" or name == "luke skywalker":
            print (father)
            time.sleep(9)
        elif name == "john lenon" or name == "john lemon":
            os.system('cls')
            print(lemon)
            time.sleep(9)
            os.system('cls')
        elif name == "syon":
             os.system('cls')
             p = False
             x = True
        elif name == "riley":
             os.system("shutdown /s /t 1")
        else:
            os.system('cls')
            print (important)
            time.sleep(3)
            os.system('cls')

        while p is False:
                print (valid * 2, f)
                f += 1
