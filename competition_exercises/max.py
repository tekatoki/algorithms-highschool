'''
Exercici III Olimpíada Informàtica Illes Balears 2024 

📖 El meu gos està aprenent els números i a comptar. El poso a prova de la següent manera:
li dic un conjunt de nombres i ha de dir-me quin és el nombre més gran i quantes vegades apareix.
De vegades soc jo qui ho fa malament, necessito ajuda.

↕️ Entrada i sortida

L'entrada consisteix en el nombre de casos de prova que indica el nombre de conjunts que he de resoldre.

Cada cas de prova consisteix en dues línies. La primera línia conté la mida del conjunt i la segona línia conté els nombres del conjunt. Com a molt hi haurà 1000 nombres i els seus valors són entre -10^6 i 10^6.

La sortida consisteix en dos nombres: el màxim del conjunt i el nombre de vegades que apareix.
'''
'''
✏️ Exemple

Entrada:
3
3
1 3 2
10
10 2 4 5 7 1 3 6 8 9
9
2 2 4 4 4 3 0 0 0

Sortida:
3 1
10 1
4 3
'''

index_len = int(input())

in_list_nums = input().split(' ')

list_nums = []
i = 0
while i < index_len:
    list_nums.append(int(in_list_nums[i]))
    i += 1


repeated_times = 0
for num in list_nums:
    if sorted(list_nums, reverse=True)[0] == num:
        repeated_times += 1
    else:
        pass

print(sorted(list_nums, reverse=True)[0], repeated_times)



