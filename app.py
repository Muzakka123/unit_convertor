import streamlit as st

# App Title
st.title("Unit Converter")

# Conversion types
conversion_types = ["Length", "Weight", "Temperature"]

# User selects conversion type
conversion_choice = st.selectbox("Choose Conversion Type:", conversion_types)

# Input fields
input_value = st.number_input("Enter value:", min_value=0.0, format="%.2f")

# Length Conversion
if conversion_choice == "Length":
    units = ["Meters", "Kilometers", "Feet", "Inches", "Centimeters"]
    conversion_dict = {
        "Meters": 1,
        "Kilometers": 1000,
        "Feet": 0.3048,
        "Inches": 0.0254,
        "Centimeters": 0.01
    }

# Weight Conversion
elif conversion_choice == "Weight":
    units = ["Kilograms", "Grams", "Pounds", "Ounces"]
    conversion_dict = {
        "Kilograms": 1,
        "Grams": 0.001,
        "Pounds": 0.453592,
        "Ounces": 0.0283495
    }

# Temperature Conversion
elif conversion_choice == "Temperature":
    units = ["Celsius", "Fahrenheit", "Kelvin"]

# Dropdowns for selecting units
from_unit = st.selectbox("From Unit:", units)
to_unit = st.selectbox("To Unit:", units)

# Temperature conversion function
def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif to_unit == "Kelvin":
            return value + 273.15
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            return (value - 32) * 5/9
        elif to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            return value - 273.15
        elif to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
    return value  # If same unit is selected

# Single Convert Button
if st.button("Convert"):
    if conversion_choice == "Temperature":
        result = convert_temperature(input_value, from_unit, to_unit)
    else:
        result = input_value * (conversion_dict[from_unit] / conversion_dict[to_unit])
    
    st.success(f'{input_value} {from_unit} is equal to {result:.2f} {to_unit}')