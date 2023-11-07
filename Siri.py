import speech_recognition as sr
import webbrowser

def listen_and_execute():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening for your command...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for noise levels
        audio = recognizer.listen(source, timeout=10)

    try:
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)

        if "search" in command:
            query = command.replace("search", "").strip()
            search_url = f"https://www.google.com/search?q={query}"
            webbrowser.open(search_url)
        else:
            print("Sorry, I don't understand the command.")

    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
    except sr.RequestError as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    while True:
        listen_and_execute()