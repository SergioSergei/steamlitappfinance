import streamlit as st

# Hard-coded blog posts for demonstration
BLOG_POSTS = [
    {
        "title": "Market Update: October 2025",
        "content": "The S&P 500 has shown resilience despite inflation concerns...",
    },
    {
        "title": "Top 5 Investment Tips",
        "content": "1) Diversify... 2) Stay patient... 3) ...",
    },
    {
        "title": "Hello World",
        "content": "This is our first sample blog post!",
    },
]

def run_blog_page():
    st.title("Finance Blog")
    st.write("Here are the latest blog posts:")

    for post in BLOG_POSTS:
        st.subheader(post["title"])
        st.write(post["content"])
        st.write("---")

if __name__ == "__main__":
    run_blog_page()
