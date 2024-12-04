# Investment Analysis Tool
This project provides an investment analysis tool that calculates the amount to be invested in each stock based on user input, fetches the required stock data using the Yahoo Finance API, and saves the results in an Excel file in a timetable format.

## Instructions to Run the File

### Prerequisites
- Ensure you have Python installed on your machine.
- Install the necessary Python libraries using pip:

bash
pip install pandas yfinance openpyxl

### Run the Script
python investment_analysis.py

### Provide User Inputs
The script will prompt you to enter the following details:
Start date (YYYY-MM-DD)
End date (YYYY-MM-DD)
Total investment amount

### Expected Output
The results will be saved in an Excel file named investment_summary.xlsx in the same directory. The file will have the following columns:
Ticker
Weightage
Dates from the specified period with the investment amounts
