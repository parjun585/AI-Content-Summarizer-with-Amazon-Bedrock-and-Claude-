
# 📄 AI Content Summarizer with Amazon Bedrock and Claude

This is a flexible web application built using **Streamlit** and **AWS Bedrock** that allows users to summarize content using **Anthropic's Claude 3 Sonnet** model.

The application is designed to handle two main input types: **user-uploaded PDF files** and **custom text** pasted directly into the browser, all while allowing the user to provide specific summarization instructions.

---

## ✨ Features

* **Flexible Content Source:** Summarize either an **uploaded PDF file** (handling multimodal input) or **pasted text**.
* **Custom Instructions:** Users can provide detailed instructions (e.g., “Summarize in 5 bullet points,” “Translate to Spanish”) to precisely control the LLM’s output.
* **Powered by Bedrock:** Utilizes the `boto3` `bedrock-runtime` client and the **`converse` API** for a clean, efficient interaction with Claude 3 Sonnet.

---

## 🚀 Setup and Installation

### 1. Prerequisites

You must have the following installed and configured:

* **Python 3.8+**
* **AWS CLI**, configured with credentials that have access to the **Amazon Bedrock Runtime** service.

### 2. Install Dependencies

Install the required Python packages:

```bash
pip install streamlit boto3 pandas numpy
```

### 3. Configure AWS Credentials

Ensure your AWS credentials and configuration files (`~/.aws/credentials` and `~/.aws/config`) are set up correctly.
The IAM user or role must have a policy granting permission to call the **`bedrock:Converse`** action.

---

## ⚙️ How to Run the App

Start the Streamlit application from your terminal:

```bash
streamlit run summarization_app.py
```

The application will automatically open in your web browser.

---

## 📝 Usage Guide

The application guides the user through the following steps:

1. **Select Content Source:** Choose between **"Upload a PDF Document"** or **"Paste Custom Text."**
2. **Input Content:**

   * For PDF, use the **`st.file_uploader`** to select your file.
   * For custom text, paste your content into the text area.
3. **Provide Instructions:** Use the **"How would you like the content summarized?"** input area to specify the desired format, length, or style of the summary.
4. **Generate Summary:** Click the **Generate Summary** button.
   The application sends the content and instructions to Claude 3 Sonnet via Amazon Bedrock and displays the result.

---

## 📁 Project Structure

| File Name              | Description                                                                                                                                                                |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `summarization_app.py` | The main **Streamlit UI** application. Handles all user interaction, conditional rendering of inputs, and data collection.                                                 |
| `summarization_lib.py` | The core **logic module** containing the `get_summary` function, which constructs the Bedrock request (including PDF bytes or text content) and executes the AWS API call. |

---

## 🤝 Contribution

Feedback and contributions are welcome!
If you have suggestions for new features (like adding support for more file types or improving summarization prompts), feel free to open an issue or submit a pull request.


