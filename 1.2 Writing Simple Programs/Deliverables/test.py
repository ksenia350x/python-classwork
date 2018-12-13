def main():
    # Desc of program
    print("This program calculates the future value")
    print("of an yearly investment.")
    # User input: years of the investment
    years = eval(input("Enter the amount of years: "))
    # User input: initial amount of money
    principal = eval(input("Enter the initial principal: "))
    # User input: yearly interest rate
    rate = eval(input("Enter the yearly interest rate: "))
    # User input: compounded interest
    periods = eval(input("How many times is the interest compounded each year? "))
    # Loop the calculation according to the amount of years it lasts
    for i in range (years * periods) :
	# Calculation
        principal = principal * (1 + rate / periods)
    # Print conclusion
    print("The value in",years,"years is: ", principal)

main()
