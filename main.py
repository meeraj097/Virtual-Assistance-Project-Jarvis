import pyttsx3 as p
import speech_recognition as sr
import datetime

# Initialize the text-to-speech engine
engine = p.init()

# Set the rate of speech
rate = engine.getProperty('rate')
engine.setProperty('rate', 130)

# Set the voice (use index 1 for female voice if available)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to greet the user based on the time of day
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour > 0 and hour < 12:
        return "morning"
    elif hour >= 12 and hour < 16:
        return "afternoon"
    else:
        return "evening"

# Initial greeting
speak("Hello sir, good " + wishme() + ". I'm your Voice Assistant.")

# Function to listen to the user's speech input
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.energy_threshold = 10000
        recognizer.adjust_for_ambient_noise(source, 1.2)
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            # Convert speech to text
            text = recognizer.recognize_google(audio)
            print("You said: " + text)
            return text
        except sr.UnknownValueError:
            speak("Sorry, I did not get that.")
            print("Sorry, I did not get that.")
            return ""
        except sr.RequestError:
            speak("Sorry, my speech service is down.")
            return ""

# Loop to continually listen for user input
while True:
    text = listen().lower()

    # Exit condition
    if "exit" in text or "stop" in text or "goodbye" in text or "bye" in text:
        speak("Goodbye sir, have a nice day!")
        break

    # Handle greetings or inquiries about the assistant's status
    if "what about you" in text:
        speak("I am having a good day, sir. How can I help you?")
        continue

    elif "your name" in text:
        speak("My name is Jarvis.")

    # Respond with current time
    elif 'time' in text:
        time_now = datetime.datetime.now().strftime('%I:%M %p')
        speak(f'Current time: {time_now}')
        print(time_now)

    # Respond with current date
    elif 'date' in text:
        date_now = datetime.datetime.now().strftime('%d-%m-%Y')
        speak(f'Current date: {date_now}')
        print(date_now)

    # Handle jokes
    elif "joke" in text or "jokes" in text:
        speak("Sure sir, get ready for some chuckles.")
        print("Why don’t skeletons fight each other? They don’t have the guts.")

    # Example for weather command (you can integrate with a weather API)
    elif "weather" in text:
        speak("The current temperature in Hyderabad is 30 degrees Celsius.")
        print("The current temperature in Hyderabad is 30 degrees Celsius.")

    # Set a reminder functionality
    elif "set a reminder" in text:
        speak("What should I remind you about?")
        message = listen()
        speak("When should I remind you?")
        time_str = listen()
        # Placeholder: handle the reminder scheduling elsewhere
        speak(f"Reminder set for {time_str} to {message}.")

    # Default response if input isn't recognized
    else:
        speak("Sorry, I didn't understand that. Can you please repeat?")