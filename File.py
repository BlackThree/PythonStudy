with open("PIDigits.txt") as fileObject:
    contents = fileObject.read()
    print(contents)
    #print(contents.rstrip())   #read()会返回空白行。但实际并没有

#逐行读取
with open("PIDigits.txt") as fileObject:
    for line in fileObject:
        print(line.rstrip())

#将文件内容存储在列表中
lines = []

with open("PIDigits.txt") as fileObject:
    lines = fileObject.readlines()

for line in lines:
    print(line.rstrip())

#清除所有空白字符
piString = ""
for line in lines:
    piString += line.strip()

print(piString)
print(len(piString))

#查找字符串中是否存在特定字符
contents = []
with open("PiThousandDigits.txt") as fileObject:
    contents = fileObject.readlines()

piString = ""
for str in contents:
    piString += str.strip()

#while(True):
birthday = input("Please enter your birthday, in the form mmddyy: ")
if birthday in piString:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi!")

#创建文件并写入
fileName = "Programming.txt"
# "r"读取模式，"w"写入模式，"a"附加模式, "r+"读写模式
with open("Programming.txt", "w") as fileObject:
    fileObject.write("I Love programming.")

