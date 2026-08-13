Python 3.14.6 (v3.14.6:c63aec69bd5, Jun 10 2026, 08:07:54) [Clang 21.0.0 (clang-2100.1.1.101)] on darwin
Enter "help" below or click "Help" above for more information.
#lists
l = []
l = list()
type(l)
<class 'list'>
l= [1,12,13.9,"str",True,[1,2,3],(1,2,3),{1:1,2:2},9+19j]
l
[1, 12, 13.9, 'str', True, [1, 2, 3], (1, 2, 3), {1: 1, 2: 2}, (9+19j)]
l[1,1,1,1]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    l[1,1,1,1]
TypeError: list indices must be integers or slices, not tuple
l= [1,1,1,1]
l
[1, 1, 1, 1]
#list operations
a = [1,2,3,]
b = [4,5,6,]
a+b
[1, 2, 3, 4, 5, 6]
a*3
[1, 2, 3, 1, 2, 3, 1, 2, 3]
a=[568,68,13,45,99]
a
[568, 68, 13, 45, 99]
a[1]
68
a[3]
45
a[-1]
99
a[-5]
568
a[-2]
45
a
[568, 68, 13, 45, 99]
a[1:4]
[68, 13, 45]
a[::-1]
[99, 45, 13, 68, 568]
a[-1:-4:-1]
[99, 45, 13]
a[-1:-2:-1]
[99]
a[1::2]
[68, 45]
99 in a
True
899 is not in a
SyntaxError: invalid syntax
899 not in a
True
max[a]
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    max[a]
TypeError: 'builtin_function_or_method' object is not subscriptable
a
[568, 68, 13, 45, 99]
maz
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    maz
NameError: name 'maz' is not defined. Did you mean: 'max'?
max(a)
568
sorted(a)
[13, 45, 68, 99, 568]
len(a)
5
a
[568, 68, 13, 45, 99]
id(a)
4387301056
a[0]
568
a[0]=56
a
[56, 68, 13, 45, 99]
id(a)
4387301056
a[3]=45
a
[56, 68, 13, 45, 99]
a[-1] = 23
a
[56, 68, 13, 45, 23]
id(a)
4387301056
a.append(50)
a
[56, 68, 13, 45, 23, 50]
a.pop()
50
>>> a.pop(2)
13
>>> a
[56, 68, 45, 23]
>>> a.insert(90)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    a.insert(90)
TypeError: insert expected 2 arguments, got 1
>>> a.insert(1,99)
>>> a
[56, 99, 68, 45, 23]
>>> a.extend([1,2,3,4])
>>> a
[56, 99, 68, 45, 23, 1, 2, 3, 4]
>>> a.remove(23)
>>> a
[56, 99, 68, 45, 1, 2, 3, 4]
>>> a.remove(99)
>>> a
[56, 68, 45, 1, 2, 3, 4]
>>> a.clear()
>>> a
[]
>>> a.index(68)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    a.index(68)
ValueError: list.index(x): x not in list
>>> a = [56, 68, 45, 1, 2, 3, 4]
... a
SyntaxError: multiple statements found while compiling a single statement
>>> a = [1,2,3,4]
>>> b = a
>>> b
[1, 2, 3, 4]
>>> b.append(99)
>>> b
[1, 2, 3, 4, 99]
>>> a
[1, 2, 3, 4, 99]
>>> b
[1, 2, 3, 4, 99]
>>> c = a.copy()
>>> c.append(12)
>>> c
[1, 2, 3, 4, 99, 12]
>>> any([1,'',False,[],{},())
...     
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
>>> any([1,'',False,[],{})
...     
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
>>> any([1,'',False,[],{},set()])
...     
True
>>> l.sort()
...     
>>> l=[1,2,3,4]
...     
>>> l
...     
[1, 2, 3, 4]
>>> a.sort()
...     
>>> a
...     
[1, 2, 3, 4, 99]
>>> a.reverse()
...     
>>> a
...     
[99, 4, 3, 2, 1]
>>> a.reverse()
...     
>>> a
...     
[1, 2, 3, 4, 99]
