import math

for _ in range(int(input())):
    data = input().split(' ')
    print(round(math.sqrt(int(data[0])**2 + int(data[1])**2)))
