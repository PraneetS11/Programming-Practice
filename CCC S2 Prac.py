numInput = input()
primes = []
notprimes = []
avgs = []

def is_prime(num):
    if num in primes:
        return 1
    elif num in notprimes:
        return 0
    for i in range(num):
        if(i == 0 or i == 1):
            continue
        elif(not(num % i)):
            primes.append(num)
            return 0
    primes.append(num)
    return 1

for i in range(int(numInput)):
    avgs.append(int(input()))

for avg in avgs:
    if(is_prime(avg)):
        print(avg, " ", avg)
        continue
    total = avg * 2
    
    for j in range(total - avg - 1):
        high = avg + j + 1
        low = avg - j - 1
        if(is_prime(high) and is_prime(low)):
            print(high, " ", low)
            break
        else:
            continue