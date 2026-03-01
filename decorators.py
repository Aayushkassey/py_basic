from datetime import datetime

def looger(func):
    '''hello 
    '''
    def wrapper(*args, **kwargs):
        print(f"{args[0]}User has called {func.__name__} at {datetime.now()}")
        func(*args, **kwargs)
        print(f"Function call ended at {datetime.now()}")
    return wrapper
    
@looger   
def hello(username):
    print("Hello!", username)

@looger
def goodbye(username):
    print("GoodBye!", username)

@looger
def login(username):
    print("User is trying to login", username)

@looger
def logout(username):
    print("User is trying to logout", username)

hello("aayush")
goodbye("aayush")