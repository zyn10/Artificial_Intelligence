#Library Managment System
class Library:
    Dictionary={
        'messi':"Book of Economics",
        'lana':   "why nation fails",
        'tera': "Chadda the Bussinessman",
        'Shere': "Rich Dad Poor Dad",
        'zizo':  "Atomic Habits"

    }
    def __init__(self):
        print("Library Managment System")
        self.stdName  = None
        self.rollNo   = None
        self.bookName = None


# getter Functions

    def getName(self):
        return self.stdName
    def getRollNo(self):
        return self.rollNo
    def getBookName(self):
        return self.bookName

# Setter Functions
    def setName(self, name_):
        self.stdName = name_

    def setRollNo(self, rollName_):
        self.rollName = rollName_

    def setBookName(self, book_):
        self.bookName = book_
#greet
    def greet(self):
        print("Hi ",self.getName())


#allocate Book
    def allocateBook(self):
        n_temp=self.getName()
        r_temp=self.getRollNo()
        b_temp=self.bookName

        self.Dictionary.append(n_temp,r_temp,b_temp)