from flask import Flask, render_template, request, jsonify
from parrot import Parrot
import os
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
parrot = Parrot()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/paraphrase', methods=['POST'])
def paraphrase():
    data = request.get_json()
    text = data.get('text', '')

    if text:
        try:
            # Get paraphrases from Parrot
            result = parrot.rephrase(text)
            logging.debug(f"Generated paraphrases (raw): {result}")

            # Handle different types of results
            if isinstance(result, list):
                if all(isinstance(item, tuple) and len(item) == 2 for item in result):
                    paraphrases = [item[0] for item in result]  # Extract paraphrases
                    return jsonify({'paraphrased_texts': paraphrases})
                else:
                    return jsonify({'paraphrased_texts': result})  # Treat as list of paraphrases
            elif isinstance(result, str):
                return jsonify({'paraphrased_texts': [result]})  # Single string result wrapped in a list
            elif isinstance(result, tuple):
                # If the result is a tuple, return the first element (paraphrase)
                return jsonify({'paraphrased_texts': [result[0]]})  # Take only the paraphrased text
            elif isinstance(result, dict):
                if 'paraphrases' in result:
                    return jsonify({'paraphrased_texts': result['paraphrases']})
                else:
                    logging.error('Unexpected dictionary format from Parrot')
                    return jsonify({'error': 'Unexpected dictionary format from Parrot'}), 400
            else:
                logging.error(f"Unexpected result type: {type(result)}")
                return jsonify({'error': 'Unexpected result format from Parrot'}), 400

        except Exception as e:
            logging.error(f"Error during paraphrasing: {e}")
            return jsonify({'error': 'An error occurred while paraphrasing the text'}), 500

    return jsonify({'error': 'No text provided'}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5001)
