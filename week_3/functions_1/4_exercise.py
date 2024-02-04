def isPrime(num):
    cnt = 0
    for i in range(1, num + 1):
        if num % i == 0:
            cnt = cnt + 1
    return cnt == 2


def filter_prime(nums):
    res = []
    for x in nums:
        num = int(x)
        if isPrime(num) == True:
            res.append(num)
    return res


mylist = input().split(" ")
print(filter_prime(mylist))

newlist = [x for x in mylist if isPrime(int(x))]
print(newlist)
