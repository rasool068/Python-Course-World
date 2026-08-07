Python 3.14.6 (v3.14.6:c63aec69bd5, Jun 10 2026, 08:07:54) [Clang 21.0.0 (clang-2100.1.1.101)] on darwin
Enter "help" below or click "Help" above for more information.



a=10
b=5
a+b
15
a-b
5
a*b
50
a/b
2.0
a/2
5.0
9/2
4.5
9//2
4
comparison operators
SyntaxError: invalid syntax
a=10
a
10
b=5
b
5
a<b
False
a>b
True
a<=b
False
a>=b
True
a>=10
True
a==10
True
a==b
False
a!=b
True
a=20
a=a+10
a
30
a=a+20
a
50
a-=10
a
40
a*=20
a
800
a//=10
a
80
a**=20
a
115292150460684697600000000000000000000
a/=1000
a
1.152921504606847e+35
a=10
a
10
#logical operators
email=True
password=False
email and password
False
login = True
login = False
display_products = True
login or display_products
True
's' in 'aeiou'
False
's' not in 'aeiou'
True
7%2==0
False
7%2==0 and 2%3==0
False
6%2 or 2%3
2
6%2==0 or 2%3==0
True
9%2 not
SyntaxError: invalid syntax
not 9%2==0
True
#str list tuple dic set
s= 'python programming'
'python' in s
True
'java' in s
False
'z' in s
False
'c++' in s
False
>>> l=[1,2,3,4]
>>> '3' in l
False
>>> 3 in l
True
>>> 9 is not in l
SyntaxError: invalid syntax
>>> t={20,30,40,50)
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
>>> t=(20,30,40,50)
>>> 20 not in t
False
>>> 30 in t
True
>>> 80 not in t
True
>>> s={'xyz':'abc','123':'890','wsd':'python'}
>>> 'xyz' in s
True
>>> 'abc' in s
False
>>> 'python' not in s
True
>>> 'python' in s
False
>>> 'wsd' not in s
False
>>> 'name' not in s
True
>>> l= [1,2,3,4]
>>> m=[1,2,3,4]
>>> l=m
>>> l==m
True
>>> l is m
True
>>> id(l)
4435908032
>>> id(m)
4435908032
>>> l=[1,2,3,4]
>>> m=[1,2,3,4]
>>> l==m
True
>>> id(l)
4336260928
>>> id(m)
4435842240
>>> l is m
False
>>> n=m
>>> n is m
True
>>> m is l
False
>>> l is not m
True
>>> 11 & 12
8
>>> 11 | 12
15
>>> 11 ^ 12
7
>>> 11 ~ 12
SyntaxError: invalid syntax
>>> 11 << 12
45056
>>> 11 >> 12
0
