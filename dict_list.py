import Function
Function.makePizza('sugar', 'flour')    #函数调用

alien_0 = {'color': 'green', 'points': 5}

print(alien_0['points'])

alien_0['x_pos'] = 25
print(alien_0)

#del alien_0['color']
#print(alien_0)

#遍历字典
for k, v in alien_0.items():
    print('key: ' + k)
    print('value: ' + str(v))
    print('\n')

#遍历键值
for k in alien_0.keys():    #返回键值列表
    print(k)

print(alien_0.values())

#列表中嵌套字典
aliens = []
for alien_num in range(3):
    aliens.append(alien_0)
print(aliens)

#字典中嵌套列表
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }
print(pizza)