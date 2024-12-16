from flask import Flask, render_template, request
from googletrans import Translator

app = Flask(__name__)

# Initialize the translator object
translator = Translator()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    # Get the text and language choice from the form
    text = request.form.get('text')
    target_language = request.form.get('target_language')

    # Perform the translation
    if text:
        translation = translator.translate(text, dest=target_language)
        translated_text = translation.text
    else:
        translated_text = None

    # Render the result page with translated text
    return render_template('index.html', translated_text=translated_text, text=text, target_language=target_language)

if __name__ == '__main__':
    app.run(debug=True)
