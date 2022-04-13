

a = [1,2,3,4,6,7]
print(a)
print(type(a))

b = [1,2,3,[4,5,6],7]

print(b[1])
print(b[3])
recur = b[3]

print(b[3][0])

b.append(7)
print(b)
b.insert(4,'a')
print(b)

print(b.pop())
print(b)


def addC(x) :
  return str(x)+"C"

c = list(map(addC, a))

print(c)

d = {1:2, 2:3, 3:1}

print(d)

print(d[1]) 

print(d.get(4, 0))

d.update({3:"삼삼"})

print(d)

