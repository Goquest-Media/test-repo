from datetime import datetime
import time
def get_time_loop(): 
    for _ in range(5):
        print(datetime.now())
        time.sleep(2)
#time delay set to 2

def get_double(num):
    return num*2

def hello(name):
    return (f"Hello {name}")

print(get_double(4))
print(get_double(get_double(4)))
print(hello('vrushab'))
