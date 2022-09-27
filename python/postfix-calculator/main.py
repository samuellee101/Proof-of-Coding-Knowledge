# Samuel Lee ID: 20412795

arr = input("Please type in your string: ")

print("Postfix Problem: " + arr)

arr = arr.split(" ")

q = []

for index in range(0, len(arr)):
    #check and see if index is not operator
    if arr[index] != '+' and arr[index] != '-' and arr[index] != '/' and arr[index] != '*':
        #error if a string is input that isn't an operator or a number
        try:
            float(arr[index])
        except ValueError:
            print(arr[index], " Not a float or a operator")
            break
        arr[index] = float(arr[index])
        q.append(arr[index])
        print("pushed ", arr[index])
    #perform operation if operator is found
    else:
        if len(q) <= 1:
            print("Error: not enough numbers to perform operation")
            break
        if arr[index] == '+':
            a = q.pop()
            b = q.pop()
            print("popped ", a, " ", b, " ", "+")
            c = a + b
            print("pushed ", c)
            q.append(c)
        if arr[index] == '-':
            a = q.pop()
            b = q.pop()
            print("popped ", a, " ", b, " ", "-")
            c = b - a
            print("pushed ", c)
            q.append(c)
        if arr[index] == '/':
            a = q.pop()
            b = q.pop()
            print("popped ", a, " ", b, " ", "/")
            c = b / a
            print("pushed ", c)
            q.append(c)
        if arr[index] == '*':
            a = q.pop()
            b = q.pop()
            print("popped ", a, " ", b, " ", "*")
            c = a * b
            print("pushed ", c)
            q.append(c)

print("The result of this operation is->", q[len(q)-1])
