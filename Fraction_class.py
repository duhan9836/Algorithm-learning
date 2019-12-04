#def a Fraction class, which has two attributes: numerator and denomitor, and three methods: __str__,__add__,__eq__
#understand the differences between shallow equation and deep equation
def gcd_euclid_recursion(m,n):
    m=abs(m)
    n=abs(n)
    if m==n:
        return m
    elif m<n:
        m,n=n,m
    if m%n==0:
        return n
    else:
        temp=m%n
        m=n
        n=temp
        euc=gcd_euclid_recursion(m,n)
        return euc

class Fraction:
    def __init__(self,num,den):
        gcd=gcd_euclid_recursion(num,den)
        if num*den>0:
            self.num=abs(int(num/gcd))
            self.den=abs(int(den/gcd))
        if num*den<0:
            self.num = -abs(int(num/gcd))
            self.den = abs(int(den/gcd))
    def __str__(self):
        return "{}/{}".format(self.num,self.den)
    def show(self):
        print ("{}/{}".format(self.num,self.den))
    def __add__(self,otherFraction):
        newnum=self.num*otherFraction.den+self.den*otherFraction.num
        newden=self.den*otherFraction.den
        gcd=gcd_euclid_recursion(newnum,newden)
        return Fraction(newnum/gcd,newden/gcd)
    def __iadd__(self, otherFraction):
        newnum = self.num * otherFraction.den + self.den * otherFraction.num
        newden = self.den * otherFraction.den
        gcd = gcd_euclid_recursion(newnum, newden)
        self.num=int(newnum/gcd)
        self.den=int(newden/gcd)
        return self
    def __sub__(self,otherFraction):
        newnum = self.num * otherFraction.den - self.den * otherFraction.num
        newden = self.den * otherFraction.den
        gcd = gcd_euclid_recursion(newnum, newden)
        return Fraction(newnum / gcd, newden / gcd)
    def __mul__(self,otherFraction):
        newnum = self.num * otherFraction.num
        newden = self.den * otherFraction.den
        gcd = gcd_euclid_recursion(newnum, newden)
        return Fraction(newnum / gcd, newden / gcd)
    def __truediv__(self, other):
        newnum =self.num*other.den
        newden=self.den*other.num
        gcd=gcd_euclid_recursion(newnum,newden)
        return Fraction(newnum/gcd,newden/gcd)
    def __eq__(self,otherFraction):
        firstnum=self.num*otherFraction.den
        secondnum=otherFraction.num*self.den
        return firstnum==secondnum
    def __gt__(self, otherFraction):
        firstnum = self.num * otherFraction.den
        secondnum = otherFraction.num * self.den
        return firstnum > secondnum
    def getNum(self):
        return self.num
    def getDen(self):
        return self.den


f1=Fraction(2,-4)
f2=Fraction(5,15)
print(f1)
print(f2)
print(f1+f2)
print(f1-f2)
print(f1*f2)
print(f1/f2)
print(f1==f2)
print(f1>f2)
print(f1.getNum())
print(f2.getDen())
f1+=f2
print(f1.getNum())
print(f1.getDen())