import re

string = "One to One Idea can change you life, small steps can cover long journey with consistency,at time 1-2-2021"
result_findall = re.findall(r'[A-Z][a-z]+',string)
print(result_findall)


result_search = re.search(r'O\w{2}', string)
print(result_search)


result_match = re.match(r'j\w{2}', string)
print(result_match)


result_sub = re.sub(r'One','steps', string)
print(result_sub)

result_sub = re.findall(r'\d{1,2}-\d{1,2}-\d{4}', string)
print(result_sub)


