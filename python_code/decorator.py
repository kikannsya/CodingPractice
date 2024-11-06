def bar(func):
    def inner():
        print('start func')
        func()
        print('end func')
    return inner

@bar
def f1():
    print('f1 is called')

@bar
def f2():
    print('f2 is called')

f1()
f2()

# same 
def f1():
    print('f1 is called')

f1 = bar(f1)
f1()