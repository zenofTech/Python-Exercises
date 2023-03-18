from unicodedata import name

"""\\\\\\\\\\\\\\\\
      welcome note
    \\\\\\\\\\\\\\\\"""

print(
    "\n\t\t",
    " █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█\n\t\t  █░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█\n\t\t  █░░║║║╠─║─║─║║║║║╠─░░█\n\t\t  █░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█\n\t\t  █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n",
)

print("  This is a python mini game, created by Z3N0FTECH hope  you will like it!")

"""\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
      Asking for user choice
    \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\"""

Choice = str(input("  Are you ready to play the game? ")).capitalize()
name = input("What is your name: ").upper()
while Choice == "Yes":
    print(name, " Let's start the game now :)! ")
    score = 0  # incrementing the scores

    """\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
        Asking user for answers to the questions  
        \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\"""

    qustion_answer = input(" What is the meaning of NIC? ")
    if qustion_answer.lower() == "network interface card":
        print(" Correct!")
        score += 1  # incrementing the scores
    else:
        print(" Wrong answer.")
        print("correct answer is: ", "network interface card".capitalize())

    qustion_answer = input(" What is the meaning of CD? ")
    if qustion_answer.lower() == "compact disk":
        print(" Correct!")
        score += 1  # incrementing the scores
    else:
        print(" Wrong answer.")

    qustion_answer = input(" What is the meaning of ROM? ")
    if qustion_answer.lower() == "read only memory":
        print(" Correct!")
        score += 1
    else:
        print(" Wrong answer.")


    qustion_answer = input(" What is the meaning of HTML? ")
    if qustion_answer.lower() == "hypertext markup language":
        print(" Correct!")
        score += 1
    else:
        print(" Wrong answer.")


    qustion_answer = input(" What is the meaning of HTTP? ")
    if qustion_answer.lower() == "hypertext transfer protocol":
        print(" Correct!")
        score += 1
    else:
        print(" Wrong answer.")

    qustion_answer = input(" What is the meaning of SSL? ")
    if qustion_answer.lower() == "secure sockets layer":
        print(" Correct!")
        score += 1
    else:
        print(" Wrong answer.")

    qustion_answer = input(" What is the meaning of TCP? ")
    if qustion_answer.lower() == "transmission control protocol":
        print(" Correct!")
        score += 1
    else:
        print(" Wrong answer.")

    qustion_answer = input(" What is the meaning of IP? ")
    if qustion_answer.lower() == "internet protocol":
        print(" Correct!")
        score += 1
    else:
        print(" Wrong answer.")

    qustion_answer = input(" What is the meaning of SMTP? ")
    if qustion_answer.lower() == "simple mail transfer protocol":
        print(" Correct!")
        score += 1
    else:
        print(" Wrong answer.")

    qustion_answer = input("  What is the meaning of IMAP? ")
    if qustion_answer.lower() == "internet message access protocol":
        print(" Correct!")
        score += 1
    else:
        print(" Wrong answer.")

        """\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
        calcuting scores in number and percentage
        \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\"""

    print("\n  ", name, " You have answer ", score, " questions correctly.")
    print("\n\t****** You got ", (score / 10)*100, "% ******")


    Choice = str(input(" \n Do want to play the game again? ")).capitalize()
else:
    print(name, " Thanks for dropping by :D")
    input(" Click the enter key to exit... ")
    quit()
