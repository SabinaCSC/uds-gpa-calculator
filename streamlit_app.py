import streamlit as st

# ==============================
# PAGE SETTINGS
# ==============================

st.set_page_config(
    page_title="UDS Student Toolkit",
    page_icon="🎓",
    layout="centered"
)

# ==============================
# TITLE
# ==============================

st.title("🎓 UDS Student Toolkit")

st.caption(
    "Developed by Sabina Awenchiiminoi Akanko • "
    "BSc Computer Science • UDS Nyankpala"
)

st.divider()

# ==============================
# GRADE POINTS
# ==============================

grade_points = {
    "A": 4.0,
    "B+": 3.5,
    "B": 3.0,
    "C+": 2.5,
    "C": 2.0,
    "Pass": 1.0,
    "Fail": 0.0
}

# ==============================
# COURSE DATABASE
# ==============================

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

# ==============================
# NAVIGATION
# ==============================

page = st.radio(
    "Choose a tool",
    [
        "🏠 Home",
        "📊 GPA Calculator"
    ]
)

# ==============================
# HOME PAGE
# ==============================

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

    st.markdown("**GPA Calculator
