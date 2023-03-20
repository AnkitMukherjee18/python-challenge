# Import budget_data.csv
import csv
import os

# Set path for file 
file_path = r'C:\Users\bayek\OneDrive\Documents\GitHub\python-challenge\PyBank\Resources\budget_data.csv'

# Define function to read the CSV file and return two lists
def read_csv_file(file_path):
    dates = []
    profit_losses = []
    with open(file_path, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)  # skip header row
        for row in csvreader:
            dates.append(row[0])
            profit_losses.append(int(row[1]))
    return dates, profit_losses

# Call the function to get the lists of dates and profit/loss values
file_path = os.path.join('.', 'budget_data.csv')
dates, profit_losses = read_csv_file(file_path)

# Calculate the total number of months in the dataset
total_months = len(dates)

# Calculate the net total amount of profit/losses over the entire period
net_profit_losses = sum(profit_losses)

# Create a new list of changes in profit/loss values over the entire period
changes = [profit_losses[i] - profit_losses[i-1] for i in range(1, len(profit_losses))]

# Calculate the average of the changes in profit/loss values over the entire period
average_change = sum(changes) / len(changes)

# Find the greatest increase and decrease in profits, along with their corresponding dates
max_increase = max(changes)
max_decrease = min(changes)
max_increase_date = dates[changes.index(max_increase) + 1]
max_decrease_date = dates[changes.index(max_decrease) + 1]

# Print out the financial analysis results
print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_profit_losses}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {max_increase_date} (${max_increase})")
print(f"Greatest Decrease in Profits: {max_decrease_date} (${max_decrease})")
