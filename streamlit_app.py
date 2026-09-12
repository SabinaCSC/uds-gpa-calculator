import streamlit as st

st.set_page_config(
    page_title="UDS Student Toolkit",
    page_icon="🎓"
)

st.title("🎓 UDS Student Toolkit")

st.write("Welcome, Sabina Awenchiiminoi Akanko! 👋🏽")

st.divider()

programme = st.selectbox(
    "🎓 Select Programme",
    [
        "BSc Computer Science",
        "BSc Accounting",
        "BSc Economics",
        "BSc Mathematics",
        "BSc Public Health",
        "Bachelor of Law (LLB)"
    ]
)

level = st.selectbox(
    "📚 Select Level",
    ["100", "200", "300", "400"]
)

trimester = st.selectbox(
    "📅 Select Trimester",
    [
        "Trimester 1",
        "Trimester 2",
        "Trimester 3"
    ]
)

st.divider()

st.subheader("Your Selection")

st.write(f"**Programme:** {programme}")
st.write(f"**Level:** {level}")
st.write(f"**Trimester:** {trimester}")

st.success("✅ The programme selection is working!")
