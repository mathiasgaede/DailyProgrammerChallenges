
name = input("What is your name?")
age = input("How old are you?")
username = input("What is your username?")

f = open("info.txt","w+")

print("Your name is " + name + ", you are " + age + " years old, and your username is " + username)

f.write("Name: %s\n" % name)
f.write("Age: %s\n" % age)
f.write("Username: %s\n" % username)
f.close()