>>> a=b=c=10
>>> a
10
>>> b
10
>>> c
10
>>> a,b,c=120,240,360
>>> a
120
>>> b
240
>>> c
360
>>> a,b=b,a
>>> a
240
>>> b
120
>>> del c
>>> c
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    c
NameError: name 'c' is not defined
