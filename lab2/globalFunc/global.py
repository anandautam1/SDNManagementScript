x = 50

def func():
    global x
    print('x is', x)
    x = 2
    print('Changed global x to', x)

if __name__ == '__main__':
    func()
    print('Value of x is', x)

# the final value of variable x in the program is 2 
# this time the declaration of x is outside of the main thus it will be declared globaly inside the program
# python allows the function to access global variable thus enabling the function to modify the global variable