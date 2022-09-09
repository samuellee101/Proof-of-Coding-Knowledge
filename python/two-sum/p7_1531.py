#Samuel Lee ID: 20412795

input_file = open("p7_input.txt", "r")
output_file = open("p7_1531_output.txt", "a+")

a = input_file.readline()
b = int(input_file.readline())

num_list = a.split()

for i in range(0, len(num_list)):
    num_list[i] = int(num_list[i])

for first in range(0, len(num_list)-2):
    for second in range(1, len(num_list)-1):
        if num_list[first] + num_list[second] == b:
            output_file.write(str(first))
            output_file.write(" ")
            output_file.write(str(second))
            output_file.write("\n") #in case there is more than one pair

output_file.close()