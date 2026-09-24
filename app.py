
import streamlit as st
from groq import Groq

api_key = st.secrets["GROQ_API_KEY"]
client = Groq(api_key=api_key)

st.set_page_config(
    page_title="LinkedIn Post Generator",
    page_icon="💼"
)

st.title("💼 LinkedIn Post Generator")
st.write("Generate professional LinkedIn posts using AI.")

topic = st.text_area(
    "Enter your LinkedIn post topic",
    placeholder="Example: The importance of continuous learning in the AI era"
)

if st.button("Generate LinkedIn Post"):

    if not topic.strip():
        st.warning("Please enter a topic first.")

    else:
        with st.spinner("Generating your LinkedIn post..."):

            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "system",
                        "content": """You are an expert LinkedIn content writer.

Create professional, engaging LinkedIn posts.

Requirements:
- Start with a strong hook.
- Provide useful value.
- Sound natural and human.
- Use short paragraphs.
- Make the post easy to read.
- Encourage meaningful engagement.
- Avoid clickbait.
- Avoid excessive emojis.
- Use 3-5 relevant hashtags.
- Do not mention that AI wrote the post."""
                    },
                    {
                        "role": "user",
                        "content": f"Write a LinkedIn post about: {topic}"
                    }
                ],
                temperature=0.7,
                max_tokens=600
            )

            post = response.choices[0].message.content

        st.subheader("Your LinkedIn Post")
        st.write(post)
