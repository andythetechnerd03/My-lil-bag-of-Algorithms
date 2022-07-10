# In this file, I'll show you how to properly stress test any algorithms using randomizer. Testing the correctedness
# of any algorithm is the most important after-step you need to take to verify the reliability of your program.

# If you're doing an exercise and the algorithm you're trying to build is the familiar one that already has a
# solution online then it's great!

import random
import math
import time


# setting three sample algorithms - a naive, faster and (supposedly) instant algorithm for calculating Fibonacci

def fibonacci(n):
    # Naively, recursively speaking...
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def faster_fibonacci(n):
    # Faster, iteratively looking...
    if n == 1:
        return 0
    if n == 2:
        return 1
    previous, current = 0, 1
    for i in range(3, n + 1):
        x = previous + current
        previous, current = current, x
    return current

def instant_fibonacci(n):
    # For those who are wondering, this is the generic formula for Fibonacci number of n, which is O(logn) bc of
    # the existence of power function
    return int((1 / math.sqrt(5)) * (((0.5 + 0.5 * math.sqrt(5)) ** n) - ((0.5 - 0.5 * math.sqrt(5)) ** n)))


# here comes the test kits

while True:
    a = random.randint(100, 200)
    print("================")
    print(a)
    b = faster_fibonacci(a)
    print(b)
    c = instant_fibonacci(a-1)
    print(c)
    if b != c:
        break

# The test will randomly pick an integer in a specified interval, calculate the value of both algos,
# and compare them, effectively stopping the whole program if the 2 values are different (bugs)
# In the above test, the naive algorithm is too slow (O(n!)) so we replace it with faster one and compare it to the
# instant algo, in which case, the instant algo will produce wrong result with n sufficiently large!!
# SO, FASTER_FIBONACCI WINS!! It's still O(n) tho, but who cares?

# What about calculating time for each algorithm? Simple! Let's calculate F(40)

time1 = time.time()
fib1 = fibonacci(40)
time2 = time.time()
fib2 = faster_fibonacci(40)
time3 = time.time()
fib3 = instant_fibonacci(40)
time4 = time.time()
print("Naive Fibonacci takes: ", time2 - time1)
print("Faster Fibonacci takes: ", time3 - time2)
print("Instant Fibonacci takes: ", time4 - time3)

# The three algos took: 15s, 0.0s and 0.0s respectively. Obviously the first one is gone for sure!!
