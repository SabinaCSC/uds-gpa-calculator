import streamlit as st

st.set_page_config(
    page_title="UDS Student Toolkit",
    page_icon="🎓",
    layout="centered"
)

# ---------------- HEADER ----------------

st.title("🎓 UDS Student Toolkit")

st.caption(
    "Developed by Sabina Awenchiiminoi Akanko • "
    "BSc Computer Science • UDS Nyankpala"
)

st.divider()

# ---------------- GRADE POINTS ----------------

grade_points = {
    "A": 4.0,
    "B+": 3.5,
    "B": 3.0,
    "C+": 2.5,
    "C": 2.0,
    "Pass": 1.0,
    "Fail": 0.0
}

# ---------------- PROGRAMMES & COURSES ----------------

courses = {

    "BSc Computer Science": {

        "100": {

            "Trimester 1": [
                ("CSC 101", "Introduction to Computer Science", 3),
                ("CSC 103", "Programming Fundamentals I", 3),
                ("FRN 155", "French I", 2),
                ("GEN 101", "English Language and Communication Skills I", 2),
                ("MTH 103", "Differential Calculus", 3),
                ("MTH 105", "Discrete Mathematics and Its Applications", 3),
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
    },

    "BSc Information Technology": {
        "100": {
            "Trimester 1": [],
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
    },

    "BSc Mathematics": {
        "100": {
            "Trimester 1": [],
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
    },

    "BSc Statistics": {
        "100": {
            "Trimester 1": [],
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
    },

    "BSc Actuarial Science": {
        "100": {
            "Trimester 1": [],
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
    },

    "BSc Business Administration": {
        "100": {
            "Trimester 1": [],
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
    },

    "BSc Accounting": {
        "100": {
            "Trimester 1": [],
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
    },

    "BSc Economics": {
        "100": {
            "Trimester 1": [],
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
    },

    "BSc Public Health": {
        "100": {
            "Trimester 1": [],
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

# ---------------- MENU ----------------

page = st.radio(
    "Choose a tool",
    ["🏠 Home", "📊 GPA Calculator"]
)

# ---------------- HOME ----------------

if page == "🏠 Home":

    st.subheader("Welcome 👋🏽")

    st.write(
        "Welcome to your personal UDS Student Toolkit."
    )

    st.write(
        "Select your programme and academic level "
        "to calculate your GPA."
    )

    st.markdown("### 📊 Available Tool")
    st.markdown("**GPA Calculator**")


# ---------------- GPA CALCULATOR ----------------

elif page == "📊 GPA Calculator":

    st.subheader("📊 GPA Calculator")

    student_name = st.text_input(
        "👤 Student Name"
    )

    programme = st.selectbox(
        "🎓 Programme",
        list(courses.keys())
    )

    level = st.selectbox(
        "📚 Level",
        list(courses[programme].keys())
    )

    trimester = st.selectbox(
        "📅 Trimester",
        list(courses[programme][level].keys())
    )

    selected_courses = courses[programme][level][trimester]

    # ---------------- NO COURSES ----------------

    if not selected_courses:

        st.info(
            f"Courses for {programme}, Level {level}, "
            f"{trimester} have not been added yet."
        )

    # ---------------- COURSES ----------------

    else:

        st.subheader(
            f"📚 {programme} — Level {level} — {trimester}"
        )

        total_points = 0
        total_credits = 0

        for code, title, credit in selected_courses:

            grade = st.selectbox(
                f"{code} - {title} ({credit} credits)",
                list(grade_points.keys()),
                key=f"{programme}_{level}_{trimester}_{code}"
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

        # ---------------- CALCULATE ----------------

        if st.button(
            "Calculate GPA",
            use_container_width=True
        ):

            if student_name.strip() == "":
                st.warning(
                    "Please enter your name before calculating."
                )

            else:

                gpa = total_points / total_credits

                st.success(
                    f"🎉 {student_name}, your GPA is {gpa:.2f}"
                )

                st.markdown("### 📋 Trimester Summary")

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
                    f"**Total Credits:** {total_credits}"
                )

                st.write(
                    f"**Total Grade Points:** "
                    f"{total_points:.1f}"
                )

                # ---------------- PERFORMANCE ----------------

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
