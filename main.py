import streamlit as st
import pandas as pd
from PIL import Image

# --- Load Logo ---
st.image("s2m-logo.png", width=150)

# --- Load Login CSV ---
login_df = pd.read_csv("login coder.csv")

# --- Login Inputs ---
username = st.text_input("Username")
password = st.text_input("Password", type="password")

# --- Login Button ---
if st.button("Login"):
    if (login_df["Username"] == username).any():
        stored_pass = login_df.loc[login_df["Username"] == username, "Password"].values[0]
        role = login_df.loc[login_df["Username"] == username, "Role"].values[0]

        if password == stored_pass:
            st.success(f"Logged in as {role}")

            # Load gspread and Google Sheet only after login
            import gspread
            from gspread_dataframe import set_with_dataframe, get_as_dataframe

            # Authenticate with Google
            try:
                gc = gspread.service_account_from_dict(st.secrets["gspread"])
                sh = gc.open("S2M_Production_Data")
                worksheet = sh.sheet1
                df = pd.DataFrame()

                if role.lower() == "coder":
                    st.subheader("Coder Form")
                    # --- You can add form components here ---
                    st.info("Form for coders coming soon...")

                elif role.lower() == "admin":
                    st.subheader("Admin Panel")
                    df = get_as_dataframe(worksheet).dropna(how="all")
                    st.dataframe(df)

            except Exception as e:
                st.error("Failed to connect to Google Sheet.")
                st.exception(e)
        else:
            st.error("Incorrect password")
    else:
        st.error("Username not found")
