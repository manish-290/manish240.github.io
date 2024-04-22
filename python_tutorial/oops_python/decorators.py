#decorators are the terms that accepts the functions as the 
#parameters and modified it to the something special

def announce(f):
    def wrapper():
        print("Ready to lauch the function.....")
        f()
        print("Completed the function execution....")
    return wrapper

#announce passed the hello function in parameter to the announce
#method
@announce
def hello():
    print("Hello world")


hello()