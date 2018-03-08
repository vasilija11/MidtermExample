#Broj mora da ima 9 ili 10 cifara
#Broj mora da pocinje sa 06
#Treca cifra mora biti jedna od [3, 6, 7, 8, 9]
#Moraju biti sve cifre

def validan_broj(broj_telefona):

    if not broj_telefona.isnumeric():
        return False

    if  len(broj_telefona) not in[9,10]:
        return False

    if not broj_telefona.startswith("06"):
        return False

    if not broj_telefona[2] in [3, 6, 7, 8, 9]:
        return False


print(validan_broj("069999123"))
