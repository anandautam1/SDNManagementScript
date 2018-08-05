import math

if math.sin(1): x=1; print ('sin(%g)=%g' % (x, math.sin(x)))

secret_number = 5;
flag = True;

while flag:
    sequence = [1,2,3,4,5,6];
    for x in range(0,len(sequence)):
        print("Guess the number inside the prorgam");
        #raw_input is for string 
        #input is for number 
        var = sequence[x]
        print("You entered " + str(var));
        if var == secret_number:
            flag = False;
        #if the number cannot be found to be matched to the secret number then it will run forever
        #Luckily there is a matched number within the sequence                                                                                                                                        
                            