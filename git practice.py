#Simple french greeter
name=input("What is your name?")
state=input("Are you staying or leaving?").lower()
if state=='staying':
    print("Bonjour,", name, "!")
else:
    print("Au revoir,", name, '!')
