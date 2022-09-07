#Samuel Lee ID: 20412795

file = open("1531_p3_output.txt", "a+")
input = open("input.txt").read()
a = input.splitlines()

first = []
second = []

for bob in a:
  if bob.split()[1].isdigit():
    first.append(bob)
  else:
    second.append(bob)

#first.sort(key = lambda f: f.split()[1])
second.sort(key = lambda f: f.split()[1])

for dab in first:
  second.append(dab)
  print(dab)
for bad in second:
  file.write(bad)
  file.write("\n")
  print(bad)

file.close()
#input.close()

with open("1531_p3_output.txt", 'r+') as temp:
  lines = temp.readlines()
  temp.seek(0)
  temp.writelines(line for line in lines if line.strip())
  temp.truncate()