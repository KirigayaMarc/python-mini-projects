print("Welcome! This is a simple tip calculator that asks for your total bill costs and what percent of that you would like to give as a tip. It could come in handy if you like tipping! Enjoy.")

#Inputs for the calculator
total_bill = float(input("What is the total cost of your bill? $"))
tip_percentage = int(input("What percentage would you like to give as a tip? %"))

#Simple Math to get the amount.
tip_amount = total_bill * tip_percentage / 100

# Final Costs
final_bill = total_bill + tip_amount
print(f"The Tip amount will be: ${tip_amount:.2f} | Your Final Bill will be: ${final_bill:.2f}. Thank you for using this simple tip calculator!")




