import streamlit as st
from api import submit_data
from form import create_insurance_form

def main():
    st.title("Insurance Information Form")
    form_data = create_insurance_form()

    if form_data:
        st.subheader("Processing your data...")
        response = submit_data(form_data)
        if response:
            st.success("Data submitted successfully!")
            st.json(response)
        else:
            st.error("Failed to submit data.")

if __name__ == "__main__":
    main()
