import speech_recognition as sr
import pyttsx3
from windows_automation import open_application

# Initialize the recognizer and the TTS engine
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

# Set properties for the TTS engine
tts_engine.setProperty('rate', 130)  # Speed of speech (slower for more natural sound)
tts_engine.setProperty('volume', 1)  # Volume (0.0 to 1.0)
voices = tts_engine.getProperty('voices')
tts_engine.setProperty('voice', voices[1].id)  # Set a feminine voice

def speak(text):
    try:
        tts_engine.say(text)
        tts_engine.runAndWait()
    except Exception as e:
        print(f"Error in speak function: {str(e)}")

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            speak("Sorry, my speech service is down.")
            return ""
        except Exception as e:
            speak(f"An error occurred: {str(e)}")
            return ""

def main():
    speak("Hello, I am your advanced AI assistant. How can I help you today?")
    while True:
        command = listen()
        if command:
            if "open" in command:
                app_name = command.replace("open ", "")
                open_application(app_name)
            elif "exit" in command or "quit" in command:
                speak("Goodbye!")
                break
            else:
                speak("Sorry, I didn't understand that command.")
        else:
            speak("Please say a command.")

if __name__ == "__main__":
    main()