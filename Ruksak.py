def r(cost, volumul, rucsac):
    index = list(range(len(cost)))
    raport = [v / w for v, w in zip(cost, volumul)]
    index.sort(key = lambda i: raport[i], reverse=True)
    max_cost = 0
    frac = [0] * len(cost)
    for i in index:
        if volumul[i] <= rucsac:

            frac[i] = 1
            max_cost += cost[i]
            rucsac -= volumul[i]
        else:

            frac[i] = rucsac/ volumul[i]
            max_cost += cost[i] * rucsac/ volumul[i]
            break
 
    return max_cost, frac
n = int(input("Cate Lucruri sunt in total: "))
cost = [int(input(f"Valoarea a {n} lucruri: ")) for _ in range(n)]
volumul= [int(input(f"Volumul a {n} lucruri: ")) for _ in range(n)]
rucsac = int(input("Volumul rucsacului: "))
max_val, frac = r(cost, volumul, rucsac)
for i in range(len(frac)):
    print(f"In rucsac incap {round(frac[i], 2)} lucruri cu pretul de {cost[i]}")
print('Suma lucrurilor adunate:', max_val)