# python-paraphrase

# Text Paraphrasing Web App

This project is a simple web application that uses the **Parrot** Python-based NLP model to generate paraphrases for given text. The application allows users to input text and get back paraphrased versions, which can be used to enhance writing or improve clarity.

## Features
- Text input box for users to type or paste text.
- Button to submit text for paraphrasing.
- Displays paraphrased versions of the input text.
- Displays an error message if the text is not provided or if any issue occurs.

## Technologies Used
- **Flask**: A lightweight Python web framework used for building the backend.
- **Parrot NLP model**: Used for generating paraphrases of input text.
- **HTML/CSS**: Used for creating the frontend.
- **JavaScript**: To handle form submission, fetch data from the server, and display results dynamically.

## Setup Instructions

### Prerequisites
Make sure you have the following installed:
- **Python 3.8+**
- **Pip** (Python package manager)

### Installation Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/text-paraphrasing-app.git
    cd text-paraphrasing-app
    ```

2. Create a virtual environment:
    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:
    - On Windows:
      ```bash
      venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

4. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Run the Flask application:
    ```bash
    python app.py
    ```

6. Open your browser and go to `http://127.0.0.1:5001` to view the app.

## Contributing

Feel free to fork this project and submit issues or pull requests. If you want to add new features or improve the UI, I welcome contributions!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
