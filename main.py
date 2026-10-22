import streamlit as st
import string
st.title("Password Strength Checker")
st.write("Check your password strength below.")

password = st.text_input("Enter a sample password", type="password")
if password:
    length = len(password) >= 8
    uppercase = any(c.isupper() for c in password)
    lowercase = any(c.islower() for c in password)
    number = any(c.isdigit() for c in password)
    special = any(c in string.punctuation for c in password)

    score = sum([length, uppercase, lowercase, number, special])

    st.subheader("Password Analysis")
    st.write("Length of 8 or more characters:", "right" if length else "incorrect")
    st.write("Uppercase letter:", "right" if uppercase else "wrong")
    st.write("Lowercase letter:", "right" if lowercase else "wrong")
    st.write("Number:", "right" if number else "wrong")
    st.write("Special character:", "right" if special else "wrong")

    st.write("Password Strength Score:", score, "/ 5")
    st.progress(score / 5)

    if score <= 2:
        st.error("Strength: Weak")
    elif score <= 4:
        st.warning("Strength: Moderate")
    else:
        st.success("Strength: Strong")

    st.subheader("Suggestions")

    if not length:
        st.write("- Use at least 8 characters.")
    if not uppercase:
        st.write("- Add an uppercase letter (A-Z).")
    if not lowercase:
        st.write("- Add a lowercase letter (a-z).")
    if not number:
        st.write("- Add a number (0-9).")
    if not special:
        st.write("- Add a special character (!, @, #, etc.).")
    if score == 5:
        st.write("Great! Your sample password meets all five criteria.")
