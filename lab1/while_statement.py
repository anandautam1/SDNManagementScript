secret_number = 5;
flag = True;

while flag:
    print("Guess the number inside the prorgam");
    #raw_input is for string 
    #input is for number 
    var = input("Enter the number: ");
    print("You entered " + str(var));
    if var == secret_number:
        flag = False;

print("Congratulations the secret number is %.3f" %secret_number);