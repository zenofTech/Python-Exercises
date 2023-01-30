# This print function is to print the coder
print("\n","\t"*4,"Created","\n","\t"*3,"\\"*25, "\n","\t"*4,"   By","\n","\t"*4,"Zenoftech\n", "\t"*3,"\\"*25)


print('\nThis program accept two numbers and give the sum of their squares.')

#This lines will prompt the user to enter numbers.
num1 = int(input("Enter a number: "))
num2 = int(input("Enter second number: "))

#Here we get the square of the numbers the user entered.
num1Sq = num1*num1
num2Sq = num2*num2

#The sum variable below add the square of the numbers
sum = num1Sq + num2Sq

#Then we print the result here.
print("\tThe squares of the sum is: ", sum)
input("\nPress the any key to exit...")

#This make a sound when the user click on any key to quit the program.)
print("\a")
