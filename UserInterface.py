import sys

class UI:
    __functionList = []
    def UserInterface(self):
        try:
            inp = int(input("What task do you want to check?\n[<task number>]: Choose the task you want\n[0]: Exit\n"))
            if inp == 0:
                sys.exit()
            if inp > len(self.__functionList) or inp < 1:
                print(f"\nThere are only {len(self.__functionList)} tasks to choose from!\n")
                self.UserInterface()
            self.__ChooseTask(inp)
            self.__Continue(inp)
        except ValueError:
            print("This is not a number!")
            self.UserInterface()

    def __Continue(self, taskNum):
        message = str(input("Continue?\n[t]: Choose another task\n[e]: exit\n[a]: same task\n"))
        match message:
            case "t":
                self.UserInterface()
            case "e":
                sys.exit()
            case "a":
                self.__ChooseTask(taskNum)
                self.__Continue(taskNum)
        print("This message means nothing to me!")
        self.__Continue()


    def __ChooseTask(self, taskNum):
        self.__functionList[taskNum-1]()
        

    
    def __init__(self, functionList) -> None:
        self.__functionList = functionList
        