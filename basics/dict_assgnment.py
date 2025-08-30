student_info={"name":"john","age":18,"major":"CS"}
print(student_info)
print(student_info.get("name"))
print(student_info.get("age"))
student_info.update({"email":"john@demo.com"})
print(student_info)
#---update age to 25
student_info.update({"age":25})
print(student_info)
#---Remove the key 'major'
student_info.pop("major")
print(student_info)