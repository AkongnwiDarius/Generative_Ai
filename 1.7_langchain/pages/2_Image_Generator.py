from tools.image_gen import generate_image
import streamlit as st 

st.title('AI Image Generator')
prompt = st.text_input('What can i do for you')

if st.button('Generate'):
    with st.spinner('Generating...'):
        image = (prompt)
        st.image(image, caption=prompt, use_container_width=True)

