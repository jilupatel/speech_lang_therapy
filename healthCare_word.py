from flask import Flask, render_template, jsonify, request
import pyttsx3
import speech_recognition as sr
import threading

app = Flask(__name__)

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set properties (optional)
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 1.0)  # Volume level (0.0 to 1.0)

# Initialize the speech recognition engine
recognizer = sr.Recognizer()

# List of words
words = ['apple', 'banana', 'orange', 'grapes', 'mango', 'potato']
current_word_index = 0

# Lock for thread-safe access to the speech engine
engine_lock = threading.Lock()

# Function to speak a word
def speak_word(word):
    with engine_lock:
        engine.say(word)
        engine.runAndWait()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/speak_word', methods=['POST'])
def speak_word_route():
    global current_word_index
    if current_word_index < len(words):
        word = words[current_word_index]
        speak_word(word)
        return jsonify({'word': word})
    else:
        return jsonify({'message': 'No more words to say!'})

@app.route('/listen_for_word', methods=['POST'])
def listen_for_word():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            spoken_text = recognizer.recognize_google(audio).lower()
            if spoken_text == words[current_word_index]:
                return jsonify({'status': 'correct', 'spoken_word': spoken_text})
            else:
                return jsonify({'status': 'incorrect', 'spoken_word': spoken_text})
        except sr.UnknownValueError:
            return jsonify({'status': 'error', 'message': 'Sorry, I didn\'t catch that. Please try again.'})
        except sr.RequestError:
            return jsonify({'status': 'error', 'message': 'Sorry, there was a problem with the speech recognition service.'})

@app.route('/next_word', methods=['POST'])
def next_word():
    global current_word_index
    if current_word_index < len(words) - 1:
        current_word_index += 1
        return jsonify({'status': 'success', 'message': 'Next word available.'})
    else:
        return jsonify({'status': 'error', 'message': 'No more words available.'})

if __name__ == '__main__':
    app.run(debug=True)
