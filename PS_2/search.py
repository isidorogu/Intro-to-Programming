import mortgage

value = input("Home Value: ")
p = input("Term (in years): ")
i = input("Annual Int Rate: ")
payment = input("Desired payment: ")

payment = int(payment)
value = float(value)
p = float(p)
i = float(i)/100*12

a = 0
c= 100000

while True:
    b = (a+c)/2
    Fc = (i*(value-b))/(1-(1+i)**(-p)) - payment
    print(c, Fc)

    if abs(Fc)<0.0001:
        break

    elif Fc>0:
        a = b
    else:
        c = b

print(b)
