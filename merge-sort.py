import datetime
def merge(v, ini, meio, fim):
    p1 = ini
    p2 = meio + 1
    tam = fim - ini + 1
    temp = [0] * tam
    i = 0

    while p1 <= meio and p2 <= fim:
        if v[p1] < v[p2]:
            temp[i] = v[p1]
            p1 += 1
        else:
            temp[i] = v[p2]
            p2 += 1
        i += 1

    while p1 <= meio:
        temp[i] = v[p1]
        p1 += 1
        i += 1

    while p2 <= fim:
        temp[i] = v[p2]
        p2 += 1
        i += 1

    for j in range(tam):
        v[ini + j] = temp[j]



v = [1,6,3,4,5,8]
tempoInicial = datetime.datetime.now()
merge(v, 0, 2, 4)
tempoFinal = datetime.datetime.now()
soma = tempoFinal - tempoInicial
print(soma)

print(v)
