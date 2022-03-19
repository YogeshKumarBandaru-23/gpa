import streamlit as st

st.set_page_config( page_title = "CalcGPA", page_icon = None) 
#for page title & favicon


def grades(marks):
    if marks >= 90:
        grade = 10
    elif marks >= 75:
        grade = 9
    elif marks >= 65:
        grade = 8
    elif marks >= 55:
        grade = 7
    elif marks >= 50:
        grade = 6
    elif marks >= 45:
        grade = 5
    elif marks >= 40:
        grade = 4
    else:
        grade = 0
    
    return grade



def calc(sem):
    subjects = {}
    labs = {}
    GPA = 0
    flag = 0  #for the warning message when marks haven't entered
    credits = 0
    col1, col2 = st.columns(2)  #for columns: one for theory sub, and another for lab sub

    if sem == 1 :
        subjects = { 'App. Maths-I' : 4, 'App. Physics-I' : 3, 'Manufacturing Processes' : 4, 'Electrical Science.' : 3, 'Communication Skills' : 3, 'App. Chemistry' : 3 }
        labs = { 'App. Physics Lab-I' : 1, 'Elecrical Science Lab' : 1,'Engg. Graphics Lab' : 2,'App. Chemistry Lab' : 1 }
        credits = 25

    elif sem == 2:
        subjects = { 'App. Maths-II' : 4, 'App. Physics-II' : 3, 'Indian Constitution' : 2, 'Programming in C' : 3, 'Engineering Mechanics' : 3, 'Human Values and Ethics' : 1, 'Environmental Studies' : 3 }
        labs = { 'App. Physics Lab-II' : 1, 'Programming in C Lab' : 1, 'Workshop lab' : 2, 'EVS Lab' : 1,'Engg. Graphics II Lab':1 }
        credits = 25

    elif sem == 3:
        subjects = { 'App. Maths-III' : 4, 'Foundation of CS' : 4, 'Switching Theory & Logic Design' : 4, 'Circuits & Systems' : 4, 'Data Structures' : 4, 'Computer Graphics & Multimedia' : 4, }
        labs = { 'STLD Lab' : 1, 'Data Stucture Lab' : 1, 'Circuits & Systems Lab' : 1, 'CGMM Lab' : 1 }
        credits = 28

    elif sem == 4:
        subjects = { 'App. Maths-IV' : 4, 'Computer Organisation & Architecture' : 4, 'Theory of Computation' : 4, 'Database Management' : 4, 'Object Oriented Programming' : 3, 'Communication Systems' : 4 }
        labs = { 'App. Maths Lab' : 1, 'COA Lab' : 1, 'DBMS Lab' : 1, 'OOPS Lab' : 1, 'Communication Systems Lab' : 1 }
        credits = 28

    elif sem == 5:
        subjects = { 'Algo. Design & Analysis' : 4, 'Software Engineering' : 4, 'Java Programming' : 4, 'Industrial Management' : 3, 'Digital Communications' : 4, 'Communication Skills for Professionals' : 1 }
        labs = { 'Algo. Design Lab' : 1, 'Software Engineering Lab' : 1, 'Java Programming Lab' : 1, 'In-house Workshop' : 1, 'Digital Communications Lab' : 1, 'Communication Skills for Professionals Lab' : 1 }
        credits = 26

    elif sem == 6:
        subjects = { 'Compiler Design' : 4, 'Operating Systems' : 4, 'Computer Networks' : 4, 'Web Engineering' : 3, 'Artificial Intelligence' : 4, 'Microprocessors & Microcontrollers' : 4, }
        labs = { 'Operating Systems Lab' : 1, 'Computer Networks Lab' : 1, 'Web Engineering Lab' : 1, 'Microprocessor & Microcontroller Lab' : 1 }
        credits = 27

    elif sem==7:
        subjects = { 'Information Security' : 4, 'Software Testing and Quality Assurance' : 3, 'Wireless Communcation' : 3, 'Elective Group-A' : 3, 'Elective Group-B' : 3}
        labs={'Information Security Lab' : 1,'Software Testing and QA Lab' : 1, 'Wireless Communcation Lab' : 1, 'Lab based on Elective I or II' : 1, 'Summer Training/Industrial Workshop/Certification' : 1, 'Minor Project +' : 3}
        credits = 24

    elif sem==8:
        subjects = {'Mobile Computing' : 4, 'Machine Learning' : 3, 'Human Values and Professional Ethics-II' : 1, 'Elective Group-A' : 3, 'Elective Group-B' : 3}
        labs={'Mobile Computing Lab' : 1, 'Machine Learning Lab' : 1, 'Lab based on Elective-I' : 1, 'Lab based on Elective-II' : 1, 'Major Project' : 8}
        credits = 26

    with col1:
        with st.expander("Theory Subjects"):
            for subject in subjects:
                marks = st.number_input("{}:".format( subject ), 0, 100)
                if marks == 0 :
                    flag = 1
                num = grades(marks)
                GPA += num * subjects[subject]

    with col2:
        with st.expander("Practical Subjects"):
            for lab in labs:
                marks = st.number_input("{}:".format( lab ), 0, 100)
                if marks == 0 :
                    flag = 1
                num = grades(marks)
                GPA += num * labs[lab]

    if flag:
        st.warning("You haven't entered the marks of all subjects!")

    GPA = GPA / credits
    return GPA

    

st.markdown("<h1 style='text-align: center; color: red;'>CalcGPA</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; '>Semester GPA Calculator of B.Tech(CSE)</h3>", unsafe_allow_html=True)

with st.container():
    name = st.text_input("ENTER YOUR NAME")

    if name:
        st.write("Hello {}!".format(name))
        sem = st.number_input("ENTER YOUR SEMESTER", 0, 8)

        if sem:
            st.write("")
            st.write("")
            st.markdown("<h3 style='text-align: center; '>Enter Marks!</h3>", unsafe_allow_html=True)

            GPA = calc(sem)

            st.write("")
            st.write("")

            cl1, cl2, cl3, cl4, cl5, cl6, cl7, cl8, cl9 = st.columns(9) #just for formatting XD
            with cl5:
                ans = st.button("Submit")
                
            
            
    
            if ans:
                msg = "Your GPA: {}".format(str(round(GPA,2)))
                st.markdown(f"<h3 style='text-align: center; '>{msg}</h3>", unsafe_allow_html=True)
                if GPA >= 8.0 :
                    st.balloons()
                    st.balloons()
                    st.balloons()



