import math

choice = input("\nDo you want to evaluate a quadratic equation: ").lower()
while choice =="yes":    
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    c = int(input("Enter the value of c: "))
    x = b * b - 4 * a * c

    if x < 0:
            print("Imaginary root")
            print("\nDo you want to evaluate another quadratic equation: \n").lower()
        
    else:
        root1 = (-b + math.sqrt(x)) / (2.0 * a)
        root2 = (-b - math.sqrt(x)) / (2.0 * a)
        print("x  = ", root1, "\t x  = ", root2)
        choice = input("\nDo you want to evaluate another a quadratic equation: ").lower()
else:
    print("Thank your for stopping by :D")
