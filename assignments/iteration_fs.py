def show_numbers():
    limit = int(input("Enter the limit: "))
    j = 0
    for i in range(limit):
        if i % 2 == 0:
            print(i, " - even ")
        else:
            print(i, "- odd ")

    while j <= limit:
        if j % 2 == 0:
            print(j, " - even ")
        else:
            print(j, "- odd ")
        j += 1


def validate_number(num):
    try:
        num = float(num)
        return num
    except ValueError:
        print("Only numbers and decimals allowed")
        financial_statement()

def round_num(num):
    return round(num, 2)
    
def financial_statement():
    percentage_tracker = 100
    percentage_marketing = 0
    percentage_operational_expenses = 0

    print("Please enter the amount given for the project")
    income = validate_number(input("Enter your amount given: "))
    if income == 0:
        print("You have no income")
        exit()

    percentage_marketing = validate_number(input("(%) marketing: "))
    if percentage_marketing > percentage_tracker:
        print("Percentage allocated for marketing should be less than or equal to " + str(percentage_tracker))
        financial_statement()
    
    percentage_tracker -= percentage_marketing

    if percentage_tracker > 0:
        percentage_operational_expenses = validate_number(input("(%) operational expenses: "))

    cost_per_customer = float(input("(ghs) What does it cost to acquire a customer: "))

    marketing = income * (percentage_marketing / 100)
    operational_expenses = income * (percentage_operational_expenses / 100)
    customer_acquisition = income - (marketing + operational_expenses)
    
    customers_aquisition_count = customer_acquisition / cost_per_customer

    print("____FINANCIAL STATEMENT____ \n\n")

    print(f"Marketing budget: {round_num(marketing)} \n\n Operational expenses: {round_num(operational_expenses)} \n\n Customer acquisition: {round_num(customer_acquisition)} \n\n Number of customers to acquire: {round_num(customers_aquisition_count)}")

def main():
    user = input("""Choose an operation:
    1. Show financial statement
    2. Show even and odd numbers
    """)

    if user == "1":
        financial_statement()
    elif user == "2":
        show_numbers();
    else:
        print("Invalid operation")
        exit()

main()
