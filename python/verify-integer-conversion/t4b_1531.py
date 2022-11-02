#Samuel Lee ID:20412795

#t4b

#works for a b
#works for 2 162
#works for 4 42
#works for 5 255 (personal test, not on the actual test)
#does not work for 100 40021
#after adding 'b portion' code works for 100 40021

input = open("t4b_input.txt", "r")
output = open("t4b_1531_output.txt", "w")

numbers = input.readline().split()
try:
  numbers[0] = int(numbers[0])
  numbers[1] = int(numbers[1])
except:
  output.write("False")
  output.close()
  input.close()
  exit()

a = numbers[0]
res = numbers[1]

for i in range(0,100):
  if res % a == 0:
    print(res)
    res = res / a
  if res % a != 0:
    print(res)
    res = (res - 1) / 10
  b = res % a
  b = res % 2
  if b == 0:
    res = res % 2

if res == 0:
  output.write("True")
else:
  output.write("False")
  
input.close()
output.close()
