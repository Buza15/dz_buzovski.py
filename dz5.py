
#Task 1

a = int(input("Enter a number: "))
c = input("choose into (b) or into (k): ")

if c == 'b':
    print("%d Байт = %d Килобайт" % (a, a*1024))
elif c == 'k':
    print("%d Килобайт = %d Байт" % (a, a/1024))

print('#####' * 10)


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




#Task 3

start = input()
end = input()
step = input()

for i in range(start, end, step):
    print(-1.24 * i ** 2 + i)

#Task 4


value = input("Type number")

for i in range(len(value) / 2):
    if value[i] != value[-(i+1)]:
        print('Not palindrome')
        break
else:
    print('Palindrome')

#Task 5


a = [1, 2, -3]

_sum = 0
_count = 0
for value in a:
    if value > 0:
        _sum += value
        _count += 1
print(_sum / (_count or 1))
