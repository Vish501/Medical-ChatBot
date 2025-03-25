# Medical-ChatBot

An AI-powered chatbot designed to assist with medical inquiries by providing information and guidance based on user input.

## Disclaimer

**This Medical ChatBot is for educational purposes only.**  

- This chatbot is **not** a certified medical device and **does not** provide professional medical advice, diagnosis, or treatment.  
- The information provided by this chatbot is **general in nature** and may not be accurate, up-to-date, or applicable to individual cases.  
- **Do not rely on this chatbot for medical decisions.** Always consult a qualified healthcare professional for medical concerns.  
- The creator of this project is **not responsible** for any actions taken based on the chatbot’s responses.  

By using this chatbot, you acknowledge that it is a **educational tool for demonstration purposes only** and should **not** be used for real medical guidance.

## Features

- **Natural Language Understanding**: Utilizes the Gemini API to comprehend and process user inputs.
- **Conversational AI**: Engages in interactive dialogues, providing relevant and coherent responses.
- **Extensible Design**: Structured to allow easy integration of additional functionalities and data.

## Requirements

- Python 3.10.16
- Required Python packages (listed in `requirements.txt`)
- Google API Key for accessing the Gemini AI services
- Pinecone API Key for creating and/or accessing the Pinecone Database

## Installation

1. **Clone the repository**:

     ```bash
     git clone https://github.com/Vish501/Medical-ChatBot.git
    ```
     
     ```bash
     cd Medical-ChatBot
    ```
     
2. **Install dependencies**:

    It's recommended to use a virtual environment to manage dependencies. You can create and activate one using:
   
     ```bash
     conda create -p venv python=3.10.16 -y
    ```
     
     ```bash
    conda activate venv/
   ```
     Then, install the required packages: ```pip install -r requirements.txt```

## Setting Up the Google API Key

To use the Gemini API, you need to set up your GOOGLE_API_KEY:

1. Obtain your **Google API Key** from the **Google Cloud Console**.
2. Add the API key to your environment:
     - Locally (Linux/macOS): ```export GOOGLE_API_KEY="your-api-key-here"```
     - Locally (Windows - Command Prompt): ```set GOOGLE_API_KEY="your-api-key-here"```
     - Locally (Windows - PowerShell): ```$env:GOOGLE_API_KEY="your-api-key-here"```

3. If you are using GitHub Codespaces, store the API key as a GitHub repository secret:
     
     - Go to your GitHub repository
     - Navigate to **Settings > Secrets and variables > Actions**
     - Click **New repository secret**
     - Set the name as ```GOOGLE_API_KEY``` and paste your API key as the value
     - Click **Add secret**

This will allow the chatbot to authenticate and communicate with the Gemini API securely.

## Usage

1. Run the chatbot:

   ```bash
    python app.py
   ```
   
2. Navigate to the webpage: ```localhost:8080/```
  
3. Interact with the bot:

     Access the chatbot interface through the provided web interface and input your medical-related questions to receive information.

## Project Structure

- ```app.py```: Main application script to run the chatbot.
- ```data/```: Directory containing data files used by the chatbot.
- ```research/```: Contains notebook files used to build the application before modulation.
- ```src/```: Hosts importable functions important to the project.
- ```static/```: Static CSS files for the web interface.
- ```templates/```: HTML templates for the web interface.
- ```requirements.txt```: List of Python packages required to run the chatbot.
- ```setup.py```: Script for setting up the package hosted in the src.
- ```store_index.py```: Script related to indexing data for retrieval and if required creating the Pinecone database.
- ```template.py```: Template script to build the structure of the project.

## Acknowledgment

This project utilizes the Gemini API to power the chatbot's language understanding capabilities. For more information, visit the Hugging Face Space.   
