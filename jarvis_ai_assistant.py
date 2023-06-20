import os
import openai
import speech_recognition as sr
import pyttsx3

# Initialize speech recognition and text-to-speech engines
r = sr.Recognizer()
engine = pyttsx3.init()

# Function to convert speech to text
def speech_to_text():
    with sr.Microphone() as source:
        audio_data = r.listen(source)
        text = r.recognize_google(audio_data)
        return text

# Function to communicate with OpenAI's GPT-3
def communicate_with_gpt3(text):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=text,
        max_tokens=100,
        temperature=0.5
    )
    return response.choices[0].text.strip()

# Function to convert text to speech
def text_to_speech(text):
    engine.say(text)
    engine.runAndWait()

# Main function to run the AI assistant
def run_ai_assistant():
    print("Listening...")
    command = speech_to_text()
    print("Processing command...")
    response = communicate_with_gpt3(command)
    print("Responding...")
    text_to_speech(response)

run_ai_assistant()
