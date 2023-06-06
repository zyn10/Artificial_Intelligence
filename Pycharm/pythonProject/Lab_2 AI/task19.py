#stack and queue
class Stack:
    Counter = 0
    StackList = []
    def Insertion ( self , input ) :
       self.StackList.insert(0,input)
       self.Counter+=1
    def Deletion(self):
        self.StackList.pop(0)
        self.Counter-=1
    def isEmpty(self):
        if self.Counter==0:
            print("Stack Empty hay....")
    def top(self):
        if self.Counter != 0:
            return self.StackList[0]
        else:
            print("Stack Empty hay....")
    def printFun(self):
        print(self.StackList)



class Queue:
    Counter = 0
    QueueList = []
    def Insertion ( self , input ) :
       self.QueueList.append(input)
       self.Counter+=1
    def Deletion(self):
        self.QueueList.pop(0)
        self.Counter -= 1
    def isEmpty(self):
        if self.Counter == 0:
            print("Queue Empty hay....")
    def top(self):
        if self.Counter != 0:
            return self.QueueList[0]
        else:
            print("Queue Empty hay....")
    def printFun(self):
        print(self.QueueList)

print ( " Testing Stack Class" )
obj_S = Stack()
obj_S.isEmpty()
obj_S.top()
obj_S.Insertion(2)
obj_S.Insertion(3)
obj_S.Insertion(4)
obj_S.Insertion(5)
obj_S.Insertion(6)
print("After insertion.....\n")
obj_S.printFun()
obj_S.Deletion()
print("After Deletion........\n")
obj_S.printFun()


print ( " Testing Queue Class" )
obj_Q = Queue()
obj_Q.isEmpty()
obj_Q.top()
obj_Q.Insertion(2)
obj_Q.Insertion(3)
obj_Q.Insertion(4)
obj_Q.Insertion(5)
obj_Q.Insertion(6)
print("After insertion.....\n")
obj_Q.printFun()
obj_Q.Deletion()
print("After Deletion........\n")
obj_Q.printFun()
