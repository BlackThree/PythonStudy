for value in range(1,5):
    print(value)

numbers = list(range(1,6))
print(numbers)

for value in range(1,22,2):
    numbers.append(value ** 2)
print(numbers)

#列表解析
squares = [value ** 2 for value in range(1,11)]
print(squares)
print(squares[0:3])
print(squares[:3])  #从头开始
print(squares[3:])  #到尾终止
print(squares[-3:]) #末尾元素获取

#复制列表
squaresCopy = squares[:]
print(squaresCopy)

#关联到同一列表
squaresCopy2 = squares  
print(squaresCopy2)
squares.append("关联")
print(squaresCopy2)
