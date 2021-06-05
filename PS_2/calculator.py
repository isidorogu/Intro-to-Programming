value = input("Home Value: ")
down = input("Down Payment: ")
p = input("Term (in years): ")
i = input("Annual Int Rate: ")

value = float(value)
down = float(down)
p = float(p)
i = float(i)

l = value - down

p = p*12
i = i/100

import mortgage

a = mortgage.mortgage_pymnt(l, p, i)

print('Your payment is', round(a, 2))
