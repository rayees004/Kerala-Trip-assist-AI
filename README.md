# Kerala Trip Assist AI

## Project Description
Kerala Trip Assist AI is a smart travel chatbot built with Python and Streamlit. It helps users plan trips in Kerala by answering travel questions, suggesting tourist places, recommending food, and guiding trip planning using a language model.

## Project Working Report
This project uses a Streamlit web app that connects to the OpenRouter API with an OpenAI-compatible client. The app stores conversation history in the browser session and responds to user messages as a Kerala travel assistant.

The system works like this:
- The app loads environment variables from a .env file.
- It initializes the OpenAI client using the API key from OPENAI_API_KEY.
- A system prompt is set to act like a professional Kerala trip planner.
- User messages are sent to the LLM along with prior chat context.
- The model returns travel guidance, which is displayed in the chat interface.

This makes the project useful for tourism support, trip planning, and destination suggestions in a simple web-based interface.

## How to Use the Project

### 1. Install Python dependencies
Open the project folder in a terminal and run:

```bash
pip install -r requirments.txt
```

### 2. Set up your API key
Create a `.env` file in the project folder and add your key:

```env
OPENAI_API_KEY=your_api_key_here
```

### 3. Run the app locally
Start the application with:

```bash
streamlit run chatbotai.py
```

### 4. Open in the browser
After running the command, Streamlit will display a local URL similar to:

```text
http://localhost:8501
```

Open that URL in your browser to use the Kerala Trip Assistant.

## Features
- Kerala-focused travel guidance
- Tourist place recommendations
- Trip planning assistance
- Food and local experience suggestions
- Chat-based interface using Streamlit
- Session-based chat memory for ongoing conversation
- Easy local deployment with Python and Streamlit

## Project Local Host Setup
The project runs locally using Streamlit's built-in server. The default local host address is:

```text
http://localhost:8501
```

If the app does not open, ensure:
- Python is installed
- Dependencies are installed
- The `.env` file has a valid OPENAI_API_KEY
- The Streamlit server is started from the project folder

## Technologies Used
- Python
- Streamlit
- OpenAI-compatible API via OpenRouter
- Python-dotenv

## Notes
This is a lightweight AI travel assistant project designed for local use and learning. It can be expanded by adding features such as hotel suggestions, route planning, budget calculations, and destination maps.
