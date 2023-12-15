# Import necessary libraries
import os
import csv

# Initialize variables for the analysis
last_profit_loss = None  # Stores the profit/loss of the previous month
total_change = 0  # Total change in profit/loss
Number_ofMonths = 0  # Total number of months in the dataset
net_total = 0  # Net total amount of profit/losses
greatest_increase = {"date": "", "amount": 0}  # Record of the greatest increase in profits
greatest_decrease = {"date": "", "amount": 0}  # Record of the greatest decrease in profits

# Open and read the budget data file
with open('budget_data.csv', "r", newline='') as file:
    Reader = csv.reader(file)
    next(Reader, None)  # Skip the header row

    # Iterate over each row in the CSV file
    for row in Reader:
        date = row[0]
        Number_ofMonths += 1  # Count the month
        value_of_Coloumn_2 = int(row[1])  # Convert profit/loss value to integer
        net_total += value_of_Coloumn_2  # Accumulate the net total

        # Calculate the monthly change in profit/loss
        if last_profit_loss is not None:
            change_in_profit_loss = value_of_Coloumn_2 - last_profit_loss
            total_change += change_in_profit_loss

            # Check for greatest increase in profit
            if change_in_profit_loss > greatest_increase["amount"]:
                greatest_increase["date"] = date
                greatest_increase["amount"] = change_in_profit_loss
            
            # Check for greatest decrease in profit
            elif change_in_profit_loss < greatest_decrease["amount"]:
                greatest_decrease["date"] = date
                greatest_decrease["amount"] = change_in_profit_loss
        
        # Update last profit/loss for the next iteration
        last_profit_loss = value_of_Coloumn_2
            
# Calculate average change in profit/loss
average_change = total_change / (Number_ofMonths-1)

# Set the output file name
output_file = "financial_analysis.txt"

# Write the analysis to a text file and print it to the console
with open(output_file, "w") as text_output:
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {Number_ofMonths}")
    print(f"Total: ${net_total}")
    print(f"Average Change: ${average_change:.2f}")
    print(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})")
    print(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})")
