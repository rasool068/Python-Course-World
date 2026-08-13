Python 3.14.6 (v3.14.6:c63aec69bd5, Jun 10 2026, 08:07:54) [Clang 21.0.0 (clang-2100.1.1.101)] on darwin
Enter "help" below or click "Help" above for more information.
#string operations
s ="codegnan"
s
'codegnan'
<class 'str'>
SyntaxError: invalid syntax
type (s)
<class 'str'>
s = ''
s
''
a='python'
b='programming'
a+b
'pythonprogramming'
fname='rasool'
lname='dudekula'
fname + lname
'rasooldudekula'
a
'python'
a*10
'pythonpythonpythonpythonpythonpythonpythonpythonpythonpython'
'*'*20
'********************'
'codegnan'*50
'codegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnan'
names = 'cricketers'
s='players'
s(2)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    s(2)
TypeError: 'str' object is not callable
s[2]
'a'
s[5]
'r'
s[6]
's'
s[-1]
's'
s[-5]
'a'
names= 'kohli' 'rohit' 'bumrah' 'bhuvi'
names
'kohlirohitbumrahbhuvi'
names= 'kohli', 'rohit' ,'bumrah', 'bhuvi'
names
('kohli', 'rohit', 'bumrah', 'bhuvi')
names[:1]
('kohli',)
names[8:13]
()
names='kohli rohit bumrah bhuvi'
names
'kohli rohit bumrah bhuvi'
names[:6]
'kohli '
names[8:13]
'hit b'
names[13:19]
'umrah '
names[12:18]
'bumrah'
names[:-6]
'kohli rohit bumrah'
kohli in names
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    kohli in names
NameError: name 'kohli' is not defined
'kohli' in names
True
len(names)
24
ord
<built-in function ord>
(
ord
<built-in function ord>
ord('a')
97
ord('v')
118
ord('A')
65
chr('100')
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    chr('100')
TypeError: 'str' object cannot be interpreted as an integer
chr(100)
'd'
chr('40')
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    chr('40')
TypeError: 'str' object cannot be interpreted as an integer
chr(40)
'('
sorted(names)
[' ', ' ', ' ', 'a', 'b', 'b', 'h', 'h', 'h', 'h', 'i', 'i', 'i', 'k', 'l', 'm', 'o', 'o', 'r', 'r', 't', 'u', 'u', 'v']
min
<built-in function min>
9
min(names)
' '
max(names)
'v'
#case conversion methods
s='python programming language'
s
'python programming language'
s.upper()
'PYTHON PROGRAMMING LANGUAGE'
s.lower()
'python programming language'
s.swapcase()
'PYTHON PROGRAMMING LANGUAGE'
s.title()'PYTHON PROGRAMMING LANGUAGE'
SyntaxError: invalid syntax
s.title()
'Python Programming Language'
s.casefold()
'python programming language'
"STRAẞEMÁLAGAÅngströmCafé".casefold()
'strassemálagaångströmcafé'
s.center(20,'-')
'python programming language'
s.center(50,'-')
'-----------python programming language------------'
s.center(50,'-')
s.ljust(30,'.')
SyntaxError: multiple statements found while compiling a single statement
s.center(30,'_')
SyntaxError: multiple statements found while compiling a single statement
SyntaxError: multiple statements found while compiling a single statement
s.center(30,'-')
'-python programming language--'
s.ljust(30,'_')
'-python programming language--'
SyntaxError: multiple statements found while compiling a single statement
s.rjust(30,'_')
'___python programming language'
>>> '123'.zfill(9)
'000000123'
>>> '88'.zfill(20)
'00000000000000000088'
>>> '999'.zfill(2)
'999'
>>> '999'.zfill(999)
'000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000999'
>>> s
'python programming language'
>>> s.find('python')
0
>>> s.find('g')
10
>>> s.find('p')
0
>>> s.rfind('a')
24
>>> s.rfind('g')
25
>>> s.find('z')
-1
>>> s.index('a')
12
>>> s.rindex('a')
24
>>> s.index(z')
...         
SyntaxError: unterminated string literal (detected at line 1)
>>> s.index('z')
...         
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    s.index('z')
ValueError: substring not found
>>> s.count('a')
...         
3
>>> s.count('m')
...         
2
>>> s.replace('o','1')
...         
'pyth1n pr1gramming language'
>>> s.replace('m','2')
...         
'python progra22ing language'
>>> s.replace('python','java')
...         
'java programming language'
>>> s.maketrans('amign','xyzlt')
...         
{97: 120, 109: 121, 105: 122, 103: 108, 110: 116}
>>> s.translate(s.maketrans('amign','xyzlt')
... 
...             s.translate(s.maketrans('amign','xyzlt')
... 
SyntaxError: '(' was never closed
>>> s.translate(s.maketrans('amign','xyzlt'))
...                         
'pythot prolrxyyztl lxtluxle'
>>> text = 'hello 😁'
...                         
>>> text.encode()
...                         
b'hello \xf0\x9f\x98\x81'
>>> text.decode()
...                         
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    text.decode()
AttributeError: 'str' object has no attribute 'decode'. Did you mean: 'encode'?
>>> b'hello \xf0\x9f\x98\x81'.decode()
...                         
'hello 😁'
