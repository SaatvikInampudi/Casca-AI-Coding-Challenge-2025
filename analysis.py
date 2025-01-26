import pandas as pd
import json  # Ensure this is included

def categorize_transaction(description):
    """
    Categorize transactions based on keywords in descriptions.
    """
    desc_upper = description.upper()

    if "UBER" in desc_upper or "LYFT" in desc_upper:
        return "Transport"
    elif "MCDONALDS" in desc_upper or "FOOD" in desc_upper:
        return "Food/Restaurant"
    elif "WESTERN VILLA" in desc_upper or "RENT" in desc_upper:
        return "Rent"
    elif "COOPERATIVE" in desc_upper or "LOAN" in desc_upper:
        return "Loan Payment"
    else:
        return "Other"

def analyze_transactions(tx_list):
    """
    Analyze transaction data and return insights.
    """
    df = pd.DataFrame(tx_list)

    # Categorize transactions
    df['category'] = df['description'].apply(categorize_transaction)

    # Convert date for grouping (dummy year added for parsing)
    df['parsed_date'] = pd.to_datetime(df['date'], format='%d %b%y', errors='coerce')
    df['month'] = df['parsed_date'].dt.to_period('M')

    # Calculate totals
    monthly_in = df.groupby('month')['amount_in'].sum()
    monthly_out = df.groupby('month')['amount_out'].sum()
    net_flow_per_month = monthly_in - monthly_out

    total_in = df['amount_in'].sum()
    total_out = df['amount_out'].sum()
    net_flow = total_in - total_out

    recommendation = "Recommended for Loan" if total_in > total_out * 1.5 else "Not Recommended"

    return {
        'df': df,
        'monthly_in': monthly_in,
        'monthly_out': monthly_out,
        'net_flow_per_month': net_flow_per_month,
        'total_in': total_in,
        'total_out': total_out,
        'net_flow': net_flow,
        'recommendation': recommendation
    }

# Add a test section
if __name__ == "__main__":
    # Load the manually created JSON
    with open("data/parsed_statement.json", "r") as file:
        transactions = json.load(file)

    # Perform analysis
    results = analyze_transactions(transactions)

    # Print results for validation
    print("Overall Insights:")
    print(f"Total Deposits: £{results['total_in']:.2f}")
    print(f"Total Withdrawals: £{results['total_out']:.2f}")
    print(f"Net Flow: £{results['net_flow']:.2f}")
    print(f"Loan Recommendation: {results['recommendation']}")