import streamlit as st
from PIL import Image
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

# Load the image for the page icon
image = Image.open(r"C:\Users\hp\Downloads\iconfinder-blog-4661578_122455.png")

def getLLamaresponse(input_text, no_words, blog_style, user_name, description, content_type):

    ### LLama2 model
    llm = CTransformers(model="Model\llama-2-7b-chat.ggmlv3.q8_0.bin",
                        model_type='llama',
                        config={'max_new_tokens':256,
                                'temperature':0.01})

    # Prompt Template
    template = """
    You are a professional blog writer. Write a {content_type} blog post for a {blog_style} job profile on the topic "{input_text}" within {no_words} words.
    Include the following description for context: {description}.
    This blog is written by {user_name}.
    Ensure the blog is engaging, informative, and provides valuable insights.
    """
    
    prompt = PromptTemplate(input_variables=["blog_style", "input_text", 'no_words', 'user_name', 'description', 'content_type'],
                            template=template)

    # Generate the response from the LLama 2 model
    response = llm(prompt.format(blog_style=blog_style, input_text=input_text, no_words=no_words, user_name=user_name, description=description, content_type=content_type))
    print(response)
    return response

# Set page configuration
st.set_page_config(page_title="BLOG GENERATOR",
                   page_icon=image,
                   layout='centered',
                   initial_sidebar_state='collapsed')

st.header("Blog Generator")

# Input fields
user_name = st.text_input("Enter Your Name")
input_text = st.text_input("Enter the Blog Topic")
description = st.text_area("Enter a Brief Description of the Blog Topic")

# Creating more columns for additional inputs
col1, col2, col3 = st.columns([5, 5, 5])

with col1:
    no_words = st.slider('No of Words', min_value=50, max_value=1000, value=300, step=50)
with col2:
    blog_style = st.selectbox('Writing the blog for',
                              ('Researchers', 'Data Scientist', 'Common People', 'Software Engineers', 
                               'Product Managers', 'Marketing Professionals'), index=0)
with col3:
    content_type = st.selectbox('Type of Content',
                                ('How-to/Tutorial', 'Opinion Piece', 'Case Study', 'Listicle', 'FAQ', 'Narrative', 'Comparison'), index=0)

submit = st.button("Generate")

# Final response
if submit:
    with st.spinner('Generating blog...'):
        st.write(getLLamaresponse(input_text, no_words, blog_style, user_name, description, content_type))
