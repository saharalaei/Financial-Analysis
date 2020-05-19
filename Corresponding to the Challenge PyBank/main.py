import csv

# Path of the CSV file:
input_path = "C:/Users/18594/Desktop/python-challenge/Corresponding to the Challenge PyBank/budget_data.csv"

# Path of the output text file
output_path = "C:/Users/18594/Desktop/python-challenge/Corresponding to the Challenge PyBank/PyBank_results.txt"

# Initial values:
net_rows = []
date_rows = []

# Open the csv file and save its data in net_rows and date_rows

with open(input_path) as csv_file:
    csv_reader = csv.reader(csv_file , delimiter = ",")
    csv_header = next(csv_reader)
    for row in csv_reader:
        date_rows.append(row[0])
        net_rows.append(int(row[1]))

# Calculation of the required parameters:

# The total number of months included in the dataset:
month_count = len(date_rows)

# The net total amount of "Profit/Losses" over the entire period:
net_total = sum(net_rows)

# The average of the changes in "Profit/Losses" over the entire period:
average_change = round((net_rows[-1]-net_rows[0])/(month_count-1),2)

# The differnce of net between each two months
diff_net_array = [j - i for i, j in zip(net_rows[: -1], net_rows[1 :])] 

# The greatest increase in profits (date and amount) over the entire period and the date:
greatest_increase = max(diff_net_array)
ind_increase = diff_net_array.index(greatest_increase)+1
date_increase = date_rows[ind_increase]

#The greatest decrease in losses (date and amount) over the entire period and the date:
greatest_decrease= min(diff_net_array)
ind_decrease = diff_net_array.index(greatest_decrease)+ 1
date_decrease = date_rows[ind_decrease]

# Print the results on the terminal:
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {month_count}")
print(f"Total: ${net_total}")
print(f"Average  Change: ${average_change}")
print(f"Greatest Increase in Profits: {date_increase} ${greatest_increase}")
print(f"Greatest Decrease in Profits: {date_decrease} ${greatest_decrease}")


# Print the results on the output text file

with open(output_path,'w') as output:
   output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format("Financial Analysis","----------------------------",f"Total Months: {month_count}",
   f"Total: ${net_total}",f"Average  Change: ${average_change}",f"Greatest Increase in Profits: {date_increase} ${greatest_increase}",
   f"Greatest Decrease in Profits: {date_decrease} ${greatest_decrease}"))
 
    
    
    
