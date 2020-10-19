from collections import Iterable
def flatten(items,ignore_types=(str,bytes)):
    for x in items:
        if isinstance(x,Iterable) and not isinstance(x,ignore_types):
            yield from flatten(x)
        else:
            yield x

a=[1,2,[3,4,5],[1,[1,[1]]]]
for i in flatten(a):
    print(i)