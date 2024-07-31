from flask import Flask, request, jsonify, render_template
from googletrans import Translator
import os
app = Flask(__name__)
translator = Translator()
@app.route('/')
def home():
    return render_template('Translate.html')
@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()
    text = data['text']
    src_lang = data['src_lang']
    dest_lang = data['dest_lang']
    translation = translator.translate(text, src=src_lang, dest=dest_lang)
    return jsonify({'translated_text': translation.text})
if __name__ == '__main__':
    app.run(debug=True)
