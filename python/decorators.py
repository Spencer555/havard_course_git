# decorators take a function as input and returns a modified version of it 

def announce(f):
    def wrapper():
        print('About to run a function')
        f()
        print("Done with the function")
        
    return wrapper



# add a decorator
@announce
def hello():
    print("hello world")
    
    
hello()