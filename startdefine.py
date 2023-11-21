#creating a python function

def my_function():
    print("Creating new function")
    
my_function()
    
def my_function(fname):
    print(fname + " Nasif")
    
my_function("Azraf")

def my_function(child1, child2, child3):
    print("The youngest child is " + child3)
    
my_function(child1="Azraf", child2="Nameer", child3="Nasif")


#returning value 
def my_function(x):
    return 5 * x 
print(my_function(3))

