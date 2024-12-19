from flask import Flask, render_template, request, jsonify
from googletrans import Translator
from google_translate_constants import languages
import speech_recognition as sr
from gtts import gTTS
import os
import tempfile

app = Flask(__name__)
translator = Translator()

@app.route('/')
def home():
    return render_template('index.html', langs=languages)

@app.route('/translate', methods=['POST'])
def translate():
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

    return jsonify({'translated_text': translated_text})

@app.route('/stt', methods=['POST'])
def stt():
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            print("Say something...")
            audio = recognizer.listen(source)

        text = recognizer.recognize_google(audio)
        return jsonify({'text': text})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/tts', methods=['POST'])
def tts():
    text = request.form.get('text')
    if text:
        tts = gTTS(text, lang='en')
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
        tts.save(temp_file.name)
        return jsonify({'audio_url': temp_file.name})
    else:
        return jsonify({'error': 'No text provided for TTS.'})

if __name__ == '__main__':
    app.run(debug=True)
