%%according to my internet research,
%%because matlab uses (1+f)*2^e precision,
%%this program has slight inaccuracies with large numbers,
%%works best for simple interpolation
disp("We will be finding your unknown y between two points")

x0 = input("Type your x0: ")
y0 = input("Type your y0: ")
x1 = input("Type your x1: ")
y1 = input("Type your y1: ")
x = input("insert the x value: ")
d = input("How many decimal places do you want: ")

if x1-x0 == 0
    disp("You are dividing by zero")
    
else
y = y0+(x-x0)*(y1-y0)/(x1-x0)
z = round(y,d)
disp("Here is your y: "+z);

end