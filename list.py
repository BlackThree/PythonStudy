bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[-1])

bicycles.append('supent')
print(bicycles)

bicycles.insert(0, 'A')
print(bicycles)

del bicycles[0]
print(bicycles)

bicycles.pop()
print(bicycles)

print(bicycles.pop(0))
print(bicycles)

print(bicycles.remove('redline'))
print(bicycles)

print('\n')

guests = ['Tom','Tony','Mary']
print(guests)

print(guests[1]+'无法赴约')
guests[1] = 'James'
print(guests)

print('我订到了一张更大的餐桌')
guests.insert(0, '李白')
guests.insert(2, '杜甫')
guests.append('白居易')
print(guests)

print("Sorry, the big table can't arrive in time!")
print('Sorry, ' + guests.pop())
print('Sorry, ' + guests.pop())
print('Sorry, ' + guests.pop())
print('Sorry, ' + guests.pop())

print(guests)
print(guests[0] + ', you are welcome!')
print(guests[1] + ', you are welcome!')
del guests[0]
del guests[0]   # not [1]
print(guests)

names = ['李白', 'Tom', 'Tony', '杜甫']
names.sort()
print(names)
names.sort(reverse = True)
print(names)

print(sorted(names))
print(names)
print(sorted(names, reverse=True))

names.reverse()
print(names)

