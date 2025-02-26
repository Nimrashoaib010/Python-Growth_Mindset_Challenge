import streamlit as st

# Set page config for light and dark mode
st.set_page_config(page_title="Smart Unit Converter", page_icon="🔄", layout="centered")

# Add custom CSS for styling
st.markdown("""
    <style>
        .main { background-color: #f5f5f5; }
        h1 { color: #4CAF50; text-align: center; }
        .stSelectbox, .stNumber_input, .stButton, .stInfo { margin: 10px auto; }
    </style>
""", unsafe_allow_html=True)

# Navigation bar
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Unit Converter", "About"])

# Dark and light mode toggle
mode = st.sidebar.radio("Choose Mode", ["Light", "Dark"])
if mode == "Dark":
    st.markdown("""
        <style>
            .main, body, .stApp { background-color: black !important; color: white !important; }
            .stSelectbox, .stNumber_input, .stButton, .stInfo { color: white !important; }
            .css-1d391kg, .css-18e3th9 { background-color: #333 !important; color: white !important; }
            .sidebar .css-1d391kg, .sidebar .css-18e3th9 { background-color: black !important; color: white !important; }
            .sidebar { background-color: black !important; color: white !important; }
        </style>
    """, unsafe_allow_html=True)

if page == "About":
    st.write("## About this App")
    st.write("A unit conversion expresses the same property as a different unit of measurement. For instance, time can be expressed in minutes instead of hours, while distance can be converted from miles to kilometers, or feet, or any other measure of length. This is a simple, stylish, and interactive unit converter built with Streamlit.")
else:
    # Title of the app with emoji
    st.title("Smart Unit Converter ✨")

    # Unit categories
    unit_categories = ["Length", "Weight", "Temperature"]

    # Select unit category
    category = st.selectbox("Select a category", unit_categories)

    # Conversion options based on category
    units = {
        "Length": ["Meter", "Kilometer", "Mile", "Yard", "Inch", "Centimeter"],
        "Weight": ["Gram", "Kilogram", "Pound", "Ounce"],
        "Temperature": ["Celsius", "Fahrenheit", "Kelvin"]
    }

    # Select 'from' and 'to' units
    from_unit = st.selectbox("From", units[category])
    to_unit = st.selectbox("To", units[category])

    # Input value
    value = st.number_input("Enter value", min_value=0.0, format="%.2f")

    # Conversion formulas
    conversion_rates = {
        ("Meter", "Kilometer" ): 0.001,
        ("Kilometer", "Meter" ): 1000,
        ("Mile", "Yard" ): 1760,
        ("Yard", "Mile" ): 1/1760,
        ("Inch", "Centimeter" ): 2.54,
        ("Centimeter", "Inch" ): 1/2.54,
        ("Gram", "Kilogram" ): 0.001,
        ("Kilogram", "Gram" ): 1000,
        ("Pound", "Ounce" ): 16,
        ("Ounce", "Pound" ): 1/16
    }

    # Temperature conversion
    def convert_temperature(value, from_unit, to_unit):
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            return (value - 32) * 5/9
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            return value + 273.15
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            return value - 273.15
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
        else:
            return value

    # Convert value
    if st.button("Convert"):
        if category == "Temperature":
            result = convert_temperature(value, from_unit, to_unit)
        else:
            rate = conversion_rates.get((from_unit, to_unit))
            if rate:
                result = value * rate
            else:
                result = "Conversion not supported!"

        st.write(f"{value} {from_unit} = {result} {to_unit}")

    # Formula display
    if category == "Length" and (from_unit, to_unit) in conversion_rates:
        st.info(f"Formula: multiply the {category.lower()} value by {conversion_rates[(from_unit, to_unit)]}")
