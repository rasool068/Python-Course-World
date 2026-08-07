Python 3.14.6 (v3.14.6:c63aec69bd5, Jun 10 2026, 08:07:54) [Clang 21.0.0 (clang-2100.1.1.101)] on darwin
Enter "help" below or click "Help" above for more information.
>>> a=money
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    a=money
NameError: name 'money' is not defined. Did you mean: 'None'?
>>> a = money
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    a = money
NameError: name 'money' is not defined. Did you mean: 'None'?
>>> 'a' = 'money'
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
>>> a = 10
>>> b = 20
>>> c = 'codegnan'
>>> print(a,b,c)
10 20 codegnan
>>> print('a=',a,'b=',b,'c=',c)
a= 10 b= 20 c= codegnan
>>> print('a=',a,'b=',b,'c=',c,sep='\n')
a=
10
b=
20
c=
codegnan
>>> print('a=',a,'b=',b,'c=',c,sep='')
a=10b=20c=codegnan
>>> print('a=',a,'b=',b,'c=',c,sep='\t')
a=	10	b=	20	c=	codegnan
>>> print('a=',a,'b=',b,'c=',c,sep='\n\n')
a=

10

b=

20

c=

codegnan
>>> print('a=',a,'b=',b,'c=',c,sep='\t',end='\n\n')
a=	10	b=	20	c=	codegnan

>>> print (f'a={a},b={b},c={c}')
a=10,b=20,c=codegnan
>>> #recommended format
>>> print (f'a={a},b={b},c={c}')
a=10,b=20,c=codegnan
