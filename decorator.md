## Decorator
<a href="https://www.programiz.com/python-programming/decorator">
<font color="gray"> - Blog</font>
</a>

### Prerequisites

* Everything in python is object <small>(- Functions are no exception)</small>
* Functions and methoeds are called ```callable```
  * Callable Function/method/lambda/Class/Class implement ```__call__```

### What does decorator do?

* Takes in a function, **adds some functionality** and **returns it**

```python
def ordinary():
    print('Hello World.')

def decorate(func):
    def decorated():
        print('Decorator does something...')
        func()
    return inner

>>>ordinary()
Hello World.

>>>d=decorate(ordinary)
>>>d()
Decorator does something...
Hello World.
```
  
### Python syntax for decorator

```python
@decorate
def ordinary():
    print('Hello World!')
```

* This is just a syntactic sugar to implement decorators.

### Decorating Functions with Parameters

```python
def divide(a,b):
    return a/b

def smart_divide(func):
    def inner(a,b):
        if b==0:
            return
        return func(a,b)
    return inner

@smart_divide
def divide(a,b):
   print(a/b) 
```
* We can use ```(*args, **kwargs)``` to make a general decorator<br>
where ```args``` will be the tuple of positional arguments and ```kwargs``` will be the dictionary of keyword arguments. 

```python
def works_for_all(func):
    def inner(*args, **kwargs):
        #do something
        return func(*args, **kwargs)
    return inner
```

### Chaining decorators
```python
def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner


@star
@percent
def printer(msg):
    print(msg)


>>>printer("Hello")
******************************
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
Hello
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
******************************
```