#create variable stock quantity and set to zero
stock_quantity = 0
error_count = 0

#Requesting user to input stock quantity until user types quit
while True:
    user_input = input("Enter stock quantity or 'quit' to exit.\n")


    if user_input.lower() == "quit":
     print("The total Units Processed is {} and number of Failed/Rejected Entries is {} \n".format(stock_quantity, error_count) )
     break

    if user_input.isdigit():
        stock_quantity += int(user_input)
        print("Current inventory count is:",int(stock_quantity))

        if int(user_input) > 500: 
             print("Alert! Total inventory has exceeded 500units!")
             break 
        
    else:
        print("Error! Please input positive whole numbers only!\n")
        error_count += 1


    







  










    
            


