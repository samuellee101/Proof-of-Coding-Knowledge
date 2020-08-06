# simple mean calculator
d = 'd'

b = 0

c = 0

print('Please input number, or type d if you are done')

a = input()

while a != d:
    b = int(a) + b
    c = c+1
    print('Please input number, or type d if you are done')
    a=input()

if a == d:
    print(b/c)
    break
