#Samuel Lee, ID: 20412795

file = open("input.txt", "r")
a = file.readlines()
for line in range(0, len(a)):
    #a[line].pop[len(current_line) - 1]
    current_line = a[line]
    #b = current_line
    current_line = current_line[::-1]
    output_file = open("1531_p2_output.txt", "a")
    output_file.write(current_line)
    output_file.write("\n")
    output_file.close()
    #print(b)

#discuss code block with professor
with open("1531_p2_output.txt", 'r+') as temp:
    lines = temp.readlines()
    #look at beginning of file
    temp.seek(0)
    #.strip removes spaces before and after
    temp.writelines(line for line in lines if line.strip())
    temp.truncate()


#with open("input.txt", "r") as file:
    #a = list(open("input.txt").read())
    #beg: int = 0
    #end: int = len(a)-1
    #middle: int = len(a)/2
    #while beg < end:
    #    temp1: str = a[beg]
    #    temp2: str = a[end]
    #    a[beg] = temp2
    #    a[end] = temp1
    #    beg = beg + 1
    #    end = end - 1
    #a = ''.join(a)
    #output_file = open("1234.txt", "a")
    #output_file.write(a + "\n")
    #output_file.close()