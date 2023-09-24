def add(x,y):
    sum = x + y
    return str(x) + " + " + str(y) + " = " + str(sum)

def subtract(x,y):
    sum = x - y
    return str(x) + " - " + str(y) + " = " + str(sum)

def multiply(x,y):
    sum = x * y
    return str(x) + " * " + str(y) + " = " + str(sum)

def divide(x,y):
    if y == 0:
        return str(x) + " / " + str(0) + " = " + "NaN"
    else:
        sum = x / y
        return str(x) + " / " + str(y) + " = " + str(sum)

def exponent(x,y):
    sum = x ** y
    return str(x) + "^" + str(y) + " = " + str(sum)

if __name__ == "__main__":
    x = input("enter x: ")
    y = input("enter y: ")
    print(add(int(x),int(y)))
    print(subtract(int(x),int(y)))
    print(multiply(int(x),int(y)))
    print(divide(int(x),int(y)))
    print(exponent(int(x),int(y)))