#Samuel Lee ID: 20412795

inputfile = open("t3_input.txt", "r")
outputfile = open("t3_1531_output.txt" , "w")

name = inputfile.readline().split()

for i in range(0,len(name)):
  temp = name[i]
  first = temp[0:1]
  first = first.upper()
  print(first)
  temp = first + temp[1:100]
  outputfile.write(temp + " ")


inputfile.close()
outputfile.close()