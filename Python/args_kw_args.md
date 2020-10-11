## Args and **kwargs usage
--<a href="https://www.geeksforgeeks.org/args-kwargs-python/"> Blog</a>
* ```*args``` 非keyword arguments
* ```**kwargs``` keyword arguments


### ```*args```
* 使用```*```来标志可以接收可变长的参数
* 有```*```之后可以接收除了正式定义的参数之外还可以接收任意数量额外的参数
* 有了```*```之后，可以对接收的参数直接进行迭代，或者是使用一些诸如```map``` ```filter```之类的高阶函数

```python
def myFunc(*argv):
    for arg in argv:
        print(arg)

>>> myFunc('Hello', 'Welcome', 'to', '...')
Hello
Welcome
to
```

### ```**kwargs```
```python
def myFunc(**kwargs):
    for key,value in kwargs.items():
        print("%s == %s"%(key,value))
>>>myFunc(first='hello', second='world')
first==hello
second=world
```

### More usage/example
```python
def myFun(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)
     
# Now we can use *args or **kwargs to
# pass arguments to this function : 
args = ("Geeks", "for", "Geeks")
myFun(*args)
 
kwargs = {"arg1" : "Geeks", "arg2" : "for", "arg3" : "Geeks"}
>>myFun(**kwargs)
arg1: Geeks
arg2: for
arg3: Geeks
arg1: Geeks
arg2: for
arg3: Geeks
```

```python
def myFun(*args,**kwargs):
    print("args: ", args)
    print("kwargs: ", kwargs)
 
 
# Now we can use both *args ,**kwargs to pass arguments to this function :
>>>myFun('geeks','for','geeks',first="Geeks",mid="for",last="Geeks")
Output:
args: ('geeks', 'for', 'geeks')
kwargs {'first': 'Geeks', 'mid': 'for', 'last': 'Geeks'}
```