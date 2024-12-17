from flask import Flask, render_template, request
from googletrans import Translator 

app = Flask(__name__)

translator = Translator()

langs = {
    'af': 'Afrikaans',
    'sq': 'Albanian',
    'ar': 'Arabic',
    'hy': 'Armenian',
    'bn': 'Bengali',
    'bs': 'Bosnian',
    'ca': 'Catalan',
    'hr': 'Croatian',
    'cs': 'Czech',
    'da': 'Danish',
    'nl': 'Dutch',
    'en': 'English',
    'eo': 'Esperanto',
    'et': 'Estonian',
    'tl': 'Filipino',
    'fi': 'Finnish',
    'fr': 'French',
    'de': 'German',
    'el': 'Greek',
    'gu': 'Gujarati',
    'hi': 'Hindi',
    'hu': 'Hungarian',
    'is': 'Icelandic',
    'id': 'Indonesian',
    'it': 'Italian',
    'ja': 'Japanese',
    'jw': 'Javanese',
    'ka': 'Georgian',
    'km': 'Khmer',
    'ko': 'Korean',
    'la': 'Latin',
    'lv': 'Latvian',
    'lt': 'Lithuanian',
    'mk': 'Macedonian',
    'ml': 'Malayalam',
    'mr': 'Marathi',
    'my': 'Burmese',
    'ne': 'Nepali',
    'no': 'Norwegian',
    'pl': 'Polish',
    'pt': 'Portuguese',
    'ro': 'Romanian',
    'ru': 'Russian',
    'sr': 'Serbian',
    'si': 'Sinhala',
    'sk': 'Slovak',
    'sl': 'Slovenian',
    'es': 'Spanish',
    'su': 'Sundanese',
    'sw': 'Swahili',
    'sv': 'Swedish',
    'ta': 'Tamil',
    'te': 'Telugu',
    'th': 'Thai',
    'tr': 'Turkish',
    'uk': 'Ukrainian',
    'ur': 'Urdu',
    'vi': 'Vietnamese',
    'cy': 'Welsh',
    'xh': 'Xhosa',
    'yi': 'Yiddish',
    'zu': 'Zulu'
}

@app.route('/')
def home():
    return render_template('index.html', langs=langs)

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

     
    return render_template('index.html', translated_text=translated_text, text=text, target_language=target_language, langs=langs)

if __name__ == '__main__':
    app.run(debug=True)
