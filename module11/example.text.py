# file_path = "example.text"
#
# file = open(file_path, 'r')
#
#
#
# content = file.read()
# print(content)

# with open(file_path, 'w') as file:
#     content = file.read()
#     print(content)


# 'r' read only mode
# 'w' write
# 'a' apennd
# 'b' binary mode
# 'x' exclusive creation

# with open("example.txt") as file:
#     line1 = file.readlines()
#     print(line1)

# with open(file_path,  "w") as file:
#     file.write("Hello World")
#
# lines = ['Hello World\n]' , 'Welcome to python\n']
# with open(file_path, 'w') as file:
#     file.writelines(lines)

#
# with open(file_path, 'a') as file:
#     file.write('New data appended')
#

# data = b"this is some binary data"
# with open("example.text", "wb") as file:
#     file.write(data)
#
# with open("example.text", "rb") as file:
#      data = file.read()

# with open(file_path) as cl:
#     for line in cl:
#         clean_line = line.strip()
#         print(clean_line)
#
# with open("example.text") as w:
#     for line in w:
#         words = line.strip().split()
#          print(words)

#name = "Rubik"
#age = 30

#with open('example.text',"w") as file:
    #file.write("Name"+ name + "\nAge"+ str(age))

#with open("example.text"."w") as file:
    #file.write(f"Name: {name}\n"})
   # file.write(f"Age: {age}\n"})