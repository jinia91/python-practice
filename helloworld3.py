a = 1

if a==1 :
  print(a)
elif a != 1 :
  print("떙")


temp = range(0,15)
print(temp)
print(list(temp))

for i in range(1,11):
  print(i)
  
  
for i in range(1,11,5):
  print(i)


for index , i in enumerate(range(1,11,5), start = 1):
  print(index, i, sep="번째는 ")
