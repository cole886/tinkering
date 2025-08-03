
def multpli(a,b,c,d,e):
    return a*b*c*d*e

def add(a,b,c,d,e):
    return a + b + c + d + e

def sub(a,b,c,d,e):
    return a - b - c - d - e

def divide(a,b,c,d,e):
    return a/b/c/d/e

while True:
    try:
        a = float(input("Enter a number: "))
        b = float(input("Enter another number: "))
        c = float(input("Enter a third number: "))
        d = float(input("Enter a fourth number: "))
        e = float(input("Enter a fifth number: "))
        break

    except ValueError:
        print("Please enter valid integers.")


print(f" a={a} * b={b} *c={c} *d={d} *e={e} is  {multpli(a,b,c,d,e)}")
print(f" a={a} / b={b} /c={c} /d={d} /e={e} is  {divide(a,b,c,d,e)}")
print(f" a={a} + b={b} +c={c} +d={d} +e={e} is {add(a,b,c,d,e)}")
print(f" a={a} - b={b} -c={c} -d={d} -e={e} is {sub(a,b,c,d,e)}")                                 ```````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````