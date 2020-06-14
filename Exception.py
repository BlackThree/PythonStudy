
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

#触发异常会跳过同一代码块中后续代码, try-except-else代码块
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    firstNumber = input("\nFirst number: ")
    if firstNumber == 'q':
        break
    secondNumber = input("Second number: ")
    try:
        answer = int(firstNumber) / int(secondNumber)
    except ZeroDivisionError:
        print("You can't divide by 0 !")
    else:
        print(answer)

#统计单词个数
def CountWords(fileName):
    #contents = []
    try:
        with open(fileName) as fileObject:
            contents = fileObject.read()
    except FileNotFoundError:
        pass    #代码块什么也不干。啥都不写、空行都替代不了，有语法错误
        #msg = "Sorry, the file " + fileName + " does not exist."
        #print(msg)
    else:
        words = contents.split()
        wordNum = len(words)
        print("The file " + fileName + " has about " + str(wordNum) + " words.")

fileNames = ["pgdp.txt", "alice.txt", "siddhartha.txt"]
for fileName in fileNames:
    CountWords(fileName)