import time, math


def test(a, t):
    time.sleep(t / 1000) #задержка
    print(f"Square root of {a} after {t} miliseconds is {math.sqrt(a)}")

sqrtRoot = float(input("Input:"))
afterTime = float(input("Milliseconds:"))
test(sqrtRoot, afterTime)
