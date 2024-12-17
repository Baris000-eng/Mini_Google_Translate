from flask import Flask, render_template, request
from googletrans import Translator 

app = Flask(__name__)

translator = Translator()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    # Get the text and target language choice from the form
    text = request.form.get('text')
    target_language = request.form.get('target_language')

    if text:
        try:
            # Translate the text to the target language
            translated_text_object = translator.translate(text, dest=target_language)
            translated_text = translated_text_object.text
        except Exception as e:
            translated_text = f"Error during translation: {e}"
    else:
        translated_text = "Please provide some text to translate."

     
    return render_template('index.html', translated_text=translated_text, text=text, target_language=target_language)

if __name__ == '__main__':
    app.run(debug=True)
