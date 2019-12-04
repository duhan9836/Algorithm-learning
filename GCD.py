#define a function, that given two positive integers, m and n, the function will return their greatest common divisor,GCD
import random
def gcd(m,n):
    if m==n:
        return m
    elif m<n:
        m,n=n,m
    if m%n==0:
        return n
    else:
        i=n-1
        while i>1:
            if m%i==0 and n%i==0:
                return i
            i=i-1
        return 1
population=list(range(1000))
ms=random.choices(population,k=10)
ns=random.choices(population,k=10)
print(ms,ns)

for m in ms:
    for n in ns:
        print((m,n),gcd(m,n))
