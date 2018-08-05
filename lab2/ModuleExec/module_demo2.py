from mymodule import say_hi, __version__

if __name__ == '__main__':
    say_hi()
    print('Version', __version__)

#from this use case the name space from the mdoule will be occupied to the main 
# this allows main to call the function directly with a cost of occupying a particular namespace
# depends on the team this can be convinience or a disadvantage