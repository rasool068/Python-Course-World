'''
#str list tuple set dict range
for var in seq:
    #stmts
-------------------------------

s = 'python programming'
for i in s:
    print (i)

l = [1,2,3,4,5,6]
for num in l:
    print (num)

prices = (2323,423,423,43423)
for price in prices:
     print (price)

#range (start,end+1,step):(0,1)

for i in range (1,11):
    print (i)

for i in range (2,21,2):
    print (i)

for i in range (1,21,2):
    print (i)

for i in range (5,101,5):
    print (i)

for i in range (6,121,9):
    print (i)

s = 'code gnan 8th anniversary'
for i in range(len(s)):
    print(i,s[i])

s = (321,323,323,34234)
for i in range(len(s)):
    print(i,s[i])

s = [1232,9089,434,545]
for i in enumerate(s):
    print(i[0],i[1])

d = {1:2,2:4,3:6,4:8,5:10}
for i in enumerate(d):
    print(i[0],i[1],d[i[1]])

for i in range (1,11):
    if i == 5:
        break
    print (i)

for i in range (1,11):
    if i == 5:
        continue
    print (i)

for i in range(1,11):
    if i==15:
    print)i)
else:
print("End of the loop")

l = [12,13,14,15,16,18,20]
n=26
for i in l:
    if i == n:
        print(n,"Found")
        break
else:
    print(n,"Not found")

pin = 1234
for i in range(5):
    epin = int(input("Enter the pin: "))
    if epin == pin:
        print("Unlock the phone")
        break
    else:
        print("Invalid Pin")
else:
    print("try after 30 seconds")

n = 19
for i in range(2,n//2+1):
    if n%i==0:
        print("not a prime number")
        break
else:
    print("prime number")
'''
