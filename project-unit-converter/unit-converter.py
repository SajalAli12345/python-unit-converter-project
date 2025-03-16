import streamlit as st

st.title("🌎 Unit Converter App")
st.markdown("### Converts Length , Weight , And Time Instantly")
st.write("Welcome! Select the category , enter a value and get the converted result...")

category = st.selectbox("Choose a category",["Length","Weight","Time"])

def convert_units(category, value, unit):
    if category == "Length":
        if unit == "Kilometers to Miles":
            return value * 0.621371
        elif unit == "Miles to Kilometers":
            return value / 0.621371
        
    elif category == "Weight":
        if unit == "Kilograms to pounds":
            return value * 2.20462
        elif unit == "Pounds to kilograms":
            return value / 2.20462
        
    elif category == "Time":
        if unit ==  "Minutes to seconds":
            return value * 60
        elif unit == "Seconds to minutes":
            return value / 60
        elif unit == "Minutes to hours":
            return value / 60
        elif unit == "Hours to minutes":
            return value * 60
        elif unit == "Days to hours":
            return value * 24
        elif unit == "Hours to days":
            return value / 24 
        
if category == "Length":
    unit = st.selectbox("📏 Select Conversation",["Kilometers to Miles","Miles to Kilometers"])
elif category == "Weight":
    unit = st.selectbox("⚖ Select Conversation",["Kilograms to pounds","Pounds to kilograms"])    
elif category == "Time":
    unit = st.selectbox("⏱ Select Conversation",["Minutes to seconds","Seconds to minutes","Minutes to hours","Hours to minutes","Days to hours","Hours to days"])

value = st.number_input("Enter the value to convert")                

if st.button("Converts"):
    result = convert_units(category, value, unit)
    st.success(f"The result is {result:.2f}")
