Bank Statement Analysis MVP

This repository contains an MVP (Minimum Viable Product) for parsing and analyzing bank statements. The goal is to help quickly evaluate a business’s financials for a potential loan decision, saving time otherwise spent on manual statement reviews.

Table of Contents
	1.	Overview
	2.	Project Structure
	3.	Setup and Installation
	4.	How It Works
	•	1) Parsing the Statement
	•	2) Analysis Logic
	•	3) Streamlit App
	5.	Understanding the Chart
	6.	Demo Steps
	7.	Known Limitations
	8.	Possible Enhancements
	9.	Appendix: FAQ / Common Issues


Overview

This project simulates a loan-processing scenario where you:
	•	Parse a bank statement (for example, a PDF or JSON).
	•	Analyze the inflows (amount_in), outflows (amount_out), and running balance.
	•	Categorize transactions (e.g., “Food,” “Rent,” “Loan Payment”).
	•	Generate monthly totals for deposits and withdrawals, calculate net flow, and make a simple recommendation on whether to approve a loan.

You’ll see a Streamlit web app that displays:
	•	A Parsed Transactions table (each transaction row)
	•	A bar chart of “Monthly Totals” (deposits vs. withdrawals, plus net flow)
	•	Overall Insights (e.g., total deposits, total withdrawals, net flow, and a basic recommendation)



Project Structure

Your directory might look like this:

my_solution/
├── README.md                # This file
├── requirements.txt         # Python dependencies
├── parse_statements.py      # (Optional) PDF or JSON parsing logic
├── analysis.py              # Core analysis and categorization
├── app.py                   # Streamlit front-end application
└── data/
    └── parsed_statement.json  # Example structured data (fallback)




parse_statements.py
Contains the (currently optional) code for parsing PDFs. In the MVP, we may load transactions directly from a JSON to avoid PDF parsing complexities.
	•	analysis.py
Defines helper functions to categorize transactions, aggregate monthly totals, and produce a loan recommendation.
	•	app.py
A Streamlit script that ties everything together. It loads the transaction data, runs the analysis, and displays the results in a browser‐based UI.
	•	data/parsed_statement.json
A manually created JSON file containing sample transactions. This acts as a fallback so you can demonstrate your analysis without a fully functional PDF parser.




How It Works

1) Parsing the Statement
	•	By default, the code loads an example JSON (parsed_statement.json) from data/.
	•	If you check parse_statements.py, you’ll see (commented) logic that uses pdfplumber or regex to parse a PDF.
	•	For now, we skip that and rely on our JSON for the sake of an MVP—the important part is you still get structured transactions with columns:

date, description, type, amount_in, amount_out, balance



2) Analysis Logic

The analysis is done in analysis.py. It contains:
	1.	categorize_transaction()
A simple, rule‐based function that checks the transaction description for keywords like "UBER", "RENT", "LOAN", etc., and assigns a category (e.g., "Transport", "Loan Payment").
	2.	analyze_transactions(tx_list)
	•	Loads all transactions into a pandas.DataFrame.
	•	Attempts to parse the date into a datetime or monthly period (e.g., 2019-09).
	•	Groups data by month to compute:
	•	Monthly Deposits = sum of amount_in per month
	•	Monthly Withdrawals = sum of amount_out per month
	•	Net Flow = (deposits - withdrawals)
	•	Calculates overall totals for deposits, withdrawals, net flow.
	•	Creates a basic Loan Recommendation based on net flow or a deposit‐to‐withdrawal ratio.

3) Streamlit App

The main user interface is in app.py. It does the following:
	1.	Loads the data from JSON (or PDF if you integrate the parser) into a list of transactions.
	2.	Displays the transactions in a table (using st.dataframe).
	3.	Runs the analysis function from analysis.py.
	4.	Shows a bar chart of monthly totals (deposits vs. withdrawals vs. net flow).
	5.	Summarizes the final recommendation and key metrics (e.g., net flow).


Understanding the Chart

In your screenshot, the chart labeled “Monthly Totals” typically shows deposits (In) and withdrawals (Out) for each month on the y‐axis, grouped or stacked by month on the x‐axis.
	•	X‐axis:
	•	Usually the monthly period (e.g., 2019-09, 2019-10, 2019-11).
	•	Sometimes you’ll see numbers like “596,” “597,” “598.” That’s because pandas internally encodes monthly periods with integer offsets (e.g., 596 might represent 2019-09).
	•	You can rename these for a more friendly label (see “Possible Enhancements” below).
	•	Y‐axis:
	•	The scale of transaction amounts in £ (British Pounds).
	•	Depending on how your code builds the chart, the bars might represent:
	•	Blue section = total monthly deposits (amount_in)
	•	Pink section = total monthly withdrawals (amount_out)
	•	Another color or stacked segment might represent net flow.

If your code is using st.bar_chart directly on a DataFrame with columns [“Monthly Deposits”, “Monthly Withdrawals”, “Net Flow”], each month forms a group on the x‐axis, and the bars on that group show the sum for each column.



Known Limitations
	1.	PDF Parsing is not fully automated in the current MVP. The logic exists in parse_statements.py, but you may need to adjust the regex or coordinate bounding boxes for your specific statement format.
	2.	Rule‐Based Categorization can be inaccurate. Real bank statements have varied descriptions, so a more robust approach (like an NLP model) is needed for large‐scale usage.
	3.	Simple Recommendation: We use a naive net‐flow or deposit‐to‐withdrawals ratio to decide “Recommended” vs. “Not Recommended.” Real loan decisions should consider far more data (credit scores, business type, multiple months of statements, debt‐to‐income ratio, etc.).
	4.	Date Parsing: Some statements only show day/month without a year. We guess a year or parse from the PDF’s statement date range. This can be tricky or incorrect in certain edge cases.


Possible Enhancements
	•	Better Axis Labels for the Monthly Totals chart. Instead of “596 / 597 / 598,” you can rename them to “Sep 2019,” “Oct 2019,” “Nov 2019,” etc.
	•	Multiple Statement Support: Upload multiple JSON/PDF files to combine analyses across multiple months or even multiple years.
	•	Recurring Expense Detection: Identify repeated transactions (like monthly rent) and highlight them in the dashboard.
	•	Machine Learning Classifier: Use an NLP model to categorize transactions (e.g., “Food,” “Transportation,” “Utilities”) more accurately.
	•	Auto‐Parsing: Finalize the PDF ingestion with pdfplumber (or OCR with Tesseract if scanned) so that you don’t need a manual JSON.
	•	Enhanced Loan Scoring: Instead of a binary “Recommended” vs. “Not Recommended,” produce a numeric score or rating based on more sophisticated financial metrics.


