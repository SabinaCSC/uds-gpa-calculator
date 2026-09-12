import streamlit as st

st.set_page_config(
    page_title="UDS Student Toolkit",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 UDS Student Toolkit")
st.caption(
    "Developed by Sabina Awenchiiminoi Akanko • "
    "BSc Computer Science • UDS Nyankpala"
)

# Grade points
grade_points = {
    "A": 4.0,
    "B+": 3.5,
    "B": 3.0,
    "C+": 2.5,
    "C": 2.0,
    "Pass": 1.0,
    "Fail": 0.0
}

# Course database
courses = {
    "100": {
        "Semester 1": [
            ("CSC 101", "Introduction to Computer Science", 3),
            ("CSC 103", "Programming Fundamentals I", 3),
            ("FRN 155", "French I", 2),
            ("GEN 101", "English Language and Communication Skills I", 2),
            ("MTH 103", "Differential Calculus", 3),
            ("MTH 105", "Discrete Mathematics and Its Applications", 3),
            ("PHY 113", "Introduction to Physics", 3)
        ],
        "Semester 2": []
    }
}

# Menu
page = st.radio(
    "Choose a tool",
    ["🏠 Home", "📊 GPA Calculator"]
)

# ---------------- HOME ----------------
if page == "🏠 Home":

    st.subheader("Welcome")
    st.write(
        "Welcome to your personal UDS Student Toolkit."
    )

    st.markdown("### Available Tool")
    st.markdown("📊 **GPA Calculator**")


# ---------------- GPA CALCULATOR ----------------
elif page == "📊 GPA Calculator":

    st.subheader("📊 GPA Calculator")

    programme = st.selectbox(
        "Programme",
        ["BSc Computer Science"]
    )

    level = st.selectbox(
        "Level",
        list(courses.keys())
    )

    semester = st.selectbox(
        "Semester",
        list(courses[level].keys())
    )

    selected_courses = courses[level][semester]

    if not selected_courses:

        st.info(
            f"Courses for Level {level}, {semester} "
            "have not been added yet."
        )

    else:

        st.subheader(
            f"📚 Level {level} — {semester}"
        )

        total_points = 0
        total_credits = 0

        for code, title, credit in selected_courses:

            grade = st.selectbox(
                f"{code} - {title} ({credit} credits)",
                list(grade_points.keys()),
                key=f"{level}_{semester}_{code}"
            )

            point = grade_points[grade]

            st.caption(
                f"Grade: {grade} • "
                f"Grade Point: {point:.1f} • "
                f"Credits: {credit}"
            )

            total_points += point * credit
            total_credits += credit

        st.divider()

        if st.button(
            "Calculate GPA",
            use_container_width=True
        ):

            gpa = total_points / total_credits

            st.success(
                f"🎉 Your GPA is {gpa:.2f}"
            )

            st.markdown("### 📋 Semester Summary")

            st.write(f"**Programme:** {programme}")
            st.write(f"**Level:** {level}")
            st.write(f"**Semester:** {semester}")
            st.write(f"**Total Credits:** {total_credits}")
            st.write(
                f"**Total Grade Points:** "
                f"{total_points:.1f}"
            )

            if gpa >= 3.6:
                st.balloons()
                st.success(
                    "🔥 Excellent! You're on track for First Class!"
                )

            elif gpa >= 3.0:
                st.info(
                    "👏 Strong performance! Keep pushing."
                )

            elif gpa >= 2.0:
                st.warning(
                    "⚠️ You can still improve your GPA."
                )

            else:
                st.error(
                    "📚 Keep working hard and seek help "
                    "where you need it."
                )
