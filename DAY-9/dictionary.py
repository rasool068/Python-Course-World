Python 3.14.6 (v3.14.6:c63aec69bd5, Jun 10 2026, 08:07:54) [Clang 21.0.0 (clang-2100.1.1.101)] on darwin
Enter "help" below or click "Help" above for more information.
#dictionary
#mut ord het dyn unidu
d = {}
type(d)
<class 'dict'>
d = {1:4,2:8,3:18}
d
{1: 4, 2: 8, 3: 18}
d = {}
d[1]=1
d[12.3]=1
d['str']=1
d[(1,2,3)]=1
d[(2+3j)]=1
d[True]=1
d[[1,2,3]]=1
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    d[[1,2,3]]=1
TypeError: cannot use 'list' as a dict key (unhashable type: 'list')
d[1]=1
d[2]=12.3
d[3]='str'
d[4]=True
d[5]=[1,2,3]
d[6]=(1,2,3)
d[7]={1,2,3}
d[8]={1,2,3}
d[9]=frozenset({1,2,3})
d[10]={1:2,2:3}
d[11]=False
d
{1: 1, 12.3: 1, 'str': 1, (1, 2, 3): 1, (2+3j): 1, 2: 12.3, 3: 'str', 4: True, 5: [1, 2, 3], 6: (1, 2, 3), 7: {1, 2, 3}, 8: {1, 2, 3}, 9: frozenset({1, 2, 3}), 10: {1: 2, 2: 3}, 11: False}
d={}
d[1]=2
d[1]=3
d
{1: 3}
data = {'name':'rasool','course':'pfs','batch':65}
data
{'name': 'rasool', 'course': 'pfs', 'batch': 65}
'rasool' in data
False
'course' in data
True
data['name']
'rasool'
data['batch']
65
data['age']
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    data['age']
KeyError: 'age'
>>> data['age']=21
>>> data
{'name': 'rasool', 'course': 'pfs', 'batch': 65, 'age': 21}
>>> data['phnno']=12312323
>>> data
{'name': 'rasool', 'course': 'pfs', 'batch': 65, 'age': 21, 'phnno': 12312323}
>>> data.update({'email':'dinesh@gmail.com','py':2026})
>>> data
{'name': 'rasool', 'course': 'pfs', 'batch': 65, 'age': 21, 'phnno': 12312323, 'email': 'dinesh@gmail.com', 'py': 2026}
>>> data['age']=22
>>> id(data)
4389234560
>>> data.popitem()
('py', 2026)
>>> data.pop('course')
'pfs'
>>> data
{'name': 'rasool', 'batch': 65, 'age': 22, 'phnno': 12312323, 'email': 'dinesh@gmail.com'}
>>> data.pop('age')
22
>>> data.clear
<built-in method clear of dict object at 0x1059e6780>
>>> 
>>> data.clear()
>>> data
{}
>>> len
<built-in function len>
>>> 
>>> len(data)
0
>>> data= {'name':'rasool','course':'pfs','batch':65}
>>> len(data)
3
>>> data.keys()
dict_keys(['name', 'course', 'batch'])
data.values()
dict_values(['rasool', 'pfs', 65])
data.items()
dict_items([('name', 'rasool'), ('course', 'pfs'), ('batch', 65)])
sorted(data)
['batch', 'course', 'name']
max(data)
'name'
min(data)
'batch'
min(data)
'batch'
d={1:2,2:3}
m=d
m[3]=3
m
{1: 2, 2: 3, 3: 3}
d
{1: 2, 2: 3, 3: 3}
n=d.copy()
n[5]=5
n
{1: 2, 2: 3, 3: 3, 5: 5}
d
{1: 2, 2: 3, 3: 3}
data
{'name': 'rasool', 'course': 'pfs', 'batch': 65}
data.get('py')
data.setdefault('py',2026)
2026
data.setdefault('name',2026)
'rasool'
data.setdefault('email',2026)
2026
data.setdefault
<built-in method setdefault of dict object at 0x10a9bb0c0>
data.setdefault('key',2026)
2026
dict.fromkeys(["python","mysql","java"],0)
{'python': 0, 'mysql': 0, 'java': 0}
