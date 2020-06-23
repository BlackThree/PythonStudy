
def DescribePet(animalType, petName):
    """显示宠物的信息"""
    print("\nI have a " + animalType + ".")
    print("My " + animalType + "'s name is " + petName.title() + ".")

DescribePet('hamster', 'harry') #不支持放在函数定义前
DescribePet(animalType = 'dog', petName = 'tingting')

def GetPet(animalType, petName):
    retParam = "\nI have a " + animalType + "."\
                + "\nMy " + animalType + "'s name is " + petName.title() + "."
    return retParam
print(GetPet("cat", "XiaoHuang"))

#任意数量实参
def makePizza(*toppings):   #空元组
    print(toppings)

makePizza('pep')
makePizza('mushrooms', 'green pepers')

#任意数量关键字实参
def buildProfile(first, last, **userInfo):
    profile = {}
    profile['firstName'] = first
    profile['lastName'] = last
    for k, v in userInfo.items():
        profile[k] = v
    return profile

userProfile = buildProfile('zhang', 'supent',
                           location = 'zhang',  # key = value
                           field = 'yanchao')
print(userProfile)

def GetFormattedName(first, last=''):
    fullName = first + ' ' + last
    return fullName.title()
