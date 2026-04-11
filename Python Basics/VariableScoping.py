# To know about the variable scoping with use of the functions
# Local -> Enclosing -> Global -> Builtin
from dis import disco


# Local :
def order() :
    food="Briyani"
    print("The order is " + food)
order()
print(food) #gives an error because the food variable is accessed within the function order

# Enclosing :
def cart():
    discount=20 # this is called as the enclosing variable
    def checkout():
        print("The cart is " , discount)
    checkout() #call checkout function
cart()# call cart function

# Global :
user_id = "Krishai25" #Global Variable can be used by the functions at any time without issues
def homepage():
    print("Welcome from homepage : " , user_id)
def profile():
    print("Welcome from profile: " , user_id)
homepage()
profile()

# Builtin :
print(__file__) #Prints the file path
print(__doc__)
