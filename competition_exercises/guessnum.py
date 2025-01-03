from sys import stdout 
from sys import stdin
import random
import time

judge_in_parametres = input().split(' ')
limit_N = int(judge_in_parametres[0])
limit_Q = int(judge_in_parametres[1])

judge_in = ''
last_big = 0
last_min = 0
while True:
    if '-' == judge_in or '=' == judge_in:
        break
    elif '>' == judge_in:
        if 0 != last_min and 0 != last_big:
            last_big = asking_num
            asking_num = random.randint(last_big + 1, last_min - 1)
        
        elif 0 != last_big:
            last_big = asking_num
            asking_num = random.randint(last_big + 1, limit_N)

        elif 0 != last_min:
            last_big = asking_num
            asking_num = random.randint(last_big + 1, last_min - 1)
        
        else:
            asking_num = random.randint(asking_num + 1, limit_N)
            last_big = asking_num
    
    elif '<' == judge_in:
        if 0 != last_min and 0 != last_big:
            last_min = asking_num
            asking_num = random.randint(last_big + 1, last_min - 1)
        
        elif 0 != last_min:
            last_min = asking_num
            asking_num = random.randint(1, last_min - 1)
        
        elif 0 != last_big:
            last_min = asking_num
            asking_num = random.randint(last_big + 1, last_min - 1)
        
        else:
            asking_num = random.randint(1, asking_num - 1)
            last_min = asking_num
    else:
        asking_num = random.randint(1, limit_N)
    
    print('?' + str(asking_num))
    stdout.flush()
    judge_in = input()


