from parse_statements import parse_statement

# Path to the statement PDF
pdf_path = "data/statement2.pdf"

# Parse the statement
transactions = parse_statement(pdf_path)

# Print the extracted transactions
for transaction in transactions:
    print(transaction)