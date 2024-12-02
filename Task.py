#Web App to collect customer feedback 
import streamlit as st
from prettytable import PrettyTable

st.set_page_config(page_title="Customer Feedback", layout="centered")
st.title("Customer Service Feedback Form")
st.write("""Please take a moment to give us your feedback about your recent experience with our services. Your insight are crucial in helping us improve""")

with st.form("feedback_form"):
    name = st.text_input("Your Name")
    message = st.text_area("Feedback Message")
    rating = st.selectbox("Rating", [1, 2, 3, 4, 5])
    st.write("""1 - Very Satified, 2- Satisfied, 3- Neutral , 4 - Dissatisfied , 5 - Very Dissatisfied """)
    submitted = st.form_submit_button("Submit")

if "feedback_list" not in st.session_state:
    st.session_state.feedback_list = []   

if submitted:
    feedback = {"name": name, "message": message, "rating": rating}
    st.session_state.feedback_list.append(feedback)
    st.success("Feedback submitted successfully!")

def display_feedback():
    if st.session_state.feedback_list:
        st.write("### Submitted Feedback")
        for feedback in st.session_state.feedback_list:
            st.write(f"**Customer Name:** {feedback['name']}")
            st.write(f"**Feedback message:** {feedback['message']}")
            st.write(f"**Rating:** {feedback['rating']}")
            st.write("-----------------------------------")

def display_tabular_feedback():
    if st.session_state.feedback_list:
        st.write("### Submitted Feedback")
        table = PrettyTable()
        table.field_names = ["Customer Name", "Feedback message", "Rating"]
        for feedback in st.session_state.feedback_list:
            table.add_row([feedback["name"], feedback["message"], feedback["rating"]])
        st.text(table)

#display_feedback()
display_tabular_feedback()