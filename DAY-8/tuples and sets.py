Python 3.14.6 (v3.14.6:c63aec69bd5, Jun 10 2026, 08:07:54) [Clang 21.0.0 (clang-2100.1.1.101)] on darwin
Enter "help" below or click "Help" above for more information.
t = ()
t = tuple()
t = (1,2,3,45)
t
(1, 2, 3, 45)
t = (1)
t
1
t = (1,)
t
(1,)
t = (1,1,1,1)
t
(1, 1, 1, 1)
t
(1, 1, 1, 1)
(1,2,3)+(1,2,3)
(1, 2, 3, 1, 2, 3)
(1,2,3)*4
(1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3)
t
(1, 1, 1, 1)
t[1]
1
t[-1]
1
t[-3]
1
t[2]
1
t[3:2]
()
t = (12,34,432,93,3423,43,54,55,99)
t
(12, 34, 432, 93, 3423, 43, 54, 55, 99)
sorted(t)
[12, 34, 43, 54, 55, 93, 99, 432, 3423]
max(t)
3423
min (t)
12
len (t)
9
t
(12, 34, 432, 93, 3423, 43, 54, 55, 99)
t.index(93)
3
sum(t)
4245
t.count(55)
1
all(1,2,3)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    all(1,2,3)
TypeError: all() takes exactly one argument (3 given)
all((1,2,3))
True
any((1,2,3))
True
all((1,2,3,00,000))
False
t = 1,2,3
t
(1, 2, 3)
a,b,c = t
a
1
b
2
c
3
#set
#mu unor het
s = set()
type(s)
<class 'set'>
s = {1,2,3,4,5,6,134,2323,232}
s
{1, 2, 3, 4, 5, 6, 134, 232, 2323}
s = {1,1,1,1,1,}
s
{1}
s = set()
s.add(1)
s.add(12.3)
s.add("str")
s.add([1,2,3])
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    s.add([1,2,3])
TypeError: cannot use 'list' as a set element (unhashable type: 'list')
s.add([1,2,3])
a = {1,2,3,4,5}
SyntaxError: multiple statements found while compiling a single statement
a = {1,2,3,4,5}
b = {3,5,4,8,9}
2 in a
True
10 in a
False
a|b
{1, 2, 3, 4, 5, 8, 9}
a&b
{3, 4, 5}
a-b
{1, 2}
b-a
{8, 9}
a
{1, 2, 3, 4, 5}
#{1}{1,2}{1,2,3,5},{4,5},{4,5,6}
a
{1, 2, 3, 4, 5}
{1}<=a
True
{1,2,3}<=a
True
a<={1,2}
False
m={1,2,3}
n={4,5,6}
n.isdisjoiny(m)
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    n.isdisjoiny(m)
AttributeError: 'set' object has no attribute 'isdisjoiny'. Did you mean: 'isdisjoint'?
n.isdisjoint(m)
True
n.isdisjoint(b)
False
a={12,43,2,4,89,99,44,45}
a
{2, 99, 4, 43, 12, 44, 45, 89}
sorted(a)
[2, 4, 12, 43, 44, 45, 89, 99]
>>> max(a)
99
>>> min(a)
2
>>> len(a)
8
>>> a.index(a)
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    a.index(a)
AttributeError: 'set' object has no attribute 'index'
>>> a.count(1)
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    a.count(1)
AttributeError: 'set' object has no attribute 'count'
>>> all({1,2,12,12,23,})
True
>>> any({0,''})
False
]
>>> sum(a)
338
>>> a
{2, 99, 4, 43, 12, 44, 45, 89}
>>> a = {1,2,3}
>>> a
{1, 2, 3}
>>> b=a
>>> a
{1, 2, 3}
>>> b.add(4)
>>> a
{1, 2, 3, 4}
>>> b
{1, 2, 3, 4}
>>> c=a.copy()
>>> c
{1, 2, 3, 4}
>>> c.add(5)
>>> c
{1, 2, 3, 4, 5}
>>> a
{1, 2, 3, 4}
>>> a.add(5)
>>> a
{1, 2, 3, 4, 5}
>>> a.add(100)
>>> a
{1, 2, 3, 4, 5, 100}
>>> a.add980)
SyntaxError: unmatched ')'
>>> a.add(80)
>>> a
{1, 2, 3, 4, 5, 100, 80}
>>> a.update({10,20,30,40})
>>> a.pop ()
1
>>> a.pop ()
2
>>> a.pop ()
3
>>> a.remove(80)
>>> a
{4, 5, 100, 40, 10, 20, 30}
>>> a.remove(100)
>>> a
{4, 5, 40, 10, 20, 30}
>>> a.discard(100)
>>> a.discard(30)
>>> a
{4, 5, 40, 10, 20}
>>> a.clear()
>>> a.clear()
>>> a
set()
>>> a = frozenset({1,2,3,4})
>>> a
frozenset({1, 2, 3, 4})
