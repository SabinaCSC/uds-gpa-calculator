import streamlit as st

# ==========================================
# PAGE SETTINGS
# ==========================================

st.set_page_config(
    page_title="UDS Student Toolkit",
    page_icon="🎓",
    layout="centered"
)

# ==========================================
# HEADER
# ==========================================

st.title("🎓 UDS Student Toolkit")

st.caption(
    "Developed by Sabina Awenchiiminoi Akanko • "
    "BSc Computer Science • UDS Nyankpala"
)

st.divider()

# ==========================================
# GRADE POINTS
# ==========================================

grade_points = {
    "A": 4.0,
    "B+": 3.5,
    "B": 3.0,
    "C+": 2.5,
    "C": 2.0,
    "Pass": 1.0,
    "Fail": 0.0
}

# ==========================================
# PROGRAMMES
# ==========================================

programmes = [
    "BSc Computer Science",
    "BSc Accounting",
    "BSc Actuarial Science",
    "BSc Agribusiness",
    "BSc Agricultural and Food Economics",
    "BSc Business Information Systems",
    "BSc Chemical Science and Technology",
    "BSc Computing Mathematics",
    "BSc Economics",
    "BSc Engineering Physics",
    "BSc Finance and Economics",
    "BSc Food Science and Technology",
    "BSc Food Systems",
    "BSc Forensic Science",
    "BSc Human Resource Management",
    "BSc Mathematics",
    "BSc Medical Imaging Technology",
    "BSc Marketing",
    "BSc Public Health",
    "BSc Procurement and Supply Chain Management",
    "BSc Statistics",
    "Bachelor of Law (LLB)"
]

# ==========================================
# COURSE DATABASE
# ==========================================
#
# IMPORTANT:
# Courses are organised by:
#
# Programme
#     ↓
# Level
#     ↓
# Trimester
#     ↓
# Course
#
# A course will ONLY appear after the
# student selects the relevant programme,
# level and trimester.
# ==========================================

courses = {
    "BSc Computer Science": {
        "100": {
            "Trimester 1": [
                ("CSC 101", "Introduction to Computer Science", 3),
                ("CSC 103", "Programming Fundamentals I", 3),
                ("FRN 155", "French I", 2),
                (
                    "GEN 101",
                    "English Language and Communication Skills I",
                    2
                ),
                ("MTH 103", "Differential Calculus", 3),
                (
                    "MTH 105",
                    "Discrete Mathematics and Its Applications",
                    3
                ),
                ("PHY 113", "Introduction to Physics", 3)
            ],
            "Trimester 2": [],
            "Trimester 3": []
        },

        "200": {
            "Trimester 1": [],
            "Trimester 2": [],
            "Trimester 3": []
        },

        "300": {
            "Trimester 1": [],
            "Trimester 2": [],
            "Trimester 3": []
        },

        "400": {
            "Trimester 1": [],
            "Trimester 2": [],
            "Trimester 3": []
        }
    }
}

# ==========================================
# PAGE NAVIGATION
# ==========================================

page = st.radio(
    "Choose a tool",
    [
        "🏠 Home",
        "📊 GPA Calculator"
    ]
)

# ==========================================
# HOME
# ==========================================

if page == "🏠 Home":

    st.subheader("Welcome 👋🏽")

    st.write(
        "The UDS Student Toolkit is designed to help "
        "students calculate and track their academic performance."
    )

    st.markdown("### 📊 Available Tool")

    st.markdown("**GPA Calculator**")

# ==========================================
# GPA CALCULATOR
# ==========================================

elif page == "📊 GPA Calculator":

    st.subheader("📊 GPA Calculator")

    student_name = st.text_input(
        "👤 Student Name"
    )

    # --------------------------------------
    # PROGRAMME
    # --------------------------------------

    programme = st.selectbox(
        "🎓 Select Programme",
        programmes
    )

    # --------------------------------------
    # LEVEL
    # --------------------------------------

    level = st.selectbox(
        "📚 Select Level",
        [
            "100",
            "200",
            "300",
            "400"
        ]
    )

    # --------------------------------------
    # TRIMESTER
    # --------------------------------------

    trimester = st.selectbox(
        "📅 Select Trimester",
        [
            "Trimester 1",
            "Trimester 2",
            "Trimester 3"
        ]
    )

    st.divider()

    # ======================================
    # ONLY GET COURSES AFTER SELECTION
    # ======================================

    programme_courses = courses.get(programme)

    if programme_courses is None:

        st.info(
            f"Course information for {programme} "
            "has not been added yet."
        )

    else:

        level_courses = programme_courses.get(level)

        if level_courses is None:

            st.info(
                f"Course information for {programme}, "
                f"Level {level} has not been added yet."
            )

        else:

            selected_courses = level_courses.get(
                trimester,
                []
            )

            # ==================================
            # COURSES FOR SELECTED PROGRAMME
            # ==================================

            if not selected_courses:

                st.info(
                    f"Courses for {programme}, "
                    f"Level {level}, "
                    f"{trimester} have not been added yet."
                )

            else:

                st.subheader(
                    f"📚 {programme}"
                )

                st.caption(
                    f"Level {level} • {trimester}"
                )

                total_grade_points = 0
                total_credits = 0

                # --------------------------------
                # DISPLAY SELECTED COURSES
                # --------------------------------

                for code, title, credit in selected_courses:

                    grade = st.selectbox(
                        f"{code} — {title} ({credit} credits)",
                        list(grade_points.keys()),
                        key=f"{programme}_{level}_{trimester}_{code}"
                    )

                    point = grade_points[grade]

                    st.caption(
                        f"Grade: {grade} • "
                        f"Grade Point: {point:.1f} • "
                        f"Credits: {credit}"
                    )

                    total_grade_points += point * credit
                    total_credits += credit

                st.divider()

                # ==================================
                # CALCULATE GPA
                # ==================================

                if st.button(
                    "Calculate GPA",
                    use_container_width=True
                ):

                    if not student_name.strip():

                        st.warning(
                            "Please enter your name "
                            "before calculating."
                        )

                    else:

                        gpa = (
                            total_grade_points /
                            total_credits
                        )

                        st.success(
                            f"🎉 {student_name}, "
                            f"your GPA is {gpa:.2f}"
                        )

                        st.markdown(
                            "### 📋 Trimester Summary"
                        )

                        st.write(
                            f"**Student:** {student_name}"
                        )

                        st.write(
                            f"**Programme:** {programme}"
                        )

                        st.write(
                            f"**Level:** {level}"
                        )

                        st.write(
                            f"**Trimester:** {trimester}"
                        )

                        st.write(
                            f"**Total Credits:** "
                            f"{total_credits}"
                        )

                        st.write(
                            f"**Total Grade Points:** "
                            f"{total_grade_points:.1f}"
                        )

                        # ==========================
                        # GPA FEEDBACK
                        # ==========================

                        if gpa >= 3.6:

                            st.balloons()

                            st.success(
                                "🔥 Excellent performance! "
                                "You're on track for First Class!"
                            )

                        elif gpa >= 3.0:

                            st.info(
                                "👏 Strong performance! "
                                "Keep pushing."
                            )

                        elif gpa >= 2.0:

                            st.warning(
                                "⚠️ You can still improve "
                                "your GPA."
                            )

                        else:

                            st.error(
                                "📚 Keep working hard and "
                                "seek help where you need it."
                            )
