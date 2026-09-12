import streamlit as st

st.set_page_config(page_title="UDS Student Toolkit", page_icon="🎓")

st.title("🎓 UDS Student Toolkit")
st.write("Built by Sabina Akanko for the UDS student body. 💙")

page = st.radio(
    "Choose a tool",
    ["🏠 Home", "🎓 Grade Checker", "📊 GPA Calculator"]
)

grade_points = {
    "A": 4.0,
    "B+": 3.5,
    "B": 3.0,
    "C+": 2.5,
    "C": 2.0,
    "Pass": 1.0,
    "Fail": 0.0
}

if page == "🏠 Home":
    st.header("Welcome")
    st.write("Choose a tool below.")
    st.markdown("- 🎓 Grade Checker")
    st.markdown("- 📊 GPA Calculator")

elif page == "🎓 Grade Checker":
    st.header("Grade Checker")

    name = st.text_input("Enter your name")
    score = st.number_input("Enter your score", min_value=0, max_value=100, step=1)

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

        st.success(f"🎉 {name}, your result is: {grade}")

elif page == "📊 GPA Calculator":
    st.header("BSc Computer Science – Level 100 Semester 1")

    courses = [
        ("CSC 101", "Introduction to Computer Science", 3),
        ("CSC 103", "Programming Fundamentals I", 3),
        ("FRN 155", "French I", 2),
        ("GEN 101", "English Language and Communication Skills I", 2),
        ("MTH 103", "Differential Calculus", 3),
        ("MTH 105", "Discrete Mathematics and Its Applications", 3),
        ("PHY 113", "Introduction to Physics", 3),
    ]

    total_points = 0
    total_credits = 0

    st.subheader("Select your grades")

    for code, title, credit in courses:
        grade = st.selectbox(
            f"{code} – {title} ({credit} credits)",
            list(grade_points.keys()),
            key=code
        )

        total_points += grade_points[grade] * credit
        total_credits += credit

    if st.button("Calculate GPA"):
        gpa = total_points / total_credits

        st.success(f"🎉 Your GPA is {gpa:.2f}")

        st.write("### Semester Summary")
        st.write("**Programme:** BSc Computer Science")
        st.write("**Level:** 100")
        st.write("**Semester:** Semester 1")
        st.write(f"**Total Credits:** {total_credits}")
        st.write(f"**Total Grade Points:** {total_points:.1f}")

        if gpa >= 3.6:
            st.balloons()
            st.success("🔥 You're on track for First Class!")
        elif gpa >= 3.0:
            st.info("👏 Strong performance! Keep pushing.")
        elif gpa >= 2.0:
            st.warning("⚠️ You can still improve.")
        else:
            st.error("📚 Time to work harder next semester.")import streamlit as st

st.set_page_config(page_title="UDS Student Toolkit", page_icon="🎓")

st.title("🎓 UDS Student Toolkit")
st.write("Built by Sabina Akanko for the UDS student body. 💙")

page = st.radio(
    "Choose a tool",
    ["🏠 Home", "🎓 Grade Checker", "📊 GPA Calculator"]
)

grade_points = {
    "A": 4.0,
    "B+": 3.5,
    "B": 3.0,
    "C+": 2.5,
    "C": 2.0,
    "Pass": 1.0,
    "Fail": 0.0
}

if page == "🏠 Home":
    st.header("Welcome")
    st.write("Choose a tool above.")
    st.markdown("- 🎓 Grade Checker")
    st.markdown("- 📊 GPA Calculator")

elif page == "🎓 Grade Checker":
    st.header("Grade Checker")

    name = st.text_input("Enter your name")
    score = st.number_input("Enter your score", 0, 100, 0)

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

        st.success(f"🎉 {name}, your result is: {grade}")

elif page == "📊 GPA Calculator":
    st.header("Computer Science Level 100 Semester 1")

    courses = [
        ("CSC 101", "Introduction to Computer Science", 3),
        ("CSC 103", "Programming Fundamentals I", 3),
        ("FRN 155", "French I", 2),
        ("GEN 101", "English Language and Communication Skills I", 2),
        ("MTH 103", "Differential Calculus", 3),
        ("MTH 105", "Discrete Mathematics and Its Applications", 3),
        ("PHY 113", "Introduction to Physics", 3),
    ]

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

        st.success(f"🎉 Your GPA is {gpa:.2f}")

        if gpa >= 3.6:
            st.balloons()
            st.info("🔥 You're on track for First Class!")import streamlit as st

st.set_page_config(page_title="UDS GPA Calculator", page_icon="🎓")

st.title("🎓 UDS GPA Calculator")
st.write("Built by a UDS Computer Science student for the UDS student body. 💙")

programmes = [
    "BSc Computer Science",
    "BSc Mathematics",
    "BSc Computing Mathematics",
    "BSc Statistics",
    "BSc Actuarial Science",
    "BSc Engineering Physics",
    "BSc Chemical Science and Technology"
]

programme = st.selectbox("Select your programme", programmes)
level = st.selectbox("Select your level", ["100", "200", "300", "400"])

grade_points = {
    "A": 4.0,
    "B+": 3.5,
    "B": 3.0,
    "C+": 2.5,
    "C": 2.0,
    "Pass": 1.0,
    "Fail": 0.0
}

st.subheader(f"{programme} - Level {level}")

num_courses = st.number_input(
    "Number of courses this semester",
    min_value=1,
    max_value=15,
    value=6
)

total_points = 0
total_credits = 0

for i in range(int(num_courses)):
    st.markdown(f"### Course {i+1}")

    course_code = st.text_input(
        f"Course Code {i+1}",
        placeholder="Example: CSC103",
        key=f"code{i}"
    )

    credit = st.number_input(
        f"Credit Hours {i+1}",
        min_value=1,
        max_value=6,
        value=3,
        key=f"credit{i}"
    )

    grade = st.selectbox(
        f"Grade {i+1}",
        list(grade_points.keys()),
        key=f"grade{i}"
    )

    total_points += grade_points[grade] * credit
    total_credits += credit

if st.button("Calculate GPA"):
    gpa = total_points / total_credits

    st.success(f"🎉 Your GPA is {gpa:.2f}")

    st.write(f"**Programme:** {programme}")
    st.write(f"**Level:** {level}")
    st.write(f"**Total Credits:** {total_credits}")
    st.write(f"**Total Grade Points:** {total_points:.1f}")

    if gpa >= 3.6:
        st.balloons()
        st.info("🔥 You're on track for First Class!")
    elif gpa >= 3.0:
        st.info("👏 Strong performance! Keep pushing.")
    elif gpa >= 2.0:
        st.warning("⚠️ You can still improve.")
    else:
        st.error("📚 Time to work harder next semester.")
