a = int(input('Enter a number: '))
b = int(input('Enter another number: '))
def gcd(v,x):
    if v < x:
        v, x = x, v  # Ensure v is always the larger number
    array = []
    array.append(v)
    array.append(x)
    y = v % x
    array.append(y)
    while array[-1] != 0:
        array.append(array[-2] % array[-1])
    print("Remainder array:", array)
    gcd_val = array[-2]
    print("The GCD of the 2 numbers is " + str(gcd_val))

    # Extended GCD logic to find coefficients
    n = len(array) - 1
    s, old_s = 0, 1
    t, old_t = 1, 0

    for i in range(2, n + 1):
        quotient = array[i - 2] // array[i - 1]
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    print(f"Coefficients: x = {old_s}, y = {old_t}")
    print(f"Check: {v}*({old_s}) + {x}*({old_t}) = {gcd_val}")

gcd(a,b)