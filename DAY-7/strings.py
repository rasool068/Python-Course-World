Python 3.14.6 (v3.14.6:c63aec69bd5, Jun 10 2026, 08:07:54) [Clang 21.0.0 (clang-2100.1.1.101)] on darwin
Enter "help" below or click "Help" above for more information.
#strings
#white spaces and trimming methods
s = ' Hello World
SyntaxError: unterminated string literal (detected at line 1)
s.strip()
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    s.strip()
NameError: name 's' is not defined
s = " Hello World "
s.strip()
'Hello World'
s.lstrip()
'Hello World '
s.rstrip()
' Hello World'
s.replace(" ","")
'HelloWorld'
#splitting and joining methods
s = 'java-python-flask-mysql-fastaou-c'
s.split('-')
['java', 'python', 'flask', 'mysql', 'fastaou', 'c']
s.split
<built-in method split of str object at 0x10649f9b0>

s.split('-',20)
['java', 'python', 'flask', 'mysql', 'fastaou', 'c']
l = '''python'''
l = '''python
java
mysql
flask
'''
l
'python\njava\nmysql\nflask\n'
l.splitlines()
['python', 'java', 'mysql', 'flask']
c = ['python, 'java', 'mysql', 'flask']
     
SyntaxError: unterminated string literal (detected at line 1)
c = ['python, java, mysql, flask']
     
c
     
['python, java, mysql, flask']
''.join(c)
     
'python, java, mysql, flask'
', '.join(c)
     
'python, java, mysql, flask'
'@'.join(c)
     
'python, java, mysql, flask'
'-'.join(('1','2','3'))
     
'1-2-3'
a = 'strings.py'
     
a.partition('.')
     
('strings', '.', 'py')
a = 'string.py.java.png.txt'
     
a
     
'string.py.java.png.txt'
a.partiton('.')
     
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    a.partiton('.')
AttributeError: 'str' object has no attribute 'partiton'. Did you mean: 'partition'?
a.partition('.')
     
('string', '.', 'py.java.png.txt')
a.rpartition('.')
...      
('string.py.java.png', '.', 'txt')
>>> a.rpartition('.')
...      
('string.py.java.png', '.', 'txt')
>>> 
>>> #string testing methods
...      
>>> a='strings.png'
...      
>>> a.startswith('str')
...      
True
>>> a.startswith('list')
...      
False
>>> a.endswith('.py')
...      
False
>>> a.startswith('.png')
...      
False
>>> a.endswith('.png')
...      
True
>>> 'pythnv.13'.islower()
...      
True
>>> 'Pythnv.13'.islower()
...      
False
>>> 'PYTH@#$1233'.isupper()
...      
True
>>> 'estyu'.isalpha()
...      
True
>>> 'esty899u'.isalpha()
...      
False
>>> 'esty899u'.isalnum()
...      
True
>>> 'sejfefijergeir'.isalnum()
...      
True
>>> '     '.isspace()
...      
True
>>> '    Hello'.isspace()
...      
False
>>> 'HLo word'.istitle()
...      
False
>>> 'Hello World'.istitle()
...      
True
>>> 'my_var'.isidentifier()
...      
True
>>> 'my@var'.isidentifier()
...      
False
>>> a.partition('.')
...      
('strings', '.', 'png')
>>> a.rpartition('.')
...      
('strings', '.', 'png')
>>> '2321233'.isdecimal()
...      
True
>>> 'DJFNW124'.isdecimal()
...      
False
>>> '1233213'.isnumeric()
...      
True
