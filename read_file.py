file = open("example.txt", "r")  # 'r' is read mode example.txt is changed for path to file in question
content = file.read()
print(content)
file.close()
