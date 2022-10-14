#Goals
#Print 1 to 100
#If i % 3 or i % 5 print, fizz, buzz, or fizzbuzz
x = "Fizz"
y = "Buzz"
for i in range (1, 101):

    if i % 3 == 0 & i % 5 == 0:
        #if divis by 5 or 3
        print(x + y)
    elif i % 3 == 0:
        #if divis by 3
        print(x)
    elif i % 5 == 0:
        #if divis by 5
        print(y)
    else:
        #prints all other cases
        print(i)
    
