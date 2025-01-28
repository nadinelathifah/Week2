password = "1234"
# The correct PIN code is stored as a string in the variable password.

attempt = 1
# Define a variable to store the number of attempts.

# The input function prompts the user to give a password and stores it as a string in the supplied_pin variable
supplied_pin = input("Enter your PIN: ")

# Use a while loop to prompt the user for input while the number of attempts is less than 3
while attempt <4:
    # Using an if statement we check if the supplied pin equals the correct password. If it does then we print a suitable message and break out of the while loop
    if supplied_pin == password:
        print("You can enjoy freedom while it lasts!")
        break
    #If the number of attempts is between 1 and 3 ask the user to try again
    # elif 1<=attempt<3:
    print("Wrong password. Please try again if you don't want to go to jail.")
    print("Attempt # "+str(attempt)+"out of #3")
    #we increment the number of attempts
    attempt += 1
    supplied_pin = input("Enter your PIN: ")
    #If the number of attempts is more than 3 then print a suitable message and exit the while loop
    # else:
    #     print("Police is coming for you!")
    #     # additional comment: "Your account has been locked."
    #     break