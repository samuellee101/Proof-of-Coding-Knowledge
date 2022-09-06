#Samuel Lee, ID: 20412795

import collections
from statistics import mode

file = open("input.txt", "r")
a = file.readline()
b = file.readline()
a = a.lower()
b = b.lower()
a = a.replace(',', "")
a = a.replace('\n',"")
apple = list(a.split(" "))
bear = list(b.split(" "))
apple_without_bear = [x for x in apple if x not in bear]
counts = collections.Counter(apple_without_bear)
print(apple_without_bear)
print(counts)
dab = [wrd for sub in apple_without_bear for wrd in sub.split()]
answer = mode(dab)
print(answer)
output_file = open("1531_p4_output.txt", "a+")
output_file.write(answer)
output_file.close()

with open("1531_p4_output.txt", 'r+') as temp:
    lines = temp.readlines()
    temp.seek(0)
    temp.writelines(line for line in lines if line.strip())
    temp.truncate()