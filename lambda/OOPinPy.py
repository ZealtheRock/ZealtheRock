class Student():
     def __init__(self):
        self.__name = "Harsh"
        self.__age = 35

     def display(self):
         print(self.__name)
         print(self.__age)

s = Student()
#s.display()
#----Name mangling
print(s._Student__name)    #--> Name magling