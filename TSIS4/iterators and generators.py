#1
def ngen(N):
    i = 0
    while True:      
        yield i*i
        if i == N:
            break
        else:
            i += 1
       
N = int(input())
print(*ngen(N))


#2
def evenums(n):
    nums = 0
    while True:
        if (nums % 2) == 0:
            yield nums
        if nums == n:   #endpoint
            break
        else: nums += 1

n = int(input())
print(*evenums(n), ' ')


#3
def threefour(n):
    i = 0
    while True:
        if (i % 3 == 0) and (i % 4 == 0):
            yield i
        if i == n:
            break
        else: i += 1

n = int(input())
print(*threefour(n), ' ')


#4
a = int(input())
b = int(input())
def squares(a, b):
    for i in range(a, b+1):   #to include b
        yield i**2

print(*squares(a, b), ' ')


#5
def retrn(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input())
for i in retrn(n):
    print(i)