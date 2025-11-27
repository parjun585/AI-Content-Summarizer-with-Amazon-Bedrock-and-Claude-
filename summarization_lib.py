import boto3

def get_summary(user_instruction, document_content=None, use_pdf=False):
    """
    Calls AWS Bedrock to summarize content.

    :param user_instruction: The user's prompt (e.g., "Summarize using 5 bullet points").
    :param document_content: Optional custom text provided by the user.
    :param use_pdf: Boolean flag to determine if the fixed PDF should be included.
    :return: The summary text from the model.
    """
    
    doc_message = {"role": "user", "content": []}

    #Conditionally load and add the PDF document
    if use_pdf:
        try:
            with open("amazon-leadership-principles-070621-us.pdf", "rb") as doc_file:
                doc_bytes = doc_file.read()

            doc_message["content"].append({
                "document": {
                    "name": "Amazon Leadership Principles",
                    "format": "pdf",
                    "source": {
                        "bytes": doc_bytes
                    }
                }
            })
        except FileNotFoundError:
            return "Error: The PDF file 'amazon-leadership-principles-070621-us.pdf' was not found."

    #Conditionally add custom text provided by the user
    if document_content:
        # If custom text is provided, add it to the prompt for the model to process
        full_instruction = f"{user_instruction}\n\nCONTENT TO SUMMARIZE:\n{document_content}"
        doc_message["content"].append({"text": full_instruction})
    else:
        # If no custom text, the user_instruction applies directly to the PDF (if used)
        doc_message["content"].append({"text": user_instruction})

    #AWS Bedrock API Call
    session = boto3.Session()
    bedrock = session.client(service_name='bedrock-runtime')
    
    try:
        response = bedrock.converse(
            modelId="us.anthropic.claude-3-7-sonnet-20250219-v1:0",
            messages=[doc_message],
            inferenceConfig={
                "maxTokens": 2000,
                "temperature": 0
            },
        )
        
        return response['output']['message']['content'][0]['text']
        
    except Exception as e:
        return f"Bedrock API Error: {e}"
