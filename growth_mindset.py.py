import streamlit as st
import pandas as pd
import random
import matplotlib.pyplot as plt

st.set_page_config(page_title="Growth Mindset Challenge", page_icon="🌱", layout="wide")

# Navbar (Sidebar)
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Daily Challenge", "Mindset Exercises", "Motivational Quotes", "Progress Tracker"])

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

# Home Page
if page == "Home":
    st.title("🌱 Growth Mindset Challenge")
    st.subheader("Develop a Mindset for Success 🚀")

    st.write("""
    A **growth mindset** means believing that your abilities and intelligence can develop through effort, learning, and persistence.
    Let's explore how you can adopt this mindset and improve continuously!
    """)

    st.subheader("Why Adopt a Growth Mindset?")
    st.markdown("""
    ✅ **Embrace Challenges** – View obstacles as learning opportunities.  
    ✅ **Learn from Mistakes** – Mistakes are part of growth!  
    ✅ **Persist Through Difficulties** – Stay determined and keep trying.  
    ✅ **Celebrate Effort** – Focus on progress, not just results.  
    ✅ **Keep an Open Mind** – Stay curious and adaptable.  
    """)

    # User Reflection
    st.subheader("📝 Reflect on Your Journey")
    user_input = st.text_area("Write about a recent challenge you faced and how you approached it with a growth mindset:")

    if st.button("Submit"):
        if user_input:
            st.success("Great! Reflecting on challenges helps build a stronger mindset. Keep going!")
        else:
            st.warning("Please write something to reflect on your growth journey!")

    # Encouragement Message
    st.subheader("Remember:")
    st.info("Every step you take, forward or backward, is part of learning. Keep striving to be better! 🚀")

elif page == "Daily Challenge":
    st.title("🎯 Daily Growth Mindset Challenge")

    challenges = [
        "Think of a mistake you made recently. How did you learn from it?",
        "Try something new today that you've never done before.",
        "Encourage a friend or classmate who is struggling.",
        "Write down 3 things you are grateful for today.",
        "Find one thing you learned from a failure and write about it.",
        "Step outside your comfort zone and take on a small challenge."
    ]

    st.write(f"🌟 **Today's Challenge:** {random.choice(challenges)}")

    # Encouragement Message
    st.subheader("Remember:")
    st.info("Every step you take, forward or backward, is part of learning. Keep striving to be better! 🚀")

elif page == "Mindset Exercises":
    st.title("🧠 Growth Mindset Exercises")

    st.subheader("1️⃣ Reframe Negative Thoughts")
    st.write("Instead of saying *'I'm not good at this'*, say *'I can improve with practice.'*")

    st.subheader("2️⃣ Focus on Effort, Not Just Results")
    st.write("Instead of *'I failed'*, say *'This was a learning experience.'*")

    st.subheader("3️⃣ Embrace Constructive Criticism")
    st.write("Listen to feedback and see it as a tool for growth.")

    st.subheader("Remember:")
    st.info("Every step you take, forward or backward, is part of learning. Keep striving to be better! 🚀")

elif page == "Motivational Quotes":
    st.title("💬 Motivational Quotes")

    quotes = [
        "“Success is not final, failure is not fatal: it is the courage to continue that counts.” – Winston Churchill",
        "“Believe you can and you’re halfway there.” – Theodore Roosevelt",
        "“It does not matter how slowly you go as long as you do not stop.” – Confucius",
        "“The only limit to our realization of tomorrow is our doubts of today.” – Franklin D. Roosevelt",
        "“Difficulties strengthen the mind, as labor does the body.” – Seneca"
    ]

    st.write(f"📢 **Quote of the Day:** *{random.choice(quotes)}*")

    # Encouragement Message
    st.subheader("Remember:")
    st.info("Every step you take, forward or backward, is part of learning. Keep striving to be better! 🚀")

elif page == "Progress Tracker":
    st.title("📊 Progress Tracker")

    uploaded_file = st.file_uploader("Upload your progress file (CSV or Excel)", type=["csv", "xlsx"])

    if uploaded_file is not None:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        st.write("📋 Data Preview:")
        st.dataframe(df)

        st.download_button(label="Download Data", data=uploaded_file.getvalue(), file_name=uploaded_file.name)

        # Data visualization
        st.write("📈 Effort vs. Results")
        if 'Effort' in df.columns and 'Results' in df.columns:
            fig, ax = plt.subplots()
            ax.scatter(df['Effort'], df['Results'], color='green')
            ax.set_xlabel('Effort')
            ax.set_ylabel('Results')
            ax.set_title('Effort vs. Results')
            st.pyplot(fig)
        else:
            st.warning("Make sure your file has 'Effort' and 'Results' columns!")

# Footer
st.sidebar.markdown("---")
st.sidebar.write("🚀 Keep Growing & Never Stop Learning!")
