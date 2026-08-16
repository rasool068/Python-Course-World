Python 3.14.6 (v3.14.6:c63aec69bd5, Jun 10 2026, 08:07:54) [Clang 21.0.0 (clang-2100.1.1.101)] on darwin
Enter "help" below or click "Help" above for more information.
#input formatting
#int float complex str list tuple set dict bool
a=input()
Rasool Dudekula
a
'Rasool Dudekula'
a=input()
a=122
a
'a=122'
a=input("enter the value:")
enter the value:43
a
'43'
a=input("enter the value:")
enter the value:999
a
'999'
marks=input("enter the marks:")

enter the marks:990
marks
'990'
price=float(input("enter the price"))
enter the price222
price
222.0
cgpa=float(input("enter the cgpa:"))
enter the cgpa:8
cgpa
8.0

#split list of strings
#split & list of strings

name.split()
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    name.split()
NameError: name 'name' is not defined
names = ('rasool,cricket,etc')
names.split()
['rasool,cricket,etc']
names.split(',')
['rasool', 'cricket', 'etc']
softskills = 'communication quicklearner'
softskills
'communication quicklearner'
softskills.split()
['communication', 'quicklearner']
sofyskills.split(',')
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    sofyskills.split(',')
NameError: name 'sofyskills' is not defined. Did you mean: 'softskills'?
softskills.split(',')

['communication quicklearner']
names=tuple(input("enter the names:").split())
enter the names:rasool dudekula 
names
('rasool', 'dudekula')
names = set(input("Enter the names:").split())
Enter the names:rasool dudekula

#maps uses to iterate the value

marks=value().split()
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    marks=value().split()
NameError: name 'value' is not defined. Did you mean: 'False'?
marks = value().split()
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    marks = value().split()
NameError: name 'value' is not defined. Did you mean: 'False'?
marks=('11,22,33,44,55')
marks
'11,22,33,44,55'
marks=input().split()
marks
map(int,marks)
<map object at 0x1039ece00>
marks=list(map(int,input("Enter the marks").split()))
Enter the marks 33 44 55 99
marks
[33, 44, 55, 99]

marks=set(map(float,input("Enter the marks").split()))
Enter the marks32323008899
marks
{32323008899.0}
marks=bool(map(float,input("Enter the marks").split()))
Enter the marks999
marks
True
#Packinng and unpacking
a,b=[1,2]
a
SyntaxError: multiple statements found while compiling a single statement
a,b=[1,2]
a
1
b
2
a,b,c=(1,12.3,"str")
a
1
b
12.3
c
'str'
email,password=input("Enter the email,password:").split()
Enter the email,password:230dfeoif
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    email,password=input("Enter the email,password:").split()
ValueError: not enough values to unpack (expected 2, got 1)
email,password=input("Enter the email,password:").split()

Enter the email,password:rasool222@222
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    email,password=input("Enter the email,password:").split()
ValueError: not enough values to unpack (expected 2, got 1)
email,password=input("Enter the email,password:").split()

Enter the email,password:rasoool@1234 rasool123
email
'rasoool@1234'
password
'rasool123'
name,marks=input("Enter the name and marks:").split()
Enter the name and marks:33
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    name,marks=input("Enter the name and marks:").split()
ValueError: not enough values to unpack (expected 2, got 1)
name,marks=input("Enter the name and marks:").split()
Enter the name and marks:rasool 99
name
'rasool'
marks
'99'
int(marks)
99
a,b,c=list(map(int,input().split()))
22
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    a,b,c=list(map(int,input().split()))
ValueError: not enough values to unpack (expected 3, got 1)
22 33 44
SyntaxError: invalid syntax
a
1
a,b,c=list(map(int,input().split()))
22 33 44
SyntaxError: multiple statements found while compiling a single statement
#Eval function for the boolen value only
status=eval(input())
true
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    status=eval(input())
  File "<string>", line 1, in <module>
    __import__('idlelib.run').run.main(True)
NameError: name 'true' is not defined. Did you mean: 'True'?
True
True
Status
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    Status
NameError: name 'Status' is not defined
status=eval(input())
True
>>> Status
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    Status
NameError: name 'Status' is not defined. Did you mean: 'status'?
>>> type(status)
<class 'bool'>
>>> status=eval(input())
...    
>>> 2+7j
(2+7j)
>>> <class 'complex'>
SyntaxError: invalid syntax
>>> >>> status=eval(input())
SyntaxError: invalid syntax
>>> >>> status=eval(input())
SyntaxError: invalid syntax
>>> >>> status
SyntaxError: invalid syntax
>>> status
Ellipsis
>>> status=eval(input())
[1,3,5,7]
>>> status
[1, 3, 5, 7]
>>> status=eval(input())
status=eval(input())
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    status=eval(input())
  File "<string>", line 1
    status=eval(input())
                ^^^^^
SyntaxError: invalid syntax. Did you mean 'not'?
>>> status
[1, 3, 5, 7]
>>> type(status)
<class 'list'>
