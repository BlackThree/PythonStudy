import json

numbers = [2, 3, 5, 7, 11, 13];
#保存数据到json文件
fileName = "number.json";
with open(fileName, 'w') as f_obj:
    json.dump(numbers, f_obj);

#从json文件读取数据
with open(fileName) as f_obj:
    print(json.load(f_obj));

#保存用户的输入
userName= input("What is your name?");
fileName = "UserName.json"
with open(fileName, 'w') as f_obj:
    json.dump(userName, f_obj);
    print("We'll remember you when you come back, " + userName + "!");

#读取用户输入
with open(fileName) as f_obj:
    userName = json.load(f_obj);
    print("Welcome back, " + userName + "!");

#重构以上的保存和读取操作
def GetStoredUserName():
    fileName = "UserName.json"
    try:
        with open(fileName) as fileObj:
            userName = json.load(fileObj)
    except FileNotFoundError:
        return None;
    else:
        return userName;

def GetNewUserName():
    userName = input("What is your name?")
    fileName = "UserName.json"
    with open(fileName, 'w') as fileObj:
        json.load(userName, fileObj)
    return userName

def GreetUser():
    userName = GetStoredUserName()
    if userName:
         print("Welcome back, " + userName + "!");
    else:
        userName = GetNewUserName()
        print("We'll remember you when you come back, " + userName + "!");

GreetUser()
