x = 50

def func(x):
    print('x is',x)
    x = 2
    print('Changed local x to',x)

if __name__ == '__main__':
    func(x)
    print('x is still',x)

# the final value of x is still 50 
# this is the case because the passed x will be changed by the program
# it creates a copy of the passed variable thus the namespace stays explicit inside the function