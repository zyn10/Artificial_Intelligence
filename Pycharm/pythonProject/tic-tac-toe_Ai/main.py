#MinMax Algorithm

class MinMax_:

    def MaxFunction(self,Max_Array):
        print("===============================")
        length_=int(len(Max_Array)/2)
        Length1 = len(Max_Array)
        if (Length1 == 1):
            print("Required Values => ", Max_Array)
            quit()

        jump=0
        dummy=[]

        for i in range(jump,length_):
            if(Max_Array[jump]>Max_Array[jump+1]):
                dummy.append(Max_Array[jump])
            elif(Max_Array[jump]<Max_Array[jump+1]):
                dummy.append(Max_Array[jump+1])
            jump=jump+2
        print("MAX Values => ", dummy)
        self.MinFunction(dummy)

    def MinFunction(self,Min_Array):
        print("===============================")
        length_=int(len(Min_Array)/2)
        Length1=len(Min_Array)
        if(Length1==1):
            print("Required Values => ",Min_Array)
            quit()

        jump=0
        dummy2 = []
        for i in range(jump,length_):
            if(Min_Array[jump]<Min_Array[jump+1]):
                dummy2.append(Min_Array[jump])
            elif(Min_Array[jump]>Min_Array[jump+1]):
                dummy2.append(Min_Array[jump+1])
            jump=jump+2
        print("MIN Values => ",dummy2)
        self.MaxFunction(dummy2)

print("\t***Min-Max Algorithm***")
Given=[4,6,2,10,14,6,21,22]
obj=MinMax_()
obj.MaxFunction(Given)