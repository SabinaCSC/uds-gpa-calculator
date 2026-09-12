import streamlit as st

st.set_page_config(page_title="UDS Student Toolkit", page_icon="🎓")

# GPA points
grade_points = {
    "A": 4.0,
    "B+": 3.5,
    "B": 3.0,
    "C+": 2.5,
    "C": 2.0,
    "Pass": 1.0,
    "Fail": 0.0
}

# Official Computer Science Level 100 Semester 1
courses = [
    ("CSC 101", "Introduction to Computer Science", 3),
    ("CSC 103", "Programming Fundamentals I", 3),
    ("FRN 155", "French I", 2),
    ("GEN 101", "English Language and Communication Skills I", 2),
    ("MTH 103", "Differential Calculus", 3),
    ("MTH 105", "Discrete Mathematics and Its Applications", 3),
    ("PHY 113", "Introduction to Physics", 3)
]

st.title("🎓 UDS Student Toolkit")

page = st.radio(
    "Choose a tool",
    ["Home", "Grade Checker", "GPA Calculator"]
)

if page == "Home":
    st.header("Welcome")
    st.write("Built by Sabina Akanko for the UDS student body.")
    st.write("Choose a tool above.")

elif page == "Grade Checker":
    st.header("Grade Checker")

    name = st.text_input("Enter your name")
    score = st.number_input(
        "Enter your score",
        min_value=0,
        max_value=100,
        step=1
    )

    if st.button("Check Grade"):
        if score >= 80:
            grade = "Grade A"
        elif score >= 75:
            grade = "Grade B+"
        elif score >= 70:
            grade = "Grade B"
        elif score >= 65:
            grade = "Grade C+"
        elif score >= 60:
            grade = "Grade C"
        elif score >= 50:
            grade = "Pass"
        else:
            grade = "Fail"

        st.success(f"{name}, your result is: {grade}")

elif page == "GPA Calculator":
    st.header("BSc Computer Science - Level 100 Semester 1")

    total_points = 0
    total_credits = 0

    for code, title, credit in courses:
        grade = st.selectbox(
            f"{code} - {title} ({credit} credits)",
            list(grade_points.keys()),
            key=code
        )

        total_points += grade_points[grade] * credit
        total_credits += credit

    if st.button("Calculate GPA"):
        gpa = total_points / total_credits

        st.success(f"Your GPA is {gpa:.2f}")
        st.write(f"Total Credits: {total_credits}")
        st.write(f"Total Grade Points: {total_points:.1f}")

        if gpa >= 3.6:
            st.balloons()
            st.success("You're on track for First Class!")
        elif gpa >= 3.0:
            st.info("Strong performance. Keep pushing.")
        elif gpa >= 2.0:
            st.warning("You can still improve.")
        else:
            st.error("Time to work harder next semester.")
