import pandas as pd
import yfinance as yf

# Load the CSV file
stocks_df = pd.read_csv('stocks.csv')

# Accept inputs from the user
start_date = input("Enter the start date (YYYY-MM-DD): ")
end_date = input("Enter the end date (YYYY-MM-DD): ")
investment_amount = float(input("Enter the investment amount: "))

# Function to fetch stock data
def fetch_stock_data(ticker, start, end):
    stock_data = yf.download(ticker, start=start, end=end)
    return stock_data

# Initialize a dictionary to store results
results = {"Ticker": [], "Weightage": []}
date_range = pd.date_range(start=start_date, end=end_date)

for date in date_range:
    results[date.strftime("%Y-%m-%d")] = []

# Process each stock in the CSV
for index, row in stocks_df.iterrows():
    ticker = row['Ticker']
    weightage = row['Weightage']

    # Fetch stock data
    stock_data = fetch_stock_data(ticker + ".NS", start_date, end_date)

    # Calculate investment amount for this stock
    investment = investment_amount * weightage

    # Store ticker and weightage in the results
    results["Ticker"].append(ticker)
    results["Weightage"].append(weightage)

    # Store the investment amount for each date
    for date in date_range:
        date_str = date.strftime("%Y-%m-%d")
        if date_str in stock_data.index:
            results[date_str].append(investment)
        else:
            results[date_str].append(0)

# Create a DataFrame for the results
results_df = pd.DataFrame(results)

# Save the results to an Excel file
results_df.to_excel('investment_summary.xlsx', index=False)

print("Task completed! The data has been written to 'investment_summary.xlsx'.")
