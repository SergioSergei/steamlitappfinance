import streamlit as st
import streamlit_authenticator as stauth

# Below is a DEMO user setup. For real usage:
# - Store hashed passwords in a secure file or database
# - Do NOT put plain-text passwords in code
names = ["Alice", "Bob"]
usernames = ["alice123", "bob456"]

# Passwords in plain text just for demo. Use .Hasher() to create hashed versions
passwords = ["123", "abc"]
hashed_passwords = stauth.Hasher(passwords).generate()

# Create authenticator object
authenticator = stauth.Authenticate(
    names, 
    usernames, 
    hashed_passwords,
    "my_cookie_name",     # a unique cookie name
    "my_signature_key",   # a random key for signature
    cookie_expiry_days=1
)

def show_home():
    st.title("Welcome to My Advanced Streamlit App")
    st.write("Use the sidebar or the pages menu to explore:")
    st.write("- **AI Stock Analysis** to query OpenAI about specific stocks")
    st.write("- **Blog** to read some example posts")
    st.write("You’re currently on the Home page.")

def main():
    # Login widget (appears in the main area)
    name, auth_status, username = authenticator.login("Login", "main")
    
    if auth_status is False:
        st.error("Username/password is incorrect.")
    elif auth_status is None:
        st.warning("Please enter your username and password.")
    else:
        # Successfully logged in
        authenticator.logout("Logout", "sidebar")
        show_home()

if __name__ == "__main__":
    st.set_page_config(page_title="My Advanced Streamlit App", layout="wide")
    main()
