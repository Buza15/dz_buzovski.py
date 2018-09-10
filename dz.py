
#Task 1

a = int(input("Enter a number: "))
c = input("choose into (b) or into (k): ")

if c == 'b':
    print("%d Байт = %d Килобайт" % (a, a*1024))
elif c == 'k':
    print("%d Килобайт = %d Байт" % (a, a/1024))


#Task 2

n = int(input("Enter a number: "))
s = 0
m = 1
while n > 0:
    s += n%10
    m *= n%10
    n = n//10

print("Summ: ", s)
print ("Multiply", m)



def foo1():
    pass

def foo_with_return():
    return True

def foo_with_params(param1):
    pass

def foo_args(*args):
    print('FOO ARGS', args)

foo_args(1, 2, 3, 4)


def foo_kwargs(**kwargs):
    print('FOO KWARGS', kwargs)

foo_kwargs(a=1, b=2)

print('#' * 20)
def foo_arr(_list, operation=None):
    result = 0
    for elem in _list:
        result = operation(result, elem)
    return result

print(
    foo_arr([1, 2, 3],
    operation=lambda x, y: x + y)
)


print('sam #' * 15)
def foo1(x):
    x ** 2

def foo2(x):
    return 2 * x -1

def foo3(x):
    return 2 * x -1

def foo_result(x):
    if -5 <= x <= 5:
        result = foo1(x)
    elif x > 5:
        result = foo2(x)
    elif x  -5:
        result = foo3(x)

    return result














sdsd
sds
sdsd
sd
sds
delattr(s)





































































