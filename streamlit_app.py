import streamlit as st

# -----------------------------
# PAGE SETTINGS
# -----------------------------
st.set_page_config(
    page_title="UDS Student Toolkit",
    page_icon="🎓",
    layout="centered"
)

# -----------------------------
# TITLE
# -----------------------------
st.title("🎓 UDS Student Toolkit")

st.caption(
    "Developed by Sabina Awenchiiminoi Akanko • "
    "BSc Computer Science • UDS Nyankpala"
)

st.divider()

# -----------------------------
# GRADE POINTS
# -----------------------------
grade_points = {
    "A": 4.0,
    "B+": 3.5,
    "B": 3.0,
    "C+": 2.5,
    "C": 2.0,
    "Pass": 1.0,
    "Fail": 0.0
}

# -----------------------------
# COURSE DATABASE
# -----------------------------
# Structure:
# Programme
#     ↓
# Level
#     ↓
# Trimester
#     ↓
# Courses

courses = {

    # =========================
    # COMPUTER SCIENCE
    # =========================
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

    # =========================
    # OTHER UDS PROGRAMMES
    # =========================

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

    "BSc Banking and Finance": {
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

    "BSc Business Information Systems": {
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

    "BSc Food Science and Technology": {
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

    "BSc Food Systems": {
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

    "BSc Biochemistry": {
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
    },

    "Bachelor of Law (LLB)": {
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

# -----------------------------
# SIDEBAR / PAGE NAVIGATION
# -----------------------------

page = st.radio(
    "Choose a tool",
    ["🏠 Home", "📊 GPA Calculator"]
)

# -----------------------------
# HOME
# -----------------------------

if page == "🏠 Home":

    st.subheader("Welcome 👋🏽")

    st.write(
        "Welcome to the UDS Student Toolkit."
    )

    st.write(
        "Choose your programme, level and trimester "
        "to calculate your GPA."
    )

    st.divider()

    st.markdown("### 📊 Available Tool")

    st.markdown(
        "**GPA Calculator**"
    )

# -----------------------------
# GPA CALCULATOR
# -----------------------------

elif page == "📊 GPA Calculator":

    st.subheader("📊 GPA Calculator")

    # Student name
    student_name = st.text_input(
        "👤 Student Name"
    )

    # Programme
    programme = st.selectbox(
        "🎓 Select Programme",
        list(courses.keys())
    )

    # Level ONLY comes from selected programme
    level = st.selectbox(
        "📚 Select Level",
        list(courses[programme].keys())
    )

    # Trimester ONLY comes from selected programme + level
    trimester = st.selectbox(
        "📅 Select Trimester",
        list(courses[programme][level].keys())
    )

    # Get courses ONLY for the selected programme,
    # selected level and selected trimester
    selected_courses = courses[programme][level][trimester]

    st.divider()

    # -----------------------------
    # SHOW COURSES
    # -----------------------------

    if not selected_courses:

        st.info(
            f"Courses for {programme}, Level {level}, "
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

        # Show ONLY courses belonging to the
        # selected programme
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

        # -----------------------------
        # CALCULATE GPA
        # -----------------------------

        if st.button(
            "Calculate GPA",
            use_container_width=True
        ):

            if student_name.strip() == "":

                st.warning(
                    "Please enter your name before calculating."
                )

            elif total_credits == 0:

                st.warning(
                    "There are no courses available for "
                    "this selection yet."
                )

            else:

                gpa = (
                    total_grade_points /
                    total_credits
                )

                st.success(
                    f"🎉 {student_name}, your GPA is {gpa:.2f}"
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
                    f"**Total Credits:** {total_credits}"
                )

                st.write(
                    f"
