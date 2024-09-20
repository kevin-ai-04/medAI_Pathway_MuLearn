## About

MedAI accepts the name of a medicine and fetches data on that medicine from 1mg.com, a reliable source of information on common prescriptions. 1mg.com is a well-known healthcare platform that provides comprehensive and accurate information on medicines, making it a trusted source for medical data. Powered by the Pathways framework, MedAI gathers content in real-time and then uses the Gemini AI model for chat completion.

## Why Real-Time Processing?
MedAI’s use of real-time processing ensures that the information fetched is the latest available, which is crucial when dealing with healthcare data. Medicines and prescriptions can change frequently with new research, availability, or updates to drug information. By leveraging Pathway’s real-time indexing and processing capabilities, MedAI can always provide users with the most current data, making it a valuable tool for healthcare professionals and patients alike. This real-time feature also allows for immediate updates when any new medical information becomes available on external platforms like 1mg.com.

## Demo

> [Video Demo](https://www.youtube.com/watch?v=WMe5C4dQzeU)

## Screenshots
![image](https://github.com/user-attachments/assets/0d375a2e-3238-4ad4-a505-922c534d887a)
![image](https://github.com/user-attachments/assets/7b5d89fe-3458-4540-8f7a-20106996e09f)



## Requirements
1. **Creating a Custom Search Engine**:
   - **Visit**: [Google Custom Search Engine](https://cse.google.com/cse/).
   - **Add a New Search Engine**: 
     - Click **"Add"**.
     - Specify the sites in **"Sites to search"** (use `*.com` for the entire web).
     - Provide a **name**.
     - Click **"Create"**.
   - **Get the Search Engine ID**:
     - In the **Overview** section after creation.

2. **Creating an API Key**:
   - **Visit**: [Google Cloud Console](https://console.cloud.google.com/).
   - **Create a New Project**:
     - Click **project dropdown** > **"New Project"**.
     - Name your project and click **"Create"**.
   - **Enable Custom Search API**:
     - Go to **API Library** > search for **"Custom Search API"** > **Enable**.
   - **Create API Key**:
     - Go to **Credentials** > **"Create Credentials"** > **"API Key"**.
     - Copy and store the **API key** securely.

3. **Setting Up Environment Variables**:
   - **Create a `.env` file**:
     ```env
     GOOGLE_API_KEY=your_api_key_here
     GOOGLE_CSE_ID=your_cse_id_here
     GEMINI_API_TOKEN=your_gemini_api_token_here
     EMBEDDER_LOCATOR=models/text-embedding-004
     EMBEDDING_DIMENSION=768
     MODEL_LOCATOR=gemini/gemini-pro
     MAX_TOKENS=8000
     TEMPERATURE=0.0
     HOST="localhost"
     ```

<br>

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/kevin-ai-04/medAI_Pathway_MuLearn.git
    ```

2. Create a virtual environment:
    ```sh
    python3 -m venv Env/pathw
    ```

3. Activate the virtual environment:
    ```sh
    source Env/pathw/bin/activate
    ```

4. Install the required packages:
    ```sh
    pip install --upgrade -r requirements.txt
    ```

After completing these steps, your environment should be ready to run the project.



## Running

### Starting the Pathway Backend
1. Navigate to the directory with the `main.py` file.
2. Run the Pathway backend:
    ```sh
    python main.py
    ```

### Starting the Streamlit UI
1. Navigate to the `ui` directory.
2. Run the Streamlit UI:
    ```sh
    streamlit run ui.py
    ```
