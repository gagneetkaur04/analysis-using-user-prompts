# Query Your CSV

## ABOUT THE APP
This application demonstrates an innovative use of AI for analyzing and interacting with data in CSV files through natural language, combined with data visualization capabilities.

## HOW TO USE

To operate the app, follow the steps on the command line:
1. `python -m venv myenv`
2. To activate the enviroment:
     Powershell : `myenv\Scripts\activate`
     Bash: `source myenv/bin/activate`
3. `pip install -r requirements.txt`
4. You need to add GOOGLE_API_KEY in .env file. You can generate a key from [here](https://aistudio.google.com/app/apikey) .
5. `streamlit run main.py`

## ABOUT THE CODE

- ### `generate_repsonse()`
The `generate_response` function is designed to process a natural language query against a CSV file and return a response. This is done by using a combination of Google's generative AI and a custom agent tailored to work with CSV files. This function showcases a sophisticated integration of natural language processing and data analysis, enabling users to query structured data in CSV format using conversational language. The use of a deterministic AI model (`temperature=0`) ensures consistent and reliable interpretations of the queries, while the custom CSV agent facilitates the direct application of these capabilities to CSV file contents.

- ### `save_uploadedfile()`
The `save_uploadedfile` function is designed to save an uploaded file to a temporary directory on the server or local filesystem. This function is a utility for handling file uploads in a web application or script, saving uploaded files to a specified directory (`tempDir` in this case), and then returning the path to the saved file. It ensures that the directory exists before saving and handles the file in binary mode, making it suitable for any file type.

### `plot_exists()`
The `plot_exists` function is carefully designed to search for a plot within a provided output or a series of processing steps, returning the plot's figure if found. If no plot is detected, it defaults to returning the original output, ensuring versatility and robustness in handling various types of responses.

## `main()`
The `main` function orchestrates a Streamlit web application interface that interacts with CSV files using Google's generative AI. Users can upload CSV files, input prompts, and receive AI-generated responses.
