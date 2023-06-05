#This program is for calculating investment returns or home loan repayments
#for example, use in a small financial company.

import math

#Prints descriptions of the two choices, then asks user to enter which one they want to use.
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calculate the amount you'll have to pay on a home loan")
investment_or_bond = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")


#Check if the user has chosen "investment" by converting their input to all lower case.
if investment_or_bond.lower() == "investment":

    #Asks the user to input their numbers (put straight into floats or integers) ready for the calculations:
    print("You have chosen investment. Please note ONLY NUMBERS should be entered below; do NOT enter symbols like % or £.")
    deposit = float(input("Enter the amount of money you are depositing: "))
    interest_rate = float(input("Enter the interest rate: "))/100
    years = int(input("Enter the number of years you plan on investing: "))

    #Next part placed into a while loop to ensure user doesn't have to start from scratch if they enter an invalid input.
    while True:  
        interest_type = input("Enter either 'simple' or 'compound' interest: ")    
        #Simple interest choice and calculations:
        if interest_type.lower() == "simple":                                       
            amount = deposit * (1 + interest_rate*years)                            
            print(f"Your total amount with simple interest will be {amount: 0.2f}")
            print("Thank you for using this program. Please restart it if you need to perform another calculation.")
            break
        #Compound interest choice and calculations:
        elif interest_type.lower() == "compound":                                   
            amount = deposit * math.pow((1+interest_rate),years)                   
            print(f"Your total amount with compound interest will be {amount: 0.2f}")
            print("Thank you for using this program. Please restart it if you need to perform another calculation.")
            break
         #If a choice is not chosen correctly, loop back to the start to ask them again.
        else:
            print("Input not understood. Please try again.")
            continue
   
#If the user hasn't chosen "investment", check if they've chosen "bond":
elif investment_or_bond.lower() == "bond":
    print("You have chosen bond. Please note ONLY NUMBERS should be entered below; do NOT enter symbols like % or £.")
    house_value = float(input("Enter the present value of the house: "))
    interest_rate = float(input("Enter the interest rate: "))/100
    months = int(input("Enter the number of months you plan to take to repay the bond: "))
    
    #Calculate the repayment amount based on the user's input then print it to 2 decimal places.
    repayment = (interest_rate/12 * house_value) / (1 - (1 + interest_rate/12)**(-months))
    print(f"Your monthly repayment will be {repayment: 0.2f}")
    print("Thank you for using this program. Please restart it if you need to perform another calculation.")

#If neither bond or investment options are inputted, tell the user to restart the program:
else:
    print("Input not recognised. Please restart the program.")
