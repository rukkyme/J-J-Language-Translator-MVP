#!/usr/bin/python3

from flask import Flask, request, render_template, jsonify
from googletrans import LANGUAGES, Translator

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    text = request.form['text']
    source_lang = request.form['source']
    target_lang = request.form['target']

    if text and source_lang and target_lang:
        # Create a translator instance
        translator = Translator(service_urls=['translate.google.com'])

        # Translate the text
        result = translator.translate(text, src=source_lang, dest=target_lang)

        # Return the translated text as JSON response
        return jsonify({'translatedText': result.text})

    return jsonify({'error': 'Missing text, source language, or target language.'})

if __name__ == '__main__':
    app.run(debug=True)

