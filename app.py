import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Function to display the raw data table
def show_raw_data(data):
    st.dataframe(data)

# Function to display the pie chart
def show_pie_chart(data):
    category_amounts = data.groupby('Category')['Amount'].sum()
    fig, ax = plt.subplots()
    ax.pie(category_amounts, labels=category_amounts.index, autopct='%1.1f%%')
    ax.set_aspect('equal')
    st.pyplot(fig)

# Main function
def main():
    # Create an empty DataFrame to store the data
    data = pd.DataFrame(columns=['Name', 'Date', 'Debit/Credit', 'Amount', 'Category', 'Relationship_Flag'])

    # Create the main page
    st.title("Financial Tracking App")

    # Button to open the raw data sheet
    if st.button("All Expenses"):
        show_raw_data(data)

    # Slicer for filters
    selected_name = st.selectbox("Select Name", ["All"] + data["Name"].unique().tolist())
    selected_relationship_flag = st.selectbox("Select Relationship Flag", ["All"] + data["Relationship_Flag"].unique().tolist())

    # Apply filters
    filtered_data = data.copy()
    if selected_name != "All":
        filtered_data = filtered_data[filtered_data["Name"] == selected_name]
    if selected_relationship_flag != "All":
        filtered_data = filtered_data[filtered_data["Relationship_Flag"] == selected_relationship_flag]

    # Show the filtered data table
    st.subheader("Filtered Data")
    st.dataframe(filtered_data)

    # Show the pie chart
    st.subheader("Expense Distribution by Category")
    show_pie_chart(filtered_data)

    # Form to add new data point
    st.subheader("Add New Data Point")
    name = st.text_input("Name")
    date = st.date_input("Date")
    debit_credit = st.selectbox("Debit/Credit", ["Debit", "Credit"])
    amount = st.number_input("Amount")
    category = st.text_input("Category")
    relationship_flag = st.text_input("Relationship Flag")

    if st.button("Add"):
        data = data.append({
            'Name': name,
            'Date': date,
            'Debit/Credit': debit_credit,
            'Amount': amount,
            'Category': category,
            'Relationship_Flag': relationship_flag
        }, ignore_index=True)

    # Save the edited data
    data.to_excel("financial_data.xlsx", index=False)

if __name__ == '__main__':
    main()
