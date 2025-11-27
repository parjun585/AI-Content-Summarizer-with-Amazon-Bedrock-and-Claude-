import streamlit as st
import summarization_lib as glib

st.set_page_config(page_title="Document Summarization")
st.title("Document Summarization")

# Content Source Selection 
content_source = st.radio(
    "Select Content Source:",
    ('Pre-loaded PDF', 'Paste Custom Text'),
    horizontal=True
)

use_pdf = (content_source == 'Pre-loaded PDF')

# Content Input Area (Conditional)
document_text = None 
if use_pdf:
    st.info("The content to be summarized is the pre-loaded PDF: Amazon Leadership Principles.")
else:
    st.subheader("Paste your content below:")
    document_text = st.text_area(
        "Text to summarize:", 
        height=300,
        placeholder="Paste your long paragraph, article, or document text here..."
    )
    # Check if custom content is provided when the custom source is selected
    if not document_text.strip() and st.session_state.get('summarize_clicked'):
        st.error("Please paste content into the text area to summarize.")


# Summarization Instruction
# Any user should be able to ask for any type of content summarization ideas 
instruction_text = st.text_area(
    "How would you like the content summarized? (e.g., 'Use 5 bullet points', 'Explain the key concept in one paragraph')",
    value="Provide a concise summary of the content.",
    height=100
)

# Execution 
summarize_button = st.button("Generate Summary", type="primary")

# Use session state to handle errors when button is clicked but no content is provided
if 'summarize_clicked' not in st.session_state:
    st.session_state['summarize_clicked'] = False

if summarize_button:
    st.session_state['summarize_clicked'] = True
    
    # Validation check for custom text source
    if not use_pdf and not document_text.strip():
        # The error message is handled above, but we stop execution here
        pass 
    else:
        st.subheader("Summary")

        with st.spinner("Running summarization..."):
            response_content = glib.get_summary(
                user_instruction=instruction_text, 
                document_content=document_text, 
                use_pdf=use_pdf
            )
            st.write(response_content)
