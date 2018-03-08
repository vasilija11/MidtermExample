def suma_cifara(broj):

    suma= 0
    for i in str(broj):
       cifra= int(i)
       suma= suma+ cifra
       print(cifra)
    return suma


def suma_cifara_matematicari(broj):
    suma=0
    while (broj > 0):
        cifra = broj % 10
        broj = broj // 10
        suma= suma+cifra
        print(cifra)


#print(suma_cifara(123))
print("------------")
print(suma_cifara_matematicari(1123423))