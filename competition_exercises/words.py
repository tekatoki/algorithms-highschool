'''
Exercici III Olimpíada Informàtica Illes Balears 2024 

📖 El meu germà petit està aprenent a escriure i encara no sap en quin moment ha de fer servir majúscules o minúscules.
En una mateixa paraula escriu en majúscules i minúscules de manera aleatòria.
Ajuda'l a corregir les seves frases fent que només la primera lletra de cada paraula estigui en majúscules i la resta en minúscules.

↕️ Entrada i sortida

L'entrada consisteix en el nombre de casos de prova que indica el nombre de frases a corregir.

Cada cas de prova consisteix en una línia amb caràcters alfabètics i espais, amb un màxim de 80 caràcters. 
Per simplificar el problema no apareixeran lletres amb accents ni caràcters especials.

La sortida consisteix en la frase d'entrada amb la mateixa longitud de caràcters i només la primera lletra de cada paraula en majúscula.

✏️ Exemple

Entrada:
3
pROGRAMACIO
OlImPiAdA iNfOrMaTiCa
BenvingutS          OlimpiadA InformaticA                        IlleS BalearS                 HappY CodE

Sortida:
Programacio
Olimpiada Informatica
Benvinguts          Olimpiada Informatica                        Illes Balears                 Happy Code
'''
times_iteration = int(input())
results = []

i = 0
while i < times_iteration:
    i2 = 0
    for word in input().split(' '):
        if 0 == i2:
            phrase = word.capitalize()
        else:
            phrase += '\t' + word.capitalize() 
        i2 += 1
    results.append(phrase)
    i += 1

for result in results: 
    print(result.strip())
