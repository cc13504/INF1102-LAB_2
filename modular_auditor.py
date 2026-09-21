#Create Stock Quantity and Error Count
stock_quantity = 0
user_input = 0

#Functions

def get_valid_input():
    user_input = input("Enter stock quantity or 'quit' to exit.\n")

    if user_input.lower() == "quit":
        print("The total Units Processed is {} and number of Failed/Rejected Entries is {}. \n".format(stock_quantity, error_count) )

    if user_input.isdigit():
        process_delivery(user_input)
    
    else:
        print("Error! Please input positive whole numbers only!\n")


def process_delivery(user_input):
    current_total = int(user_input)
    new_value = current_total + int(user_input)

    print(new_value)
    
def calculate_tax(amount):
    return()

def generate_report(stock_quantity, error_count):
    return ()

#Requesting user to input stock quantity until user types quit
#Create Stock Quantity and Error Count

#Requesting user to input stock quantity until user types quit
while True:
    
    get_valid_input()

    
    


    







  










    
            


