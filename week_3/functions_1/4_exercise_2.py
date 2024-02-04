def isPrime(num):
    cnt = 0
    for i in range(1, num + 1):
        if num % i == 0:
            cnt = cnt + 1
    return cnt == 2


mylist = map(int, input().split())
newlist = [x for x in mylist if isPrime(int(x))]
print(newlist)
