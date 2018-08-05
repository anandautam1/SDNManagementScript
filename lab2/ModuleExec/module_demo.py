import mymodule

if __name__ == '__main__':
    mymodule.say_hi()
    print('Version', mymodule.__version__)

#role of import keyword in this case is the fact that the module is bind to the module name
# thus namespace of the mymodule will be associated to the imported module and 
# the way to access the method inside the module is to call it in a very OOP 
# fashion using the dot operator

#need to have a proper look at import 
