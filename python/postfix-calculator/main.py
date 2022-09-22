# Samuel Lee ID: 20412795

arr = input("Please type in your string: ")
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
        print(arr[index] , " has been appended")
    #perform operation if operator is found
    else:
        if arr[index] == '+':
            a = q.pop()
            print(a , " has been popped")
            b = q.pop()
            print(b , " has been popped")
            c = a + b
            print(c , " has been appended")
            q.append(c)
        if arr[index] == '-':
            a = q.pop()
            print(a , " has been popped")
            b = q.pop()
            print(b , " has been popped")
            c = b - a
            print(c , " has been appended")
            q.append(c)
        if arr[index] == '/':
            a = q.pop()
            print(a , " has been popped")
            b = q.pop()
            print(b , " has been popped")
            c = b / a
            print(c , " has been appended")
            q.append(c)
        if arr[index] == '*':
            a = q.pop()
            print(a , " has been popped")
            b = q.pop()
            print(b , " has been popped")
            c = a * b
            print(c , " has been appended")
            q.append(c)


print("This was your input list: " , arr)
print("This is what the queue currently looks like: " , q)