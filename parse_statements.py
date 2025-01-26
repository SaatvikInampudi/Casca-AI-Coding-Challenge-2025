# import pdfplumber
# import re


# def parse_statement(pdf_path):
#     """
#     Parse a bank statement PDF and return structured transaction data.
#     """
#     transactions = []
#     multiline_buffer = ""

#     with pdfplumber.open(pdf_path) as pdf:
#         for page in pdf.pages:
#             text = page.extract_text()
#             if not text:
#                 continue

#             # Split the text into lines
#             lines = text.split('\n')

#             for line in lines:
#                 # Clean the line
#                 line = line.strip()

#                 # Skip non-transactional or irrelevant lines
#                 if is_footer_or_irrelevant(line):
#                     continue

#                 # Check if the line starts with a date
#                 if re.match(r"^\d{2}\s\w{3}\d{2}", line):
#                     # Process the previous buffered transaction
#                     if multiline_buffer:
#                         process_transaction_line(multiline_buffer, transactions)
#                         multiline_buffer = ""

#                     # Start a new transaction line
#                     multiline_buffer = line
#                 else:
#                     # Append to the buffer if it doesn't start with a date
#                     multiline_buffer += " " + line

#             # Process any remaining buffered transaction
#             if multiline_buffer:
#                 process_transaction_line(multiline_buffer, transactions)

#     return transactions


# def is_footer_or_irrelevant(line):
#     """
#     Check if a line is part of the footer or irrelevant (e.g., URLs, page numbers).
#     """
#     if "https://" in line or "Lloyds Bank" in line or "Page" in line:
#         return True
#     return False


# def process_transaction_line(line, transactions):
#     """
#     Process a single transaction line and append to transactions list.
#     """
#     # Regex to match transaction details
#     pattern = re.compile(
#         r"^(\d{2}\s\w{3}\d{2})\s+(.+?)\s+(CPT|DEB|TFR|DD|CSH|FPI)\s+([\d\.]*)\s*([\d\.]*)\s+([\d\.]+)$"
#     )
#     match = pattern.match(line)

#     if match:
#         date = match.group(1)
#         description = match.group(2).strip()
#         tx_type = match.group(3)

#         # Clean numeric fields
#         def clean_amount(value):
#             if value:
#                 try:
#                     return float(value.rstrip('.'))  # Remove trailing dots and convert to float
#                 except ValueError:
#                     return 0.0
#             return 0.0

#         amount_in = clean_amount(match.group(4))
#         amount_out = clean_amount(match.group(5))
#         balance = clean_amount(match.group(6))

#         transactions.append({
#             "date": date,
#             "description": description,
#             "type": tx_type,
#             "amount_in": amount_in,
#             "amount_out": amount_out,
#             "balance": balance
#         })
#     else:
#         # Log skipped lines for debugging
#         print(f"Skipped line: {line}")


import json

def parse_statement(file_path):
    """
    Simulate parsing by loading pre-defined parsed data from a JSON file.
    """
    with open(file_path, "r") as file:
        data = json.load(file)
    return data