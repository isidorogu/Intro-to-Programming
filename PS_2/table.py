import mortgage

value = input("Home Value: ")
p = input("Term (in years): ")
i = input("Annual Int Rate: ")
min = input("Minimum Down Payment: ")
max = input("Maximum Down Payment: ")

min = float(min)
max = float(max)
min = int(min)
max = int(max)
value = float(value)
p = float(p)
i = float(i)

if (min>max):
    print('Minimun has to be lower than maximum')
else:
    for x in range(min, max, 1000):
        l = value - x
        p = p*12
        i = i/100


        a = mortgage.mortgage_pymnt(l, p, i)

        print( x,'Your payment is', round(a, 2))
