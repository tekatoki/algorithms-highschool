'''
Exercici III Olimpíada Informàtica Illes Balears 2024 

📖 Com a dissenyador de tirolines, et trobes davant el repte d'unir un gratacel amb el terra mitjançant una tirolina.
La tasca consisteix a calcular la longitud precisa d'aquesta connexió, tenint en compte la distància horitzontal cap a l'edifici i la d'altura del gratacel.
Aquesta missió requereix càlculs, utilitzant l'alçada de l'edifici i la distància al mateix, per assegurar una instal·lació exitosa.
↕️ Entrada i sortida
L'entrada es llegirà des del terminat i consistirà en diversos casos de prova. El primer número indica la quantitat de casos de prova a seguir.
Cada cas de prova conté dos números: l'altura de l'edifici i la distància horitzontal a terra.
Per a cada cas de prova, has de calcular i mostrar la longitud de la tirolina arrodonida a l'enter més proper.

✏️ Exemple

Entrada:
3
5 12
3 4
8 15

Sortida:
13
5
17

⚠️ Restriccions

L'altura màxima dels edificis és de 100 metres.

La distància màxima és de 100 metres.

🧩 Subtasques
(100 punts) L'altura i la distància màxima és 100.
'''

import math
results = []
times_iteration = int(input())

i = 0
while i < times_iteration: 
    data = input().split(' ')
    
    # data management
    a = 0
    for element in data:
        data[a] = int(data[a])
        # subtask and security comprobation
        if 100 < data[a] or len(data) > 2:
            raise Exception
        a += 1

    x = (data[0]**2 + data[1]**2)
    # print(x)
    results.append(round(math.sqrt(x)))

    i += 1 

for result in results:
    print(result)
