# This print function is to print the coder
print("\n","\t"*4,"Created","\n","\t"*3,"\\"*25, "\n","\t"*4,"   By","\n","\t"*4,"Zenoftech\n", "\t"*3,"\\"*25)

print("\nThis program will calculate will the sum of running numbers, when a negative number is encountered, it will stop adding numbers and write out the final result \n")

#Initializing sum
sum =0
i = 0
while i >=0:
	i = int(input("Enter a number: "))
	sum +=i
print(sum)
