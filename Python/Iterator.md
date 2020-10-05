## Python iterator
### What is iterator and Why do we need it?

<HR size=1>

* 有多个对象需要从头到尾遍历一个集合中的所有元素，一个公共函数无法维护许多指针，那么需要将这种**遍历的行为**定义成一种对象，这就是迭代器。

  <font size=2 color=gray>（完全可以不需要维护一个真实的数据列表/集合，只是一种行为上的抽象)</font>



### How to define an iterator?

<HR size=1>

#### Basic usage

```python
class MyClass:
    def __init__(self):
        xxx
        return self
   
   def __next__(self):
        xxx
        return x
        xxx
        raise StopIteration
```
```python
c=MyClass()
c_iter=iter(c)

for x in c:
    xxxxx
```


## Python Generator
### Defination:

<HR size=1>

* 只要一个函数中使用了 ```yield``` 关键字，就代表这个函数时一个生成器。 <font size=2 color="gray">实现了iterator接口，所以可以认为generator返回后返回了一个iterator</font>

* 懒执行 <i>lazy evaluation</i>

* Generator 实际上是返回了控制流，执行到yeild语句时，保存当前状态，返回结果，并将当前的执行流还给调用它的函数。再次调用它时，Generator就从上次yield的位置继续执行

  

###  How to use it:

<HR size=1>

```python
def MyClass:
    id=-1
    while True:
        id+=1
        yield GetResourceById(id)
#使用
for resource in MyClass():
    #do operations.	
```



###  Compare with iterator:

```python
#Fibonacci implementation by generator
def fibonacci_gen():
    a,b=(1,1)
    while True:
        yield a
        a,b=b,a+b

for x in fibonacci_gen():
    print(x)

#Fibonacci implementation by iterator
class fibonacci_iter:
    def __init__(self):
        self.a,self.b=1,1
    def __iter__(self):
        return self:
    def __next__(self):
        result=self.a
        self.a,self.b=self.b,self.b+self.a
        return result
f = fibonacci_iter()
f_iter=iter(f)
while True:
    print(next(f_iter))
```

#### Yield keep the state of  function in stack, return to the calling point

```python
def gen():
    print(1)
    yield
    print(2)
    yield
it=gen()

next(it)
#1
next(it)
#2
```

#### Yield from usage(Used to combine multiple generator)

```python
#Without yield from:
def odds(n):
    for i in range(n):
        if i % 2 == 1:
            yield i

def evens(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

def odd_even(n):
    for x in odds(n):
        yield x
    for x in evens(n):
        yield x

for x in odd_even(6):
    print(x)
#=> 1, 3, 5, 0, 2, 4

# With help of yield from:
def odd_even(n):
    yield from odds(n)
    yield from evens(n)
```

