import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests

recognition = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "c4df787c58c448938afde8b1a8cf"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(command):
    command_lower = command.lower()

    if "open google" in command_lower:
        webbrowser.open("https://google.com")
    elif "open facebook" in command_lower:
        webbrowser.open("https://facebook.com")
    elif "open linkedin" in command_lower:
        webbrowser.open("https://linkedin.com")
    elif "open youtube" in command_lower:
        webbrowser.open("https://youtube.com")
    elif command_lower.startswith("play"):
        parts = command_lower.split(" ")
        if len(parts) > 1:
            song = parts[1]
            if song in musicLibrary.music:
                link = musicLibrary.music[song]
                webbrowser.open(link)
            else:
                speak(f"Sorry, I don't have {song} in the library.")
        else:
            speak("Please specify the song to play.")
    elif "news" in command_lower:
        try:
            r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
            if r.status_code == 200:
                data = r.json()
                articles = data.get("articles", [])
                if not articles:
                    speak("Sorry, I could not find any news right now.")
                else:
                    speak("Here are the top news headlines.")
                    for i, article in enumerate(articles[:5], start=1):
                        speak(f"{i}. {article['title']}")
            else:
                speak("Sorry, I could not fetch the news at the moment.")
        except Exception as e:
            speak("An error occurred while fetching news.")
            print(f"News fetch error: {e}")
    else:
        # Here you can add integration with OpenAI or other fallback handlers if needed
        speak("Sorry, I did not understand that command.")

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                audio = recognition.listen(source, timeout=2, phrase_time_limit=1)
                word = recognition.recognize_google(audio)
                print(f"Heard word: {word}")
                if word.lower() == "jarvis":
                    speak("Yes?")
                    with sr.Microphone() as source:
                        print("Jarvis is active, listening for command...")
                        audio = recognition.listen(source)
                        command = recognition.recognize_google(audio)
                        print(f"Command received: {command}")
                        processCommand(command)

        except Exception as e:
            print(f"Error: {e}")
