# import pyttsx3
# import speech_recognition as sr

# engine = pyttsx3.init()

# engine.setProperty('rate', 150) 
# engine.setProperty('volume', 1.0) 


# recognizer = sr.Recognizer()


# alphabet = ["A", "B", "C", "D"]

# def speak_letter(letter):
#     print(f"Letter: {letter}")
#     engine.say(letter)
#     engine.runAndWait()

# def listen_for_letter():
#     with sr.Microphone() as source:
#         print("Please repeat the letter...")
#         audio = recognizer.listen(source)
#         try:
#             spoken_text = recognizer.recognize_google(audio)
#             return spoken_text.upper()  
#         except sr.UnknownValueError:
#             print("Sorry, I didn't catch that. Please try again.")
#             return None
#         except sr.RequestError:
#             print("Sorry, there was a problem with the speech recognition service.")
#             return None


# for letter in alphabet:
#     correct = False
#     while not correct:
#         speak_letter(letter)
#         spoken_letter = listen_for_letter()
        
#         if spoken_letter == letter:
#             print(f"Correct! You said: {spoken_letter}")
#             correct = True
#         else:
#             print(f"Incorrect. You said: {spoken_letter}. Let's try again.")



import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()

engine.setProperty('rate', 150) 
engine.setProperty('volume', 1.0) 

recognizer = sr.Recognizer()

words = ['apple', 'banana', 'orange', 'grapes', 'mango', 'potato', 'tomato', 'carrot', 'peach', 'pear']

def speak_word(word):
    print(f"Word: {word}")
    engine.say(word)
    engine.runAndWait()

def listen_for_word():
    with sr.Microphone() as source:

        recognizer.adjust_for_ambient_noise(source, duration=1)  
        print("Please repeat the word...")
        
        
        try:
            
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
           
            spoken_text = recognizer.recognize_google(audio)
            return spoken_text.lower()  
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that. Please try again.")
            return None
        except sr.RequestError as e:
            print(f"Could not request results from the speech recognition service; {e}")
            return None


for word in words:
    correct = False
    while not correct:
        speak_word(word)
        spoken_word = listen_for_word()
        
        if spoken_word is None:
            print("Let's try that again.")
        elif spoken_word == word:
            print(f"Correct! You said: {spoken_word}")
            correct = True
        else:
            print(f"Incorrect. You said: {spoken_word}. Let's try again.")
            
            engine.say(f"The correct pronunciation is {word}")
            engine.runAndWait()
