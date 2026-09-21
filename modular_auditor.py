#Global Contants
MAX_CAPACITY = 500
TAX_RATE = 0.1 # 10% tax rate

#local variables
user_input = 0
current_total = 0
error_count = 0
tax_result = 0

#Functions
def get_valid_input():
    user_input = input("Enter stock quantity or 'quit' to exit.\n")

    if user_input.lower() == "quit":
       return (user_input)

    if user_input.isdigit():
        return int(user_input)
    else:
        return None
        
def error_validation():
    print("Please input positive whole numbers only!")

def process_delivery(new_total, user_input):
    new_total += user_input
    print("Current Inventory Count Is:" ,new_total)
    return new_total
    
def calculate_tax(amount):
    tax = amount * TAX_RATE
    return tax

def generate_report(total_units, error_count):
    print(f"Total Units Processed: {total_units}\nNumber of Failed Entries: {error_count} ")


while True:

    user_input = get_valid_input()

    if user_input == "quit":
       break

    elif user_input is None:
        error_validation()
        error_count += 1
    
    else:
        current_total = process_delivery(current_total, user_input)
        tax_result = calculate_tax(user_input)

    if current_total > MAX_CAPACITY:
        print ("You have exceeded 500 units!")
        break

generate_report (current_total, error_count)
print(f"The tax is ${tax_result}")

    
