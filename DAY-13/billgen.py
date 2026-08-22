'''
data = {
    'ps':800,
    'bat':50,
    'shirt':100,
    'chocolate':10,
    'facewash':30,
    'maggie':20,
    'bedsheet':200,
    'light':80,
    'fan':300,
    'ice cream':500,
}

for i in data:
    print(i.ljust(20),data[i])

prods =  input("Enter the products: ").split()
total = 0
for i in prods:
    if i in data:
        print(p, ":", data[i])
        total = total + data[i]

print("Total Bill : ", total)


s = 'python programming'
d = {}
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)
'''
s = 'aaabbbbccccdddddeeee'
c=1
res = ''
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        c+=1
    else:
        res+= s[i]+str(c)
        c=1
print(res+s[i]+str(c))