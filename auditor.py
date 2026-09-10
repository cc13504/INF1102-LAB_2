#create variable stock quantity and set to zero
stock_quantity = 0

#Requesting user to input stock quantity until user types quit
while True:
    user_input = input("Enter stock quantity.\n")

    if user_input == "quit":  
        break

    #Handle invalid input
    if user_input.isdigit():
        stock_quantity += int(user_input)
        print("Current inventory count is:",stock_quantity)
    else:
        print("Error! Please input whole numbers!\n")



