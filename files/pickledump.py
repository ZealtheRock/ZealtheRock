import pickle,student

f = open("student.dat","wb")
s = student.Student(112,"John",90)
pickle.dump(s,f)
f.close()

