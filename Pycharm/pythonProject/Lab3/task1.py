import random
class LIBRARY:
    # ==============================================================================
    # Constructor
    # ==============================================================================
    def __init__(self):
        print("Library Managment System")
        self.stdName  = None
        self.rollNo   = None
    # ==============================================================================
    # HardCoding the Books in Library
    # ==============================================================================
    Genre = ("reading books", "business", "designers", "machine learning", "coding")
    readingBooks = ("Rich_Dad_Poor_Dad", "Atomic_Habits", "Learn_to_grow")
    business = ("Good_to_greet", "zero_to_one", "The_4_Hour_week")
    designers = ("logo_Design_love", "know_your_onions")
    machineLearning = ("python_AI_learning", "machine_learning", "data_mining")
    Coding = ("Clean_Code", "Design_Patterns", "Crack_to_Code")
    # ==============================================================================
    # Getter Functions
    # ==============================================================================

    def getName(self):
        return self.stdName

    def getRollNo(self):
        return self.rollNo
    # ==============================================================================
    # Setter Functions
    # ==============================================================================

    def setName(self, name_):
        self.stdName = name_

    def setRollNo(self, rollName_):
        self.rollName = rollName_
    # ==============================================================================
    # Date Function
    # ==============================================================================

    def Date_(self):
        return print(random.randint(1,30), "-", random.randint(3,12), "- 2022")
    # ==============================================================================
    # Selecting Categories to get the relevant book
    # ==============================================================================

    def Category(self):
        print("Categories of Books")
        for i in range(len(self.Genre)):
            print((i+1)," => ", self.Genre[i])
        select = int(input("Select Book : "))
        self.selectBook(select)
        return
    # ==============================================================================
    # Add member into the Dictionary
    # ==============================================================================

    def addMember (self, Dictionary, Name_, RollNo_):
        Dictionary[Name_] = RollNo_
        self.Category()
        return
    # ==============================================================================
    # function to check if the member is present in the list and then greet him/her
    # ==============================================================================

    def CheckAndGreet (self, BookDictionary, Name_, RollNo_):
        for keys, values in BookDictionary.items():
            if values == RollNo_:
                print("Hi", Name_)
                self.Category()
                return
            # if not present already just put it inside the dictionary
            else:
                self.addMember(BookDictionary, Name_, RollNo_)
    # ==============================================================================
    # function to print the books after selection of particular genre
    # ==============================================================================

    def printBooks(self,typeofGenre):
        print("Books ",typeofGenre)
        for i in range(len(typeofGenre)):
            print((i + 1), ")", typeofGenre[i])
    # ==============================================================================
    # select the copy of book
    # ==============================================================================

    def selectBookCopy(self,options,typeofGenre):
        for i in range(len(typeofGenre)):
            if i == options:
                print("Selected => ",typeofGenre[i])
                print("Issuance till ", self.Date_())
    # ==============================================================================
    # Menu for the selection of the books
    # ==============================================================================

    def selectBook(self, choice):
        if choice == 1:
            self.printBooks(self.readingBooks)
            choice_ = int(input("==Select the Book =="))
            self.selectBookCopy(choice_, self.readingBooks)

        elif choice == 2:
            self.printBooks(self.business)
            choice_ = int(input("==Select the Book =="))
            self.selectBookCopy(choice_,self.business)

        elif choice == 3:
            self.printBooks(self.designers)
            choice_ = int(input("==Select the Book =="))
            self.selectBookCopy(choice_,self.designers)

        elif choice == 4:
            self.printBooks(self.machineLearning)
            choice_ = int(input("==Select the Book =="))
            self.selectBookCopy(choice_,self.machineLearning)

        elif choice == 5:
            self.printBooks(self.Coding)
            choice_ = int(input("==Select the Book =="))
            self.selectBookCopy(choice_,self.Coding)

        else:
            print("invalid input")

# ==============================================================================
# Library Members
# ==============================================================================
Dictionary = {
        "Harry": "20F0199",
        "Kante": "21f0291",
        "David": "22f0382",
        "Weise": "24f0473",
        "Alexa": "24f0564"
    }
objLib = LIBRARY()
Name_ = input("Input your name : ")
objLib.setName(Name_)
RollNo_ = input("Input your Roll No: ")
objLib.setRollNo(RollNo_)
objLib.CheckAndGreet(Dictionary, objLib.getName(), objLib.getRollNo())