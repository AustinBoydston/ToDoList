# To Do list program
# Author: Austin Boydston
# Solution for To Do List assignment for Advanced Programming

import os




class TDlist:
    def __init__(self, list, linecount, filename):
        self.list = list
        self.linecount = linecount
        self.filename = filename
    

    # read the text file into the list array
    def readFile(self):
        self.clearList()
        file = open(self.filename, "r")
        line = file.readline()
        while line != "":
            self.list.append(line)
            line = file.readline()

    def display(self):
        for i in range(len(self.list)):
            print(  str(i + 1) + ". " + self.list[i])

    def clearList(self):
        self.list = []

    def addItem(self, number, line):
        #add newline character
        line = line + "\n"
        try:
            self.list.insert(number - 1, line)
        except IndexError:
            self.list.append(line)
        self.updateFile()


    def removeItem(self, number):
        try:
            del self.list[number - 1]
        except IndexError:
            del self.list[-1]
        finally:
            pass
        self.updateFile()


    def updateFile(self):
        #clear out the file
        open(self.filename, "w").close()
        #open again for writing
        file = open(self.filename, "w")
        #write all contents to the file
        for i in range(len(self.list)):
            file.write(self.list[i])
        file.close()
        


def PromptUser():    
    print("What would you like to do?")
    print("1: print the list.")
    print("2: add items to the list.")
    print("3: remove an item from the list.")
    print("4: clear the list.")
    print("5: Exit")
    
def getInput():
    PromptUser()
    UserInput = input()
    while UserInput != "1" and UserInput != "2" and UserInput != "3" and UserInput != "4" and UserInput != "5":
        print("=======================================")
        print("ERROR: Enter a number from 1 to 5 only.")
        print("=======================================")

        PromptUser()
        UserInput = input()
    return int(UserInput)
    

def getInputNumber(prompt):
    print(prompt)
    UserInputNumber = -1
    while True:
        UserInput = input()
        if UserInput == "":
            return UserInputNumber
        try:
            UserInputNumber = int(UserInput)
        except ValueError:
            print("ERROR: enter a number only...")
            print(prompt)
        else:
            break
    return UserInputNumber


def addToDoItems(ToDo_obj):
    position = -1
    while True:
        UserInputString = input("Type the item to add out and press enter. Type 'stop' to stop adding\n")
        if UserInputString == "stop":
            return -1
        position = getInputNumber("what position should this item be added to? Default is the end.")
        
        ToDo_obj.addItem(position, UserInputString)

def removeToDoItems(ToDo_obj):
    position = -1
    while True:
        position = getInputNumber("what list item should be removed? Default is the last item.")
        UserInputString = input("Type stop to cancel removing, or press ender to continue\n")
        if UserInputString == "stop":
            return -1
        ToDo_obj.removeItem(position)

def clearConsole():
    os.system('cls')


def main():
    ToDoList = TDlist([], 0, "ToDoList.txt")

    InputNumber = getInput()
    while(InputNumber != 5):
        ToDoList.readFile()
        match InputNumber:
            case 1: 
                clearConsole()
                ToDoList.display()
            case 2:
                clearConsole()
                addToDoItems(ToDoList)
            case 3:
                clearConsole()
                removeToDoItems(ToDoList)
            case 4:
                clearConsole()
                ToDoList.clearList()
                ToDoList.updateFile()
            case _:
                print("ERROR: INVALID OPTION CHOSEN. EXITING")
                exit()
        InputNumber = getInput()


main()


