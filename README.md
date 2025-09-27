# Search Agent with Tavily and Streamlit

This project is a simple search agent that uses the Tavily Search API to answer questions and is deployed with a Streamlit user interface.

## Prerequisites

- Python 3.8+
- An API key from [Tavily](https://tavily.com/)
- An API key from [Cohere](https://cohere.com/)

## Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file** in the root of the project and add your API keys:
   ```
   TAVILY_API_KEY="your_tavily_api_key"
   COHERE_API_KEY="your_cohere_api_key"
   ```

## Running the Application

To run the Streamlit application, use the following command:

```bash
streamlit run app.py
```

This will open a new tab in your browser with the application running.