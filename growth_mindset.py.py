
import streamlit as st
import random

# Set page configuration
st.set_page_config(page_title="Growth Mindset Challenge", page_icon="🌱", layout="wide")

# Navbar (Sidebar)
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Daily Challenge", "Mindset Exercises", "Motivational Quotes"])

# Home Page
if page == "Home":
    st.title("🌱 Growth Mindset Challenge")
    st.subheader("Develop a Mindset for Success 🚀")

    st.write("""
    A **growth mindset** means believing that your abilities and intelligence can develop through effort, learning, and persistence.
    Let's explore how you can adopt this mindset and improve continuously!
    """)

    # Why Growth Mindset?
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


# Daily Challenge Page
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

# Mindset Exercises Page
elif page == "Mindset Exercises":
    st.title("🧠 Growth Mindset Exercises")

    st.subheader("1️⃣ Reframe Negative Thoughts")
    st.write("Instead of saying *'I'm not good at this'*, say *'I can improve with practice.'*")

    st.subheader("2️⃣ Focus on Effort, Not Just Results")
    st.write("Instead of *'I failed'*, say *'This was a learning experience.'*")

    st.subheader("3️⃣ Embrace Constructive Criticism")
    st.write("Listen to feedback and see it as a tool for growth.")

    # Encouragement Message
    st.subheader("Remember:")
    st.info("Every step you take, forward or backward, is part of learning. Keep striving to be better! 🚀")

# Motivational Quotes Page
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
# Footer
st.sidebar.markdown("---")
st.sidebar.write("🚀 Keep Growing & Never Stop Learning!")