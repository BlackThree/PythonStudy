#name = input("Please enter your name:")
#print("Hello," + name + "!")

##条件不满足退出循环
#height = 0
#while height != 100:
#    height = input("How tall are you, in inches?")
#    height = int(height)

#    if height >= 36:
#        print("\nYou're tall enough to ride!")
#    else:
#        print("\nYou'll be able to ride when you're a little older.")

#break退出循环
promt = "How tall are you, in inches? "
promt += "\n（Enter 'q' to end the program.）"
while True:
    height = input(promt)

    if height == 'q':
        break;
    else:
        height = int(height)

        if height >= 36:
            print("\nYou're tall enough to ride!")
        else:
            print("\nYou'll be able to ride when you're a little older.")

#while遍历列表
unconfirmed_users = ["alice", 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    user = unconfirmed_users.pop()

    print("Verifying user: " + user.title())
    confirmed_users.append(user)

print("\nThe following users have been confirmed:")
for user in confirmed_users:
    print(user.title())

#删除列表所有相同字符串
pets = ["dog", "cat", "dog", "goldfish", "cat", 'rabbit', "cat"]
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)
