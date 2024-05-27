# LLM-chat-app
This application leverages a Language Learning Model (LLM) to provide interactive chat capabilities. Unlike basic LLM models, which process each input independently, this LLM chat model maintains the context of previous interactions. This allows it to generate responses that are informed by the history of the user's chat session.

# Working 
The LLM chat model stores the chat history in session storage. This stored context is then used to generate responses that are relevant to the ongoing conversation, providing a more coherent and contextually appropriate interaction experience.

# Requirements: 
1. Langchain
2. Streamlit (for interface)
3. Gemini API Key

To use this application, follow this steps:
1. Clone this repo
2. Install the required dependencies in the requirements.txt file
3. Add your API key in the code
4. Start the streamlit app;ication using the command 'streamlit run app.py'
