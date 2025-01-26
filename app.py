import streamlit as st
import pandas as pd
import json
from analysis import analyze_transactions

def load_data():
    """
    Load parsed transaction data from JSON.
    """
    with open("data/parsed_statement.json", "r") as file:
        return json.load(file)

def main():
    st.title("Bank Statement Analysis MVP")

    # Load parsed transactions
    st.subheader("Parsed Transactions")
    transactions = load_data()
    df = pd.DataFrame(transactions)
    st.dataframe(df)

    # Analyze transactions
    results = analyze_transactions(transactions)

    st.subheader("Monthly Totals")
    # Create DataFrame for visualization
    monthly_df = pd.DataFrame({
        "Monthly Deposits": results['monthly_in'],
        "Monthly Withdrawals": results['monthly_out'],
        "Net Flow": results['net_flow_per_month']
    })
    st.bar_chart(monthly_df)  # Pass the DataFrame directly

    st.subheader("Overall Insights")
    st.metric(label="Total Deposits", value=f"£{results['total_in']:.2f}")
    st.metric(label="Total Withdrawals", value=f"£{results['total_out']:.2f}")
    st.metric(label="Net Flow", value=f"£{results['net_flow']:.2f}")
    st.write(f"**Loan Recommendation:** {results['recommendation']}")

if __name__ == "__main__":
    main()