# This print function is to print the coder
print("\n","\t"*4,"Created","\n","\t"*3,"\\"*25, "\n","\t"*4,"      By","\n","\t"*4,"Zenoftech\n", "\t"*3,"\\"*25)

print("\nThis program will calculate will reads in three numbers and writes them all in sorted order\n")


num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))

#Setting variable to accept input from users
    #Testing the conditions.
if (num1<num2 and num2<num3):
    print("\tNumbers in order are: ", num1, num2, num3)
elif (num1 > num2 and num2 > num3):
    print("\tNumbers in order are: ", num3, num2, num1)

elif (num1 < num2 and num2 > num3):
    print("\tNumbers in order are: ", num1, num3, num2)

elif (num1 < num2 and num3 < num1):
    print("\tNumbers in order are: ", num3, num1, num2)

elif (num1 < num3 and num2 < num1):
    print("\tNumbers in order are: ", num2, num1, num3)
    
elif (num1 > num2 and num2 < num3):
    print("\tNumbers in order are: ", num2, num3, num1)
        
else :
      print("\nWe are sorry, an error as occur :(\nPlease report the error to amuktar064@gmail.com\nWe appreciate your kindness.")
        
