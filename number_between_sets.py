def getTotalX(a, b):
    # Write your code here

    LCM_a = LCM(a)
    GCD_b = GCD(b)
    total = 0
    num = LCM_a
    while GCD_b>=num:
        if GCD_b % num ==0:
            total += 1
        num += LCM_a
    return total


def LCM(a):
    if len(a)==1:
        return a[0]
    elif len(a)==2:
        return LeastCommonMultiple(a[0],a[1])
    else:
        return LeastCommonMultiple(LCM(a[:2]),LCM(a[2:]))

def GCD(b):
    if len(b) == 1:
        return b[0]
    if len(b) == 2:
        return GreatestCommonDivider(b[0], b[1])
    if len(b) > 2:
        return GreatestCommonDivider(GCD(b[:2]), GCD(b[2:]))


def GreatestCommonDivider(x, y):
    mini, maxi = min(x, y), max(x, y)
    if maxi % mini == 0:
        return mini
    else:
        return GreatestCommonDivider(mini, maxi % mini)


def LeastCommonMultiple(x, y):
    gcd = GreatestCommonDivider(x, y)
    return x * y / gcd

a=[2,3,6]
b=[42,84]

print("LCM_a is {},\n GCD_b is {}, \n and numbers_between_two_sets are {}".format(LCM(a),GCD(b),getTotalX(a,b)))



