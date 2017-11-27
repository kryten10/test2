#import PrimeNumberFunction
from PrimeNumberFunction import isPrime

def main():
    number_primes = 0
    for i in range(0,10001):
        if isPrime(i):
            number_primes += 1
    print("number of primes is: ", number_primes)

main()