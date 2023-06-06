class Student:
    def __init__ (self,firstName, lastName,age,cnic,course,gender,CGPA,SGPA,cred_hour):
        self.firstName = firstName
        self.lastName = lastName
        self.age=age
        self.cnic=cnic
        self.course = course
        self.gender = gender
        self.CGPA = CGPA
        self.SGPA = SGPA
        self.cred_hour = cred_hour

    def set_firstName(self,name):
        self.firstName = name
    def set_lastName(self,name):
        print("ast Name :- ",name)
        self.lastName=name
    def set_age(self,age):
        self.age=age
    def set_cnic(self,cnic):
        self.cnic=cnic
    def set_course(self,course):
        self.course=course
    def set_gender(self,gender):
        self.gender=gender
    def set_CGPA(self,cgpa):
        self.CGPA=cgpa
    def set_SGPA(self,sgpa):
        self.SGPA = sgpa
    def set_cred_hour(self,cred):
        self.cred_hour=cred
    #GETTER FUNCTIONS
    def get_firstName(self):
        return self.firstName
    def get_lastName(self):
        return self.lastName
    def get_age(self):
        return self.age
    def get_cnic(self):
        return self.cnic
    def get_course(self):
        return self.course
    def get_gender(self):
        return self.gender
    def get_CGPA(self):
        return self.CGPA
    def get_SGPA(self):
        return self.SGPA
    def get_cred_hour(self):
        return self.cred_hour

    def SetStudent(obj,firstName,lastName,age,cnic,course,gender,CGPA,SGPA,cred_hour ):
        obj.set_firstName(firstName)
        obj.set_lastName(lastName)
        obj.set_age(age)
        obj.set_cnic(cnic)
        obj.set_course(course)
        obj.set_gender(gender)
        obj.set_CGPA(CGPA)
        obj.set_SGPA(SGPA)
        obj.set_cred_hour(cred_hour)

def FetchStudent(obj):
     print ("First Name :- ",obj.get_firstName()," Last Name :- ",obj.get_lastName(),
            " AGE :- ",obj.get_age()," CNIC :- ",obj.get_cnic()," Course :- ",obj.get_course()," Gender :- ",obj.get_gender(),
            " CGPA :- ",obj.get_SGPA()," Credit Hour :- ",obj.get_cred_hour())

List=[]
List.append(Student("Zain", "Ahsan", 22, "123421", list, "Male", 4, 4, 100))
List.append(Student("Jahanzaib","Ahsan",18,"234234234234",list,"Male",4,4,100))
List.append(Student("Fahad","Ahsan",12,"234234234234",list,"Male",4,4,100))

print ("***List***")

for obj in List:
    FetchStudent(obj)

print(dict)