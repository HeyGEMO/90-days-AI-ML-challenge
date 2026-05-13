def calc_fact(n):
    multi=1
    for i in range(1,n):
        i=i+1
        multi=i*multi
    print(multi)
print(calc_fact(5))

def conversion(usd_val):
    NPR=147
    convert=usd_val*NPR
    print(usd_val,"USD to NPR = RS.", convert)
conversion(4)
