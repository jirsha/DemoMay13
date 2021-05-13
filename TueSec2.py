import os
os.system('cls');

def GetMessageInfo():
    first = input("What is your first name?  ")
    last = input(first + "'s last name is: ")
    greeting = "Greetings " + first + " " + last + "!"
    return greeting;

#myGreeting = GetMessageInfo()
#print(myGreeting)

print(GetMessageInfo())

#print(greeting)   #private to function

first = input("What is your first name outside of function?  ")
last = input(first + "'s last name is outside of function: ")

if len(first) < 5:
    print("The name " + first + " has a length of " + str(len(first)))
    username = first.ljust(5, '*')
    print(username)
elif len(first) >= 10:
    print("The 10th character is " + first[9])
    print("The new name is " + first[2 : 10])
elif len(first) == 6:
    print(first.upper().ljust(9, 'a').rjust(12, '$'))
else:
    print("The name of " + first + " " + last + " is perfect already")

#print(username)

friends = []

for x in range(0, 5):
    myFriend = input("Name of friend number " + str(x) + "?  ")
    friends.append(myFriend)

for fr in friends:
    print("My friend is " + fr)

fileOfFriends = input("\nName of file that will hold friends:  ")

with open(fileOfFriends, "w") as myFile:  #create object named myFile - file open for write
    myFile.write("Here is my list of friends:\n")
    for f in friends:
        myFile.write(f)
        myFile.write("\n")

input("Press Enter to Read " + fileOfFriends)

with open(fileOfFriends, "r+") as myFile:  #create object named myFile - file open for read
    print(myFile.read())

