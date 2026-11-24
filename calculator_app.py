import math
import streamlit as st


# Title
st.title("Basic Web Calculator")

# Input fields
num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

# Operation selection
operation = st.selectbox(
    "Choose operation",
    ["Add", "Subtract", "Multiply", "Divide", "Sin (degrees)", "Log (base 10)"]
)

# Calculate
if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        result = num1 / num2 if num2 != 0 else "Error: Division by zero"
    elif operation == "Sin (degrees)":
        result = math.sin(math.radians(num1))
    elif operation == "Log (base 10)":
        if num1 <= 0:
            st.error("Enter a number greater than 0 to calculate a logarithm.")
            st.stop()
        result = math.log10(num1)

    st.success(f"Result: {result}")
