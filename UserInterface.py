import sys

class UI:
    __functionList = []
    def UserInterface(self):
        try:
            inp = int(input(f"What task do you want to check?\n[1 to {len(self.__functionList)}]: Choose the task you want\n[e]: Exit\n"))
            if inp == "e":
                sys.exit()
            self.__ChooseTask(inp)
            self.__Continue(inp)
        except ValueError:
            print("This is not a number!")
            self.UserInterface()
        except IndexError:
            print(f"\nThere are only {len(self.__functionList)} tasks to choose from!\n")
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
        self.__Continue(taskNum)


    def __ChooseTask(self, taskNum):
        try:
            result = self.__functionList[taskNum-1]()
            if result != None: print(result)
        except TypeError:
            inp = str(input('Write something: '))
            result = self.__functionList[taskNum-1](inp)
            if result != None: print(result)
        
        

    
    def __init__(self, functionList) -> None:
        self.__functionList = functionList
        