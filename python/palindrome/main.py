#Samuel Lee, ID: 20412795
#a: str = input("Insert string: \n")
import re
file = open("input.txt", "r")
a = file.readlines()
for line in range(0, len(a)):
    current_line = ''.join(a[line])
    palindrome = current_line[::-1]
    palindrome = re.sub(r'\W+', '', palindrome)
    palindrome = palindrome.lower()
    comparison = re.sub(r'\W+', '', current_line)
    comparison = comparison.lower()
    #print(palindrome)
    #print(comparison)
    output = ""
    if palindrome == comparison:
        output = "True"
    else:
        output = "False"
    print(output)
    output_file = open("1531_p1_output.txt", "a")
    output_file.write(output)
    output_file.write("\n")
    output_file.close()
    #print(b)

#discuss code block with professor
with open("1531_p1_output.txt", 'r+') as temp:
    lines = temp.readlines()
    #look at beginning of file
    temp.seek(0)
    #.strip removes spaces before and after
    temp.writelines(line for line in lines if line.strip())
    temp.truncate()