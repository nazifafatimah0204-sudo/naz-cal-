import streamlit as st

# Configure the webpage
st.set_page_config(
    page_title="Simple Calculator",
    page_icon="🧮",
    layout="centered"
)

# Title
st.title("🧮 Simple Calculator")

st.write("Enter two numbers and select an operation.")

# Input numbers
num1 = st.number_input("Enter the first number", value=0.0)
num2 = st.number_input("Enter the second number", value=0.0)

# Select mathematical operation
operation = st.selectbox(
    "Select an operation",
    ["Addition (+)", "Subtraction (-)", "Multiplication (×)", "Division (÷)"]
)

# Calculate button
if st.button("Calculate", type="primary"):

    if operation == "Addition (+)":
        result = num1 + num2

    elif operation == "Subtraction (-)":
        result = num1 - num2

    elif operation == "Multiplication (×)":
        result = num1 * num2

    elif operation == "Division (÷)":
        if num2 == 0:
            st.error("Cannot divide by zero!")
            result = None
        else:
            result = num1 / num2

    # Display result
    if result is not None:
        st.success(f"Result: {result}")

# Additional information
st.divider()

st.caption("Built with Python and Streamlit")
